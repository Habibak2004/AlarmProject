import time
import pygame
from tkinter import Tk, Label, Button, Entry, filedialog
import threading
import os


pygame.mixer.init()  # Initialize the pygame mixer

# Function to play the alarm sound
def play_alarm(sound_file):
    try:
        pygame.mixer.music.load(sound_file)  # Load the sound file
        pygame.mixer.music.play()  # Play the alarm sound

        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except pygame.error as e:
        error_message = f"Pygame error playing sound: {e}"
        print(error_message)
        status_label.config(text=f"Error: {error_message}")
    except Exception as e:
        error_message = f"General error playing sound: {e}"
        print(error_message)
        status_label.config(text=f"Error: {error_message}")

# Function to validate time format (HH:MM)
def is_valid_time(time_str):
    try:
        time.strptime(time_str, "%H:%M")  # Try to match the time format
        return True
    except ValueError:
        return False

# Function to set the alarm
def set_alarm():
    alarm_time = alarm_time_entry.get()
    sound_file = sound_file_entry.get()

    print(f"Current working directory: {os.getcwd()}")

    print(f"Attempting to load sound file from: {sound_file}")

    # Validate the time format
    if not is_valid_time(alarm_time):
        status_label.config(text="Error: Invalid time format! Use HH:MM.")
        return

    # Check if the sound file exists
    if not os.path.exists(sound_file):
        error_message = f"Error: Sound file not found at path: {sound_file}"
        print(error_message)
        status_label.config(text=error_message)
        return
    
    status_label.config(text=f"Alarm set for {alarm_time}")

    # Run the alarm check in a separate thread to avoid blocking the GUI
    alarm_thread = threading.Thread(target=check_alarm, args=(alarm_time, sound_file))
    alarm_thread.start()

# Function to check the current time and trigger the alarm
def check_alarm(alarm_time, sound_file):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm ringing!")
            play_alarm(sound_file)
            status_label.config(text="Alarm ringing!")
            break
        time.sleep(1)  # Check every second

# Function to open a file dialog for selecting the sound file
def browse_sound_file():
    file_path = filedialog.askopenfilename(
        title="Select Alarm Sound File",
        filetypes=[("Audio files", "*.mp3 *.wav")]  # You can add more file types
    )
    if file_path:
        sound_file_entry.delete(0, "end")
        sound_file_entry.insert(0, file_path)


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

# Button to browse for the sound file
browse_button = Button(root, text="Browse", command=browse_sound_file)
browse_button.pack()

# Label to display status messages
status_label = Label(root, text="Status: Not Set")
status_label.pack()

# Button to set the alarm
set_button = Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

# Start the GUI loop
root.mainloop()

