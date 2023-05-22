import tkinter as tk
from tkinter import messagebox
import pyttsx3
import threading
import random
from pystray import MenuItem as item
import pystray
from PIL import Image

# List of creative reminder messages
reminder_messages = [
    "Time to drink water! Stay hydrated and healthy!",
    "Don't forget to take a water break! Your body will thank you.",
    "Hydration is key! Grab a glass of water and reenergize yourself.",
    "A gentle reminder to drink some water. Your health is worth it!",
    "Stay refreshed and drink some water. It's good for your mind and body.",
    "Remember to hydrate like a boss!",
    "Stay cool and stay hydrated. Drink some water!",
    "Water is your best friend. Have a sip now!",
    "It's time to quench your thirst. Drink some water!",
    "Keep calm and stay hydrated. Drink water regularly.",
    "Stay on top of your hydration game. Take a water break!",
    "Water is the elixir of life. Take a moment to hydrate.",
    "Stay hydrated and slay the day!",
    "Drink water and be awesome!",
    "Water, the secret of your energy. Stay hydrated!",
    "Remember, water is your body's natural fuel. Drink up!",
    "Stay hydrated, stay focused!",
    "Don't forget to refill your water tank!",
    "Stay hydrated like a pro!",
    "Water is the key to your vitality. Stay hydrated and shine!",
]

# Function to speak the reminder message
def speak_reminder():
    engine = pyttsx3.init()
    message = random.choice(reminder_messages)  # Randomly select a message
    engine.say(message)
    engine.runAndWait()

# Function to start or stop the reminders
def toggle_reminders():
    if start_button["text"] == "Start":
        interval = int(entry.get())  # Get the interval value from the entry field

        # Validate the interval value
        if interval <= 0:
            messagebox.showerror("Error", "Please enter a valid time interval.")
            return

        # Function to display the reminder and start a new timer
        def display_reminder():
            speak_reminder()
            if start_button["text"] == "Stop":
                threading.Timer(interval * 60, display_reminder).start()

        display_reminder()  # Start the first reminder
        start_button["text"] = "Stop"  # Change the button text to "Stop"
    else:
        start_button["text"] = "Start"  # Change the button text back to "Start"

# Function to minimize the program to the system tray
def minimize_to_tray():
    root.iconify()  # Minimize the main window
    menu = (item('Open', lambda: root.deiconify()),
            item('Exit', lambda: exit_program()))
    image = Image.open("icon.png")  # Replace "icon.png" with the path to your desired icon image
    image = image.resize((16, 16))  # Resize the icon image
    menu_icon = pystray.Icon("HydroBot", image, "HydroBot", menu)
    menu_icon.run()

# Function to exit the program
def exit_program():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Water Drinking Reminder")

# Create a label and entry field for time interval
interval_label = tk.Label(root, text="Enter the time interval (in minutes):")
interval_label.pack(padx=20, pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Create a button to start or stop the reminders
start_button = tk.Button(root, text="Start", command=toggle_reminders)
start_button.pack(pady=5)

# Create a button to minimize to tray
minimize_button = tk.Button(root, text="Minimize", command=minimize_to_tray)
minimize_button.pack(pady=5)

# Start the main event loop
root.mainloop()
