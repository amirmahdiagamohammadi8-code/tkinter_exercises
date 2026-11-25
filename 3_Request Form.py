
import tkinter as tk
from tkinter import messagebox

def form():
    if name_entry.get() == "":
        messagebox.showwarning("خطا", "نام را وارد کنید")
        return

    if darkhast_entry.get() == "":
        messagebox.showwarning("خطا", "موضوع درخواست را وارد کنید")
        return

    if moshkel_text.get("1.0", tk.END).strip() == "":
        messagebox.showwarning("خطا", "شرح مشکل را وارد کنید")
        return

    messagebox.showinfo(
        "خلاصه درخواست",
        f"نام: {name_entry.get()}\n"
        f"موضوع: {darkhast_entry.get()}\n"
        f"شرح مشکل: {moshkel_text.get('1.0', tk.END).strip()}"
    )

root = tk.Tk()
root.title("ثبت درخواست")

name_label = tk.Label(root, text="name:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

darkhast_label = tk.Label(root, text="darkhast:")
darkhast_label.grid(row=1, column=0)

darkhast_entry = tk.Entry(root)
darkhast_entry.grid(row=1, column=1)

moshkel_label = tk.Label(root, text="moshkel:")
moshkel_label.grid(row=2, column=0)

moshkel_text = tk.Text(root, height=5, width=25)
moshkel_text.grid(row=2, column=1)

btn_sabt = tk.Button(root, text="sabt", command=form)
btn_sabt.grid(row=4, column=1)

root.mainloop()
