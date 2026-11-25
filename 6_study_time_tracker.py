
import tkinter as tk

def calculate():
    try:
        minutes = int(time_entry.get())

        if minutes < 0:
            result.config(text="Time cannot be negative!")
            return

        total_minutes = minutes

        hours = total_minutes // 60
        remaining_minutes = total_minutes % 60

        result.config(
            text=f"Total study time: {hours} hours and {remaining_minutes} minutes"
        )

        if total_minutes >= 120:
            message.config(text="Great job! Excellent study time!")
        elif total_minutes > 0:
            message.config(text="Good job! Keep going!")
        else:
            message.config(text="No study time recorded.")

    except ValueError:
        result.config(text="Please enter a valid number!")
        message.config(text="")


# Window
root = tk.Tk()
root.title("Study Time Tracker")
root.geometry("400x250")

# Label
title_label = tk.Label(root, text="Study time (minutes):")
title_label.grid(row=0, column=0, padx=10, pady=10)

# Entry
time_entry = tk.Entry(root)
time_entry.grid(row=0, column=1)

# Button
calculate_button = tk.Button(
    root,
    text="Calculate",
    command=calculate
)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Result
result = tk.Label(root, text="")
result.grid(row=2, column=0, columnspan=2)

message = tk.Label(root, text="")
message.grid(row=3, column=0, columnspan=2)

root.mainloop()
