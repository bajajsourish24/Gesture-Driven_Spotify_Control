<div align="center">

# 🤖 Gesture-Driven Spotify Control
### *Control your music with nothing but your hand*

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-FF6F00?style=for-the-badge&logo=google&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-API-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> A real-time hand-gesture interface that maps physical gestures to Spotify playback actions and system cursor movements — built for the COA Project (Jetson Thor).

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎵 **Spotify Control** | Play, pause, and adjust volume via hand gestures |
| 🖱️ **Cursor Control** | Move your mouse pointer with a two-finger pose |
| ⚡ **Real-Time Processing** | Low-latency MediaPipe hand-landmark detection |
| 🧠 **Gesture Brain** | Modular gesture processor with cooldown & smoothing |
| 🎛️ **Configurable** | Fine-tune sensitivity, thresholds, and camera settings |

---

## 📁 Project Structure

```
gesture-driven-spotify-control/
│
├── src/
│   ├── main.py                 # 🚀 Core application loop
│   ├── gesture_processor.py    # 🧠 Gesture recognition logic
│   ├── spotify_controller.py   # 🎵 Spotify API integration
│   ├── cursor_controller.py    # 🖱️  Mouse movement & click
│   ├── visual_engine.py        # 👁️  MediaPipe + OpenCV feed
│   ├── config.py               # 🔑 Your credentials (git-ignored)
│   └── config.example.py       # 📋 Credential template
│
├── run.py                      # ▶️  Project entry point
├── requirements.txt            # 📦 Dependencies
├── .gitignore                  # 🚫 Ignored files
└── README.md                   # 📖 You are here
```

---

## 🛠️ Installation

### 1 · Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/gesture-driven-spotify-control.git
cd gesture-driven-spotify-control
```

### 2 · Create & activate a virtual environment *(recommended)*
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3 · Install dependencies
```bash
pip install -r requirements.txt
```

### 4 · Configure Spotify credentials
```bash
# Copy the template
cp src/config.example.py src/config.py
```
Then open `src/config.py` and fill in your credentials (see below).

---

## 🎵 Spotify API Setup

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click **Create App**
3. In App Settings → **Redirect URIs**, add: `http://127.0.0.1:8888/callback`
4. Copy your **Client ID** and **Client Secret**
5. Paste them into `src/config.py`:

```python
SPOTIPY_CLIENT_ID     = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
```

> ⚠️ `src/config.py` is **git-ignored** — your credentials will never be committed.

---

## 🖐️ Gesture Reference

| Gesture | Action |
|:---|:---|
| ✋ **Open Hand** | ▶️ Play Music |
| ✊ **Fist** | ⏹️ Stop Music |
| 👍 **Thumbs Up** | 🖱️ System Click (Select) |
| ✌️ **Two Fingers** | 🖱️ Move Mouse Cursor |
| ☝️ **Rotate Index (Clockwise)** | 🔊 Volume Up |
| ☝️ **Rotate Index (Anti-clockwise)** | 🔉 Volume Down |

---

## 🚀 How to Run

Make sure **Spotify** is open on your desktop, then:

```bash
python run.py
```

A window will open showing your **live camera feed** with hand-landmark overlay.  
Press **`Q`** to exit the application.

---

## ⚙️ Configuration

All tuneable parameters live in `src/config.py`:

| Parameter | Default | Description |
|---|---|---|
| `WEBCAM_INDEX` | `0` | Camera device index |
| `MOUSE_SENSITIVITY` | `1.5` | Speed multiplier for cursor movement |
| `SMOOTHING_FACTOR` | `0.65` | Mouse smoothing (0 = raw, 1 = very smooth) |
| `GESTURE_COOLDOWN` | `0.5 s` | Debounce between discrete gestures |
| `ROTATION_THRESHOLD` | `0.0005` | Sensitivity for volume-rotation gesture |
| `MODEL_COMPLEXITY` | `0` | MediaPipe model size (0 = fast, 1 = accurate) |

---

## 🧩 Architecture

```
┌─────────────────────────────────────────────┐
│                   run.py                    │  ← Entry point
└────────────────────┬────────────────────────┘
                     │
          ┌──────────▼──────────┐
          │       main.py       │  ← Orchestration loop
          └──┬──────┬──────┬───┘
             │      │      │
    ┌─────────▼──┐ ┌▼──────────┐ ┌▼───────────────┐
    │ visual_    │ │ gesture_  │ │ spotify_ /      │
    │ engine.py  │ │ processor │ │ cursor_         │
    │ (OpenCV +  │ │ .py       │ │ controller.py   │
    │ MediaPipe) │ │           │ │                 │
    └────────────┘ └───────────┘ └─────────────────┘
```

---

## 📦 Dependencies

```
opencv-python    — Camera capture & display
mediapipe        — Real-time hand landmark detection
pyautogui        — System mouse & keyboard control
spotipy          — Spotify Web API client
python-dotenv    — Environment variable support
numpy            — Numerical operations
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ for the COA Project · Jetson Thor
</div>
