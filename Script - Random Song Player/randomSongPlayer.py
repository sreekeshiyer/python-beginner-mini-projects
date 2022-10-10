import random, os
from tkinter import filedialog

music_dir = filedialog.askdirectory(title = "Select directory to play song from")  # Select directory to play song from
songs = os.listdir(music_dir)           # Make a list of all available files in selected directory
song = random.randint(0,len(songs))     # Generate a random index to play random song
print(f"Now playing {songs[song]}...")  # Prints The Song Name
os.startfile(os.path.join(music_dir, songs[song]))  # Play song