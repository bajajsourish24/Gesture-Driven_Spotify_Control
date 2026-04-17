import cv2
import time
from visual_engine import VisualEngine
from gesture_processor import GestureProcessor
from spotify_controller import SpotifyController
from cursor_controller import CursorController
import config

def main():
    print("--- Jetson Thor: Real-Time Gesture Control System ---")
    
    visual = VisualEngine()
    processor = GestureProcessor()
    spotify = SpotifyController()
    cursor = CursorController()
    
    last_action_time = 0
    cooldown = config.GESTURE_COOLDOWN
    
    while True:
        frame, results = visual.get_frame()
        if frame is None:
            break
            
        gesture, coords = None, None
        if results.multi_hand_landmarks:
            gesture, coords = processor.analyze(results.multi_hand_landmarks[0])
            frame = visual.draw_landmarks(frame, results)

        current_time = time.time()
        
        # Display Gesture on Screen
        cv2.putText(frame, f"Gesture: {gesture}", (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Action Logic
        if gesture and (current_time - last_action_time > cooldown or "ROTATE" in gesture or "TWO_FINGERS" == gesture):
            
            if gesture == "OPEN_HAND":
                spotify.play()
                last_action_time = current_time
                
            elif gesture == "FIST":
                spotify.stop()
                last_action_time = current_time
                
            elif gesture == "THUMBS_UP":
                cursor.select()
                last_action_time = current_time
                
            elif gesture == "TWO_FINGERS" and coords:
                cursor.move(coords[0], coords[1])
                # No cooldown for smooth mouse movement
                
            elif gesture == "ROTATE_CLOCKWISE":
                spotify.volume_up()
                # Smaller cooldown for rotation
                last_action_time = current_time - (cooldown * 0.8)
                
            elif gesture == "ROTATE_ANTICLOCKWISE":
                spotify.volume_down()
                last_action_time = current_time - (cooldown * 0.8)

        cv2.imshow("Jetson Thor Gesture Engine", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    visual.release()

if __name__ == "__main__":
    main()
