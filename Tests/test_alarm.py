import unittest
from unittest.mock import patch
from src.alarm import play_alarm
import pygame

class TestAlarmSystem(unittest.TestCase):
    @patch('pygame.mixer.music.play')
    def test_alarm_playback(self, mock_play):
        sound_file = "alarm_sound.wav"
        play_alarm(sound_file)
        mock_play.assert_called_once()

if __name__ == '__main__':
    unittest.main()
