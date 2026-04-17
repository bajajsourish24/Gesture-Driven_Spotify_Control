import cv2
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawing
import config

class VisualEngine:
    def __init__(self):
        self.mp_hands = mp_hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=config.MODEL_COMPLEXITY,
            min_detection_confidence=config.MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=config.MIN_TRACKING_CONFIDENCE
        )
        self.mp_draw = mp_drawing
        self.cap = cv2.VideoCapture(config.WEBCAM_INDEX)
        
        # Set resolution for speed
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        print("[Jetson Thor] Visual Engine Initialized (Turbo Mode)")

    def get_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None, None
        
        frame = cv2.flip(frame, 1) # Mirror effect
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        return frame, results

    def draw_landmarks(self, frame, results):
        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
