import numpy as np
from collections import deque

class GestureProcessor:
    def __init__(self):
        self.history = deque(maxlen=20)
        self.smoothed_x = 0
        self.smoothed_y = 0
        print("[Jetson Thor] Gesture Processor Initialized (Smoothing Active)")

    def apply_smoothing(self, x, y):
        # Exponential Moving Average (EMA)
        import config
        self.smoothed_x = (x * (1 - config.SMOOTHING_FACTOR)) + (self.smoothed_x * config.SMOOTHING_FACTOR)
        self.smoothed_y = (y * (1 - config.SMOOTHING_FACTOR)) + (self.smoothed_y * config.SMOOTHING_FACTOR)
        return self.smoothed_x, self.smoothed_y

    def analyze(self, hand_landmarks):
        import config
        if not hand_landmarks:
            return None, None

        lms = hand_landmarks.landmark
        
        # Finger statuses (True if extended)
        fingers = []
        fingers.append(lms[4].x < lms[3].x) # Thumb
        fingers.append(lms[8].y < lms[6].y)  # Index
        fingers.append(lms[12].y < lms[10].y) # Middle
        fingers.append(lms[16].y < lms[14].y) # Ring
        fingers.append(lms[20].y < lms[18].y) # Pinky

        num_fingers = sum(fingers)
        index_tip = (lms[8].x, lms[8].y)
        
        # 1. Open Hand -> Play
        if num_fingers == 5:
            return "OPEN_HAND", None
            
        # 2. Fist -> Stop
        if num_fingers == 0:
            return "FIST", None
            
        # 3. Thumbs Up -> Select/OK
        if fingers[0] and sum(fingers[1:]) == 0:
            return "THUMBS_UP", None
            
        # 4. Two Fingers -> Cursor Control (with Smoothing)
        if fingers[1] and fingers[2] and sum(fingers) == 2:
            raw_x = (lms[8].x + lms[12].x) / 2
            raw_y = (lms[8].y + lms[12].y) / 2
            smooth_coords = self.apply_smoothing(raw_x, raw_y)
            return "TWO_FINGERS", smooth_coords

        # 5. Rotate Index Finger -> Volume (Improved Sensitivity)
        if fingers[1] and sum(fingers) == 1:
            self.history.append(index_tip)
            if len(self.history) >= 5:
                # Find cross product of vectors v1 and v2
                v1 = np.array([self.history[-2][0] - self.history[-3][0], self.history[-2][1] - self.history[-3][1]])
                v2 = np.array([self.history[-1][0] - self.history[-2][0], self.history[-1][1] - self.history[-2][1]])
                cross_prod = np.cross(v1, v2)
                
                if abs(cross_prod) > config.ROTATION_THRESHOLD:
                    return "ROTATE_CLOCKWISE" if cross_prod > 0 else "ROTATE_ANTICLOCKWISE", None

        return "UNKNOWN", None
