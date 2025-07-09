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
alert_label = None


def display_led():
    """

    :return:
    """
    global root, canvas, led, alert_label
    root = tk.Tk()
    root.title("CPU LED MONITOR")

    canvas_width = 400
    canvas_height = 80
    led_diameter = 60

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    x0 = (canvas_width - led_diameter) // 2
    y0 = (canvas_height - led_diameter) // 2
    x1 = x0 + led_diameter
    y1 = y0 + led_diameter

    led = canvas.create_oval(x0, y0, x1, y1, fill="gray", outline="black", width=2)

    alert_label = tk.Label(root, text="CPU Usage: ", font=("Arial", 16))
    alert_label.pack(pady=10)

    button = tk.Button(root, text="Exit", command=root.quit)
    button.pack(pady=10)

def alert_system(usage):
    """

    :return:
    """
    if usage > 90:
        alert_label.config(text=f"CPU Usage: {usage}%", fg="red")
    else:
        alert_label.config(text=f"CPU Usage: {usage}%", fg="black")

    return


def update_led():
    try:
        usage = psutil.cpu_percent(interval=1)
    except Exception as e:
        usage = 0
        print(f"Error retrieving CPU usage: {e}")
        root.quit()
    else:
        print(usage)

    if usage < 50:
        color = "green"
    elif usage < 80:
        color = "yellow"
    else:
        color = "red"

    canvas.itemconfig(led, fill=color)
    alert_system(usage)
    root.after(1000, update_led)  # Update every second


def main():
    """
    """
    display_led()
    update_led()
    root.mainloop()

if __name__ == "__main__":
    main()