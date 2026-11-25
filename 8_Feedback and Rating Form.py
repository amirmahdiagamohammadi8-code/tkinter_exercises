
import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = name_entry.get().strip()
    rating = rating_var.get()
    feedback = feedback_text.get("1.0", tk.END).strip()

    if name == "":
        messagebox.showwarning("Error", "Please enter your name!")
        return

    if rating == 0:
        messagebox.showwarning("Error", "Please select a rating!")
        return

    if feedback == "":
        messagebox.showwarning("Error", "Please enter your feedback!")
        return

    messagebox.showinfo(
        "Feedback Summary",
        f"Name: {name}\n"
        f"Rating: {rating}/5\n"
        f"Feedback: {feedback}"
    )


# Window
root = tk.Tk()
root.title("Feedback and Rating Form")
root.geometry("350x400")

# Name
name_label = tk.Label(root, text="Your Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Rating
rating_label = tk.Label(root, text="Select Rating:")
rating_label.grid(row=1, column=0, pady=5)

rating_var = tk.IntVar(value=0)

for i in range(1, 6):
    tk.Radiobutton(
        root,
        text=str(i),
        variable=rating_var,
        value=i
    ).grid(row=1, column=i)

# Feedback
feedback_label = tk.Label(root, text="Your Feedback:")
feedback_label.grid(row=2, column=0, pady=5)

feedback_text = tk.Text(root, width=30, height=5)
feedback_text.grid(row=3, column=0, columnspan=5)

# Submit Button
submit_button = tk.Button(
    root,
    text="Submit Feedback",
    command=submit_feedback
)
submit_button.grid(row=4, column=0, columnspan=5, pady=15)

root.mainloop()
