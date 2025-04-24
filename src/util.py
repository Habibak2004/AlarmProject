import os

# Helper function to check if the sound file exists
def is_valid_sound_file(file_path):
    return os.path.isfile(file_path) and file_path.endswith(('.mp3', '.wav'))

# Helper function to format time into 24-hour format (HH:MM)
def format_time(time_str):
    try:
        return time.strftime("%H:%M", time.strptime(time_str, "%I:%M %p"))
    except ValueError:
        return None
