"""
this is the code of the project:
objective:

    -play a specific sound
    -separate the music from the ambient sound (they will have 
    different roles and they will not interfere with each other):
        ambient sound is played with the SOUND module and every sound is unique
        music is played with the MUSIC module
    -the music is played in the background and loops
    -the ambient sound is played in the foreground and stops after a cicle
    -create commands for the soundbar to control the volume and play/pause the music
        
"""
import pygame


class SoundPlayer:
    """a class to handle sound playback using Pygame"""
    def __init__(self):
        """
        Initialize the sound player with music and ambient sound files.
        Args:
        """
        pygame.mixer.init()
        self.music_file = './ambience_music/'
        self.ambient_file = './instant_sound/'
        self.is_music_playing = False
        self.volume_ambience= 1.0

    def play_music(self, name_music):
        """

        it plays the background music using the MUSIC module.

        Play the music , looping indefinitely.
        If self.is.music_playing is True, it will not reload.
        """
        if not self.is_music_playing:
            music_path = f"{self.music_file}/{name_music}"
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play(-1)  # Loop indefinitely
            self.is_music_playing = True

    def pause_music(self):
        """
        Pause the currently playing music.
        If self.is.music_playing is True, it will pause the music.
        """
        if self.is_music_playing:
            pygame.mixer.music.pause()
            self.is_music_playing = False

    def stop_music(self):
        """
        Stop the currently playing music.
        If self.is.music_playing is True, it will stop the music.
        """
        if self.is_music_playing:
            pygame.mixer.music.stop()
            self.is_music_playing = False

    def play_ambient(self, name_sound):
        """Play the ambient sound once using the SOUND module.
        If self.is.ambient_playing is True, it will not reload.
        """
        channel = pygame.mixer.find_channel()
        sound_path = f"{self.ambient_file}/{name_sound}"
        ambient_sound = pygame.mixer.Sound(sound_path)
        channel.play(ambient_sound)

    def set_volume_music(self, new_volume):
        """
        Set the volume for music playback.
            volume (float): Volume level between 0.0 and 1.0.
        """
        pygame.mixer.music.set_volume(new_volume)

    def set_volume_sound(self, new_volume, name_sound):
        """
        Set the volume for both ambient sound:
            volume (float): Volume level between 0.0 and 1.0.
        """
        self.volume_ambience = new_volume
        sound_path = f"{self.ambient_file}/{name_sound}"
        the_sound = pygame.mixer.Sound(sound_path)
        the_sound.set_volume(new_volume)



