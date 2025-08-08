import unittest
import tkinter as tk
import soundbar


class TestSoundbar(unittest.TestCase):
    """Unit tests for the Soundbar class."""
    
    def setUp(self):
        """Set up the Soundbar instance for testing."""
        self.soundbar = soundbar.Soundbar()
        self.root = tk.Tk()
        self.root.withdraw()  # Hide the main window during tests

    def test_create_button(self):
        """Test creating a button in the soundbar."""
        button = self.soundbar.create_button("Test", lambda: None, (0, 0))
        self.assertIsInstance(button, tk.Button)
        self.assertEqual(button['text'], "Test")

    def test_create_buttons_music(self):
        """Test creating music control buttons."""
        self.soundbar.create_buttons_music()
        # Check if buttons are created for each music file
        self.assertGreater(len(self.soundbar.elements_music), 0)  