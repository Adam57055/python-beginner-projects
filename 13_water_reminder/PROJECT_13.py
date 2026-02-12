# project 13 is a drink water reminder app that reminds the user to drink water at regular intervals
# the app will use plyer module to play a sound as a reminder
# the user can set the interval time in minutes
import time
from plyer import notification

def water_reminder(interval_minutes):
    if interval_minutes <= 0:
        print("Interval must be greater than 0 minutes.")
        return

    interval_seconds = interval_minutes * 60  # convert minutes to seconds

    print(f"Water reminder started. You'll be notified every {interval_minutes} minutes.")
    print("Press Ctrl + C to stop.")

    try:
        while True:
            time.sleep(interval_seconds)
            notification.notify(
                title="Drink Water Reminder",
                message="It's time to drink water! Stay hydrated Girl!",
                app_name="Water Reminder",
                timeout=10
            )
    except KeyboardInterrupt:
        print("\nWater reminder stopped. Stay healthy!")

# ---- main program ----
try:
    interval_minutes = int(input("Enter the interval time in minutes for water reminders: "))
    water_reminder(interval_minutes)
except ValueError:
    print("Please enter a valid integer value.")







   