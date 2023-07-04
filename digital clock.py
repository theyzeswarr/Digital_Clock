import tkinter as tk
import time

# Function to update the clock display
def update_clock():
    current_time = time.strftime('%H:%M:%S')  # Get the current time
    clock_label.config(text=current_time)  # Update the label text
    clock_label.after(1000, update_clock)  # Schedule the next update after 1 second

# Create the main window
window = tk.Tk()
window.title("Digital Clock")

# Create the clock label
clock_label = tk.Label(window, font=("Arial", 80), bg="black", fg="white")
clock_label.pack(padx=50, pady=50)

# Start the clock update
update_clock()

# Start the main event loop
window.mainloop()
