import psutil
import time

while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"Current CPU usage: {cpu_percent}%")
    time.sleep(1)  # Wait for 1 second before checking again