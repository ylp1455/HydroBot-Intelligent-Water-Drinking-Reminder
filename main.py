import tkinter as tk
import pyttsx3
import threading
import random

# List of creative reminder messages
reminder_messages = [
    "Time to drink water! Stay hydrated and healthy!",
    "Don't forget to take a water break! Your body will thank you.",
    "Hydration is key! Grab a glass of water and reenergize yourself.",
    "A gentle reminder to drink some water. Your health is worth it!",
    "Stay refreshed and drink some water. It's good for your mind and body.",
]

# Function to speak the reminder message
def speak_reminder():
    engine = pyttsx3.init()
    message = random.choice(reminder_messages)  # Randomly select a message
    engine.say(message)
    engine.runAndWait()

# Function to schedule the reminders
def schedule_reminders():
    interval = int(entry.get())  # Get the interval value from the entry field

    # Validate the interval value
    if interval <= 0:
        messagebox.showerror("Error", "Please enter a valid time interval.")
        return

    # Function to display the reminder and start a new timer
    def display_reminder():
        speak_reminder()
        threading.Timer(interval * 60, display_reminder).start()

    display_reminder()  # Start the first reminder

# Create the main window
root = tk.Tk()
root.title("Water Drinking Reminder")

# Create a label
label = tk.Label(root, text="Enter the time interval (in minutes):")
label.pack(padx=20, pady=20)

# Create an entry field
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to start the reminders
start_button = tk.Button(root, text="Start Reminder", command=schedule_reminders)
start_button.pack(pady=10)

# Start the main event loop
root.mainloop()
