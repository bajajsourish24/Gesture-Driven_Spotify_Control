import pyautogui
import config

class CursorController:
    def __init__(self):
        pyautogui.FAILSAFE = True
        self.screen_w, self.screen_h = pyautogui.size()
        print("[Jetson Thor] Cursor Controller Initialized")

    def move(self, x, y):
        # Map normalized coordinates (0,1) to screen size
        target_x = x * self.screen_w
        target_y = y * self.screen_h
        pyautogui.moveTo(target_x, target_y, _pause=False)

    def select(self):
        pyautogui.click()
        print("Action: Select (Mouse Click)")
