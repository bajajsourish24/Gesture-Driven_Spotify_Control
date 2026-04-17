import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

class SpotifyController:
    def __init__(self):
        self.sp = None
        try:
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=config.SPOTIPY_CLIENT_ID,
                client_secret=config.SPOTIPY_CLIENT_SECRET,
                redirect_uri=config.SPOTIPY_REDIRECT_URI,
                scope="user-modify-playback-state user-read-playback-state"
            ))
            print("[Jetson Thor] Spotify Controller Initialized")
        except Exception as e:
            print(f"[Error] Spotify Initialization Failed: {e}")

    def play(self):
        try:
            self.sp.start_playback()
            print("Action: Play")
        except:
            pass

    def stop(self):
        try:
            self.sp.pause_playback()
            print("Action: Stop")
        except:
            pass

    def volume_up(self):
        try:
            current_vol = self.sp.current_playback()['device']['volume_percent']
            self.sp.volume(min(100, current_vol + 5))
            print(f"Action: Volume Up ({current_vol + 5}%)")
        except:
            pass

    def volume_down(self):
        try:
            current_vol = self.sp.current_playback()['device']['volume_percent']
            self.sp.volume(max(0, current_vol - 5))
            print(f"Action: Volume Down ({current_vol - 5}%)")
        except:
            pass
