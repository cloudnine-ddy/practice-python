from plyer import notification
import sys
import time

if sys.stdout != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

print("Sending notification......")

notification.notify(
    title = "Reminder",
    message = "Time to drink some water!",
    app_name = "Python Notifier",
    timeout = 1
)
time.sleep(1)

print("Notification Sent")