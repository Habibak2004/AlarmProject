import time
import pygame
from datetime import datetime

# Function to play the alarm sound
def play_alarm(sound_file):
    pygame.mixer.init()  # Initialize the pygame mixer
    pygame.mixer.music.load(sound_file)  # Load the sound file
    pygame.mixer.music.play()  # Play the alarm sound

    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Wait while the sound is playing

# Function to set an alarm
def set_alarm():
    alarm_time = input("Enter the time for the alarm (HH:MM): ")
    sound_file = input("Enter the path to the alarm sound file (e.g., 'alarm_sound.wav'): ")

    # Run the alarm check continuously
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:  # Check if current time matches the alarm time
            print("Alarm ringing!")
            play_alarm(sound_file)  # Play the sound when the time matches
            break
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    set_alarm()
