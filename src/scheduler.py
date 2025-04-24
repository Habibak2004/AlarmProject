import time
from datetime import datetime

def schedule_alarm(alarm_time):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            return True
        time.sleep(30)  # Check every 30 seconds
