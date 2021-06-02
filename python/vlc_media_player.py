import pafy
import vlc
import time
from enum import IntEnum, auto

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s]: %(asctime)s:%(module)s:%(message)s")

# Use
class Action(IntEnum):
    PLAY = 1
    PAUSE = 2
    STOP = 3
    MUTE = 4
    VOL_UP = 5
    VOL_DN = 6


class VLCMediaPlayer:
    """VLC Media Player
    Play a video with VLC, from a YouTube url

    Actions :
    Play
    Stop
    Pause
    Mute
    Volume Up
    Volume Down
    """

    def __init__(self, url="https://www.youtube.com/watch?v=xtp4msMYi9s", mode=None):
        self.url = url
        video = pafy.new(self.url).getbest()
        if str(mode).lower() == "terminal":
            self._player = vlc.MediaPlayer(video.url)
            instance = vlc.Instance("prefer-insecure")
        else:
            instance = vlc.Instance("--loop")
            # instance = vlc.Instance("prefer-insecure")
            self._player = instance.media_player_new()
            media = instance.media_new(video.url)
            media.get_mrl()
            self._player.set_media(media)

    # STATES
    def get_state(self):
        return self._player.get_state()

    def is_paused(self):
        return self.get_state() == vlc.State.Paused

    def is_stopped(self):
        return self.get_state() == vlc.State.Stopped

    def is_playing(self):
        return self._player.is_playing()

    # ACTIONS (PLAYBACK)
    def play(self):
        logging.debug("Playing")
        self._player.play()

    def pause(self):
        logging.debug("Paused")
        self._player.pause()

    def stop(self):
        logging.debug("Stopped")
        self._player.stop()

    def mute(self):
        logging.debug(f"Muted : {self._player.audio_get_mute()}")
        self._player.audio_toggle_mute()

    def next_frame(self):
        self._player.next_frame()

    # ACTIONS (VOLUME)
    def get_volume(self):
        return self._player.audio_get_volume()

    def set_volume(self, val):
        if val < 0:
            logging.info("Minimal volume was reached")
        elif val > 100:
            logging.info("Maximal volume was reached")
        else:
            self._player.audio_set_volume(val)

    def volume_up(self, offset=20):
        logging.debug("Increased volume")
        self.set_volume(self.get_volume() + offset)

    def volume_dn(self, offset=20):
        logging.debug("Decreased volume")
        self.set_volume(self.get_volume() - offset)


class VLCController:
    """VLC Controller
    Control a VLC Media Player
    """

    def __init__(self, url="https://www.youtube.com/watch?v=xtp4msMYi9s", DELAY=1):
        self.media_player = VLCMediaPlayer(url)
        self.media_player.play()

    def test_run(self):
        self.media_player.play()
        time.sleep(5)
        self.media_player.pause()
        time.sleep(3)

    def is_playing(self):
        return self.media_player.is_playing()

    def test_sequence(self, sequence):
        """Control VLC Media Player accordingly to sequence"""
        action_options = {
            Action.PLAY: self.media_player.play,
            Action.PAUSE: self.media_player.pause,
            Action.STOP: self.media_player.stop,
            Action.MUTE: self.media_player.mute,
            Action.VOL_UP: self.media_player.volume_up,
            Action.VOL_DN: self.media_player.volume_dn,
        }
        for sequence_action in sequence:
            action_options[sequence_action]()
            time.sleep(1)


if __name__ == "__main__":

    control = VLCController()
    control.test_sequence((Action.PLAY, Action.PAUSE, Action.VOL_UP, Action.VOL_UP, Action.MUTE, Action.PAUSE))
    while True:
        control.test_run()
