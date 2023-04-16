# Importing the libraries
import os
import subprocess
import tkinter as tk
import time
from tkinter import filedialog

# Creating a Tkinter window
root = tk.Tk()
root.withdraw()

# Gives the possibility to choose a video file
file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])

# Paths to ffmpeg and ffplay, as well as playing the video
if file_path:
    ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg.exe")
    ffplay_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffplay.exe")

    command = f"{ffplay_path} {file_path} -window_title \"Barebones Video Player\" -autoexit -stats"
    ffplay_process = subprocess.Popen(command, shell=True)

    time.sleep(3)
    ffplay_process.wait()
    
# Honestly this was my first time using ffmpeg and ffplay in Python, so I'm not sure if this is the best way to do it, but it works, somehow. I'm not even going to question it.