from sound_code import SoundPlayer
import pygame
import unittest

class TestSoundPlayer(unittest.TestCase):
    """unit tests for the SoundPlayer class"""
    def setUp(self):
        """Set up the SoundPlayer with test files."""
        self.player = SoundPlayer()
        self.test_file='test.wav'

    def test_play_music(self):
        """Test playing music."""
        self.player.play_music(self.test_file)
        self.assertTrue(self.player.is_music_playing)

    def test_pause_music(self):
        """Test pausing music."""
        self.player.play_music(self.test_file)
        self.player.pause_music()
        self.assertFalse(self.player.is_music_playing)

    def test_stop_music(self):
        """Test stopping music."""
        self.player.play_music(self.test_file)
        self.player.stop_music()
        self.assertFalse(self.player.is_music_playing)

    def test_play_ambient(self):
        """Test playing ambient sound."""
        self.player.play_ambient(self.test_file)
        self.assertTrue(pygame.mixer.get_busy())
    
    def test_set_volume_music(self):
        """test setting volume for music playback."""
        new_volume = 0.5
        self.player.set_volume_music(new_volume)
        self.assertEqual(pygame.mixer.music.get_volume(), new_volume)
    
    def test_set_volume_sound(self):
        """Test setting volume for ambient sound.""" 
        new_volume = 0.5
        self.player.set_volume_sound(new_volume, self.test_file)

        self.assertEqual(self.player.volume_ambience, new_volume)

