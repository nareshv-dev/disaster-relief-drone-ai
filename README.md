🛩️ Disaster Relief Drone AI

An AI-powered drone system that captures aerial video during disaster situations and uses computer vision to detect humans, identify victims, and extract location data to support faster rescue operations.

📌 Overview

During natural disasters such as floods, earthquakes, and landslides, rescue teams struggle to manually search for victims in large and dangerous areas.
This project solves that by using AI + drones to automatically detect people from aerial footage and provide their exact coordinates to rescue teams.

🚀 Features

🛸 Drone Aerial Footage Capture
Drone records video streams from disaster-affected areas.

🎯 AI-Based Human Detection
Uses a YOLO-based object detection model to identify whether people are present.

🌍 Location Extraction (GPS Coordinates)
When a person is detected, the system captures:

Latitude

Longitude

Detection confidence

Bounding box location

🌡️ Thermal Imaging Support (Optional)
Helps detect victims in low-light or underwater flood conditions.

📤 Alert System (Optional)
Sends notifications to disaster response teams when victims are found.

📊 Visualization Dashboard (Optional)
A Streamlit / Web UI to view:

Detected persons

Drone path

Video frames

Mapped coordinates

🧠 Tech Stack

Python

OpenCV

YOLO (v5 / v8)

Drone SDK / API (DJI or custom)

Numpy, Pandas

Streamlit / Gradio (optional)

Thermal Camera Feed (optional)

🛠️ How It Works

The drone flies over the disaster region and captures video.

Frames are extracted from the video using OpenCV.

YOLO model processes each frame to detect humans.

If a person is detected:

Bounding box is produced

Detection confidence is calculated

Drone telemetry data provides GPS coordinates

Coordinates + detection details are saved for rescue teams.

(Optional) Alerts are automatically sent to authorities.

📂 Project Structure (Example)
disaster-relief-drone-ai/
│── models/                # YOLO weights
│── input_videos/          # Drone footage
│── outputs/               # Detection results
│── scripts/
│   ├── detect_victims.py  # Main detection script
│   ├── gps_mapping.py     # GPS extraction logic
│── README.md
│── requirements.txt

▶️ How to Run the Project
1️⃣ Clone the repo
git clone https://github.com/nareshv-dev/disaster-relief-drone-ai.git

2️⃣ Move into the folder
cd disaster-relief-drone-ai

3️⃣ Install required packages
pip install -r requirements.txt

4️⃣ Run the detection script
python detect_victims.py

✔️ Steps You Have Already Completed

Created the GitHub repository

Opened your project folder in VS Code

Initialized Git using git init

Staged your files with git add .

Committed with git commit -m "first commit"

Connected to GitHub using

git remote add origin https://github.com/nareshv-dev/disaster-relief-drone-ai.git


Pushed the project to GitHub

git push -u origin main

🔮 Future Improvements

Live drone video streaming processing

Victim pose estimation (lying, drowning, unconscious)

Real-time map with pinned victim locations

SMS/WhatsApp emergency notifications

Integration with Disaster Relief Dashboard

🤝 Contributions

Feel free to open issues or submit pull requests.
Contributions are welcome!
