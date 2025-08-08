"""
create a simple soundbar with tkinter

objective:
-create a class called Soundbar to handle the graphical interface of the soundbar
- create a soundbar with tkinter

    -create a frame with a simple button called play, stop, pause for music using the SoundPlayer class 
    -create a frame with a simple button called play for ambient sound
    -divide the soundbar in two frames, one for music and one for ambient sound
    -create a volume control for music and ambient sound
-create the frame for the soundbar using the class
"""
import os 
import tkinter as tk
from sound_code import SoundPlayer


class Soundbar:
    """a class to handle the soundbar interface using Tkinter"""
    def __init__(self):
        """"Initialize the soundbar, get elements from the sound files, instantiate SoundPlayer, 
        create the main window."""
        self.elements_sound = os.listdir('./instant_sound')
        self.elements_music = os.listdir('./ambience_music')
        self.elements_music_test = os.listdir('./sound_test')
        self.position = 0 
        self.s = SoundPlayer()

        """Create the main window for the soundbar."""
        root = tk.Tk()
        root.title("Soundbar music")
        root.geometry("800x600")
        self.create_buttons_music()
        self.create_buttons_ambient()
        root.mainloop()

    def add_dinamic_string(self,string):
        """Insert a label as a divider in the grid."""
        divider = tk.Label(text=str(string))
        self.position =+ 1
        row = self.position 
        divider.grid(row=row, column=0, columnspan=4, pady=10)
        return divider
    
    def add_static_string(self, string):
        """Add a static label to the grid at the next available row."""
        label = tk.Label(text=string)
        self.position += 1
        label.grid(row=self.position, column=0, columnspan=4, pady=10)
        return label
    
    def create_button(self,name, function, grid_pos):
        """
        Create a button with the given name and function, and place 
        it in the grid at the specified position.
        """
        button = tk.Button(text=name, command=function)
        col, row  = grid_pos
        button.grid(row=row, column=col, padx=5, pady=5)      
        return button
    
    def create_buttons_music(self):
        """Create the buttons play, pause, resume, stop for every file in the music directory"""
        self.add_static_string("----MUSIC----")
        for x in self.elements_music:
            self.position += 1
            self.create_button(f"Play {x}",  lambda x=x: self.s.play_music(x),(0, self.position))            
            self.create_button(f"Pause {x}", lambda: self.s.pause_music(),(1, self.position))
            self.create_button(f"Resume {x}", lambda: self.s.resume_music(),(2, self.position))
            self.create_button(f"Stop {x}", lambda: self.s.stop_music(),(3, self.position))
                       

    def create_buttons_ambient(self):
        """Create the buttons play for every file in the ambient sound directory""" 
        self.add_static_string("----AMBIENT SOUND----")
        for x in self.elements_sound:
            self.position += 1
            self.create_button(f"Play {x}", lambda x=x: self.s.play_ambient(x),(0, self.position))
            
if __name__ == "__main__":
    """Run the soundbar if this file is run directly."""
    Soundbar()
