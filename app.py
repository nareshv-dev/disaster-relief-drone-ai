from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
import cv2
import os
import time
import json
from ultralytics import YOLO
import requests
import threading

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = YOLO("yolov8n.pt")

DETECTIONS_FILE = "detections.json"
if not os.path.exists(DETECTIONS_FILE):
    with open(DETECTIONS_FILE, "w") as f:
        json.dump([], f)

# Load configuration/secrets from a local file
SECRETS_FILE = "secrets.json"
if os.path.exists(SECRETS_FILE):
    try:
        with open(SECRETS_FILE, "r") as f:
            secrets = json.load(f)
    except Exception as e:
        print(f"Error loading secrets.json: {e}")
        secrets = {}
else:
    secrets = {}

BOT_TOKEN = secrets.get("telegram_bot_token", "")
CHAT_ID = secrets.get("telegram_chat_id", "")

# 🔐 Global video capture lock and camera
camera_lock = threading.Lock()
camera = cv2.VideoCapture(0)


def escape_markdown(text):
    special_chars = r'\_*[]()~`>#+-=|{}.!'
    return ''.join(f'\\{c}' if c in special_chars else c for c in text)


def save_detection(image, gps):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}.jpg"
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    cv2.imwrite(filepath, image)

    with open(DETECTIONS_FILE, "r") as f:
        detections = json.load(f)

    detections.append({
        "image_path": filepath,
        "timestamp": timestamp,
        "gps": gps,
        "status": "Detected"
    })

    with open(DETECTIONS_FILE, "w") as f:
        json.dump(detections, f)

    return filename


@app.route('/')
def index():
    with open(DETECTIONS_FILE, "r") as f:
        detections = json.load(f)
    return render_template('index.html', detections=detections)



@app.route('/detect', methods=['POST'])
def detect():
    gps = request.json.get('gps', 'Unknown')

    with camera_lock:
        ret, frame = camera.read()

    if not ret:
        return jsonify({"error": "Failed to capture image"}), 500

    results = model(frame)
    for r in results:
        person_detected = False
        for box in r.boxes:
            cls = int(box.cls[0])
            if model.names[cls] == "person":
                person_detected = True
                break
        
        if person_detected:
            # Annotate the frame with bounding boxes using YOLO's plot method
            annotated_frame = r.plot()
            filename = save_detection(annotated_frame, gps)
            return jsonify({
                "message": "Person detected!",
                "image": filename,
                "gps": gps
            })

    return jsonify({"message": "No person detected."})


@app.route('/send_alert', methods=['POST'])
def send_alert():
    timestamp = request.form.get('timestamp')

    with open(DETECTIONS_FILE, "r") as f:
        detections = json.load(f)

    for d in detections:
        if d['timestamp'] == timestamp and d['status'] == "Detected":
            d['status'] = "Rescue Sent"
            gps = d['gps']
            img_path = d['image_path']
            gmap_link = f"https://www.google.com/maps?q={gps}"

            escaped_gps = escape_markdown(gps)
            escaped_timestamp = escape_markdown(timestamp)
            escaped_url = gmap_link.replace("&", "\\&").replace("?", "\\?")
            message = (
                f"🚨 Rescue Alert\n\n"
                f"🕒 Timestamp: {escaped_timestamp}\n"
                f"📍 GPS: {escaped_gps}\n"
                f"🗺 [Open in Google Maps]({escaped_url})"
            )

            try:
                requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
                    "chat_id": CHAT_ID,
                    "text": message,
                    "parse_mode": "MarkdownV2"
                })

                with open(img_path, 'rb') as photo:
                    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", data={
                        "chat_id": CHAT_ID
                    }, files={"photo": photo})

            except Exception as e:
                print(f"Failed to send alert: {e}")
            break

    with open(DETECTIONS_FILE, "w") as f:
        json.dump(detections, f)

    return redirect(url_for('index'))


# ✅ Shared live stream from single camera instance
def gen_frames():
    while True:
        with camera_lock:
            success, frame = camera.read()

        if not success:
            break
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
