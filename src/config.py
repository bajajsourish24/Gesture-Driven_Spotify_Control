import os

# Spotify Configuration
# Get these from https://developer.spotify.com/dashboard
SPOTIPY_CLIENT_ID = '183aa741d5dd467a92271cbcc0b8c03c'
SPOTIPY_CLIENT_SECRET = 'a9da316128d645e39f9109c45de6423e'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8888/callback'

# Gesture Control Settings
WEBCAM_INDEX = 0
GESTURE_THRESHOLD = 0.7
VOLUME_SENSITIVITY = 0.05
MOUSE_SENSITIVITY = 1.5
MIN_DETECTION_CONFIDENCE = 0.5 # Lowered for speed
MIN_TRACKING_CONFIDENCE = 0.5
MODEL_COMPLEXITY = 0          # 0 is faster, 1 is more accurate
FRAME_WIDTH = 640             # Standard resolution
FRAME_HEIGHT = 480

# Advanced Optimization
SMOOTHING_FACTOR = 0.65       # Range 0-1 (higher = smoother, lower = faster)
ROTATION_THRESHOLD = 0.0005   # Sensitivity for volume rotation
GESTURE_COOLDOWN = 0.5        # Seconds between non-continuous actions
