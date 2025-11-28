# 🚨 DroneAid — Disaster Relief through Drone-Assisted Victim Identification

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![YOLO](https://img.shields.io/badge/Object--Detection-YOLOv8-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

**A resilient, multi-drone AI system to locate survivors in disaster zones using computer vision, thermal sensing, multisensor fusion, and distributed coordination.**

[Features](#-key-features) • [Quick Start](#-quick-start) • [Architecture](#-project-architecture) • [API](#-api-reference)

</div>

---

## 🌟 Key Features

### 🧠 YOLOv8 Object Detection  
Like a vigilant eye watching over the disaster zone, YOLOv8 scans every frame in real time. The moment it detects a human or animal, it highlights them instantly — ensuring no potential victim goes unnoticed.  

---

### 🎥 OpenCV Live Video Streaming  
OpenCV acts as the heartbeat of the system. It keeps the camera feed flowing smoothly, turning raw visuals into searchable signals, frame after frame, without missing a moment. 

---

### 🌐 Flask-Powered Web Dashboard  
Flask becomes the command center that brings everything together. A lightweight live dashboard displays the feed, detection boxes, and captured alerts — making monitoring effortless on any device.  

---

### ⚙️ Multi-Threaded Processing Engine  
Multiple threads work like a coordinated rescue unit behind the scenes. One captures video, another runs detection, another saves outputs — all in perfect sync, ensuring real-time responsiveness during emergencies.  

---

### 📁 JSON-Based Detection Logging  
Every confirmed detection is stored neatly in `detections.json`. Timestamp, confidence, file paths — all recorded, creating a reliable digital trail that supports faster rescue decisions.


## ⚙️ Tech Stack

#### 🐍 Python --> ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

#### 🌐 Flask --> ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

#### 🤖 YOLOv8 (Ultralytics) --> ![YOLO](https://img.shields.io/badge/YOLOv8-FF6F00?style=for-the-badge&logo=ai&logoColor=white)

#### 🎥 OpenCV --> ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

#### 🧵 Threading --> ![Threading](https://img.shields.io/badge/Threading-FFD43B?style=for-the-badge&logo=python&logoColor=black)

#### 🔗 Requests Library -->![Requests](https://img.shields.io/badge/Requests-000000?style=for-the-badge&logo=python&logoColor=white)

#### 🖼 HTML + Jinja Templates --> ![HTML](https://img.shields.io/badge/HTML-Jinja2-orange?style=for-the-badge)


## 🏗️ Project Architecture

```
drone-rescue-ai/
│
├── 📁 static/                          # Public assets served by Flask
│   ├── 📁 detections/                  # Saved YOLO-annotated output images
│   └── 📁 images/                      # Raw uploaded/test images
│
├── 📁 templates/                       # Flask HTML UI (Jinja2 templates)
│   └── index.html                      # Live video feed + detection dashboard
│
├── app.py                              # Main Flask backend (video stream + YOLO inference)
├── detections.json                     # Auto-generated detection logs (JSON format)
├── yolov8n.pt                          # YOLOv8 model weights (Ultralytics)
├── test.jpg                            # Sample image for testing detection
├── .env                                # Environment variables (API keys, configs)
├── .gitignore                          # Git ignored files
└── README.md                           # Project documentation
```

