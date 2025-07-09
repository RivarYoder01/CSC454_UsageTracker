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



def update_led():
    usage = psutil.cpu_percent(interval=1)
    print(usage)

    if usage < 50:
        color = "green"
    elif usage < 80:
        color = "yellow"
    else:
        color = "red"

    canvas.itemconfig(led, fill=color)
    root.after(1000, update_led)  # Update every second


def main():
    """
    """
    display_led()
    update_led()
    root.mainloop()

if __name__ == "__main__":
    main()