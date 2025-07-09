#!/usr/bin/env python3
"""
CPU Usage LED Simulator
"""

import psutil
import time

# CPU Usage LED Simulator
# Using psutil, simulate a CPU monitor that:
# • Lights up virtual LEDs (ASCII or GUI)
# • Color/brightness changes based on CPU %
# • Alert system if CPU > 90%


def main():
    """
    """
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"Current CPU usage: {cpu_percent}%")
        time.sleep(1)  # Wait for 1 second before checking again

if __name__ == "__main__":
    main()