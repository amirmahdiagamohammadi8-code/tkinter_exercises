
import tkinter as tk

remaining = 0
running = False

def start_timer():
    global remaining, running

    if running:
        return

    try:
        seconds = int(time_entry.get())

        if seconds <= 0:
            result.config(text="Enter a positive number!")
            return

        remaining = seconds
        running = True
        countdown()

    except ValueError:
        result.config(text="Enter a valid number!")


def countdown():
    global remaining, running

    if remaining > 0:
        result.config(text=f"Time left: {remaining} seconds")
        remaining -= 1
        root.after(1000, countdown)

    else:
        result.config(text="Break time is over!")
        running = False


# Window
root = tk.Tk()
root.title("Study Break Timer")
root.geometry("300x200")

# Label
title = tk.Label(root, text="Enter break time (seconds):")
title.grid(row=0, column=0, pady=10)

# Entry
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=0)

# Button
start_button = tk.Button(
    root,
    text="Start Timer",
    command=start_timer
)
start_button.grid(row=2, column=0, pady=10)

# Result
result = tk.Label(root, text="Ready!")
result.grid(row=3, column=0)

root.mainloop()
