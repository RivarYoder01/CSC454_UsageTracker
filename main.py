#!/usr/bin/env python3
"""
CPU Usage LED Simulator
"""

import psutil
import tkinter as tk

# CPU Usage LED Simulator
# Using psutil, simulate a CPU monitor that:
# • Lights up virtual LEDs (ASCII or GUI)
# • Color/brightness changes based on CPU %
# • Alert system if CPU > 90%

root = None
canvas = None
led = None


def find_cpu_usage():
    """

    :return: float
    """

    return psutil.cpu_percent(interval=0.1)


def display_led():
    """

    :return:
    """
    global root, canvas, led
    root = tk.Tk()
    root.title("CPU LED MONITOR")

    canvas = tk.Canvas(root, width=400, height=80)
    canvas.pack()

    led = canvas.create_oval(10, 10, 70, 70, fill="gray", outline="black", width=2)


def main():
    """
    """
    display_led()
    find_cpu_usage()
    root.mainloop()

if __name__ == "__main__":
    main()