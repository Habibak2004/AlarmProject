import time
import pygame
from tkinter import Tk, Label, Button, Entry

# Function to play the alarm sound
def play_alarm(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Function to set an alarm
def set_alarm():
    alarm_time = alarm_time_entry.get()
    sound_file = sound_file_entry.get()

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm ringing!")
            play_alarm(sound_file)
            break
        time.sleep(30)  # Check every 30 seconds

# Setting up the GUI window
root = Tk()
root.title("Custom Alarm")

# Label and input field for alarm time
Label(root, text="Enter Alarm Time (HH:MM):").pack()
alarm_time_entry = Entry(root)
alarm_time_entry.pack()

# Label and input field for sound file path
Label(root, text="Enter the path to the sound file:").pack()
sound_file_entry = Entry(root)
sound_file_entry.pack()

# Button to set the alarm
Button(root, text="Set Alarm", command=set_alarm).pack()

# Start the GUI loop
root.mainloop()
