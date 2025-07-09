#!/usr/bin/env python3

"""
CPU Usage LED Simulator
CSC 454 | Tech Platforms Summer 2025 FINAL PROJECT

REQUIREMENTS AS LISTED IN PROJECT DESCRIPTION:
Using psutil, simulate a CPU monitor that:
 • Lights up virtual LEDs (ASCII or GUI)
 • Color/brightness changes based on CPU %
 • Alert system if CPU > 90%
"""

__author__ = 'Rivar Yoder'
__version__ = '1.0'
__date__ = '2025.07.06'
__status__ = 'Development'

import psutil # tracks CPU usage
import tkinter as tk # GUI library for Python

# Global variables for tkinter
root = None
canvas = None
led = None
alert_label = None


def display_led():
    """
    Draws canvas and displays:
        'LED' that toggles between green, yellow, and red based on CPU usage.
        Labels that display the usage percentage.
        Button to exit the application

    :return:
    """
    global root, canvas, led, alert_label # Initialize global variables
    root = tk.Tk() # Create the main window
    root.title("CPU LED MONITOR")

    # Set the dimensions of the canvas and LED to be used for display and centering LED
    canvas_width = 400
    canvas_height = 80
    led_diameter = 60

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height) # Create a canvas
    canvas.pack()

    # sets variables that centers LED
    x0 = (canvas_width - led_diameter) // 2
    y0 = (canvas_height - led_diameter) // 2
    x1 = x0 + led_diameter
    y1 = y0 + led_diameter

    # Draws the LED as a circle on the canvas
    led = canvas.create_oval(x0, y0, x1, y1, fill="gray", outline="black", width=2)

    alert_label = tk.Label(root, font=("Arial", 12)) # text for alerts
    alert_label.pack(pady=10)

    button = tk.Button(root, text="Exit", command=root.quit) # Exit button
    button.pack(pady=10)

def alert_system(usage):
    """
    Based on CPU usage, alert lable is updated with different messages.
    Based on usage of:
        < 50%
        51% - 79%
        80% - 89%
        > 90%

    If the usage is above 90%, the text color changes to red.

    :param usage: CPU usage percentage
    :return:
    """
    if usage < 50:
        alert_label.config(text=f"Everything is calm ^.^ CPU Usage: {usage}%", fg="black")
    elif usage < 80:
        alert_label.config(text=f"Things are picking up ._. CPU Usage: {usage}%", fg="black")
    elif usage < 90:
        alert_label.config(text=f"Your processor is toasty >.< CPU Usage: {usage}%", fg="black")
    else:
        alert_label.config(text=f"HIGH USAGE .0. CPU Usage: {usage}%", fg="red")

    return


def update_led():
    """
    Try-Except that checks the CPU usage. If psutil fails the program ends. Prints the usage percentage to the console.
    Retrieves the current CPU usage and updated LED color based on psutil.
    Passes usage to alert_system function to update the alert label.
    Usage is updated every second.

    :return:
    """
    try: # Check CPU usage
        usage = psutil.cpu_percent(interval=1)
    except Exception as e: # If psutil fails
        usage = 0 # Defaults to 0
        print(f"Error retrieving CPU usage: {e}") # Print error to CONSOLE, not GUI
        root.quit()
    else:
        print(usage) # Print usage to CONSOLE, not GUI

    if usage < 50:
        color = "green"
    elif usage < 80:
        color = "yellow"
    else:
        color = "red"

    canvas.itemconfig(led, fill=color) # Change LED color
    alert_system(usage) # Update alert
    root.after(1000, update_led)  # Update every second


def main():
    """
    Runs display_led to set up window
    Runs update_led to start monitor CPU usage and update LED color
    Loops
    """
    display_led()
    update_led()
    root.mainloop()

if __name__ == "__main__":
    main()