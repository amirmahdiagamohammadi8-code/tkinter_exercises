
import tkinter as tk

def calculate():
    try:
        food_price = float(food_entry.get())
        drink_price = float(drink_entry.get())
        snack_price = float(snack_entry.get())
        tax_percent = float(darsad.get())

        if food_price < 0 or drink_price < 0 or snack_price < 0 or tax_percent < 0:
            result_label.config(text="مقادیر نباید منفی باشند")
            return

        total = food_price + drink_price + snack_price

        totall = total * tax_percent / 100

        tax = total + totall

        result_label.config(
            text=f"جمع اولیه: {total:.2f}\nمبلغ مالیات: {totall:.2f}\nمبلغ نهایی: {tax:.2f}"
        )

    except ValueError:
        result_label.config(text="لطفا تمام ورودی ها را عددی وارد کنید")


window = tk.Tk()
window.title("محاسبه هزینه غذا")
window.geometry("200x200")
window.configure(bg="darkblue")

label = tk.Label(window, text="Food Calculator")
label.grid(row=0, column=1)

food_entry = tk.Entry(window)
drink_entry = tk.Entry(window)
snack_entry = tk.Entry(window)
darsad = tk.Entry(window)

food_entry.grid(row=2, column=1)
drink_entry.grid(row=3, column=1)
snack_entry.grid(row=4, column=1)
darsad.grid(row=5, column=1)

food_label = tk.Label(window, text="Food")
food_label.grid(row=2, column=0)

drink_label = tk.Label(window, text="Drink")
drink_label.grid(row=3, column=0)

snack_label = tk.Label(window, text="Snack")
snack_label.grid(row=4, column=0)

darsad_label = tk.Label(window, text="Tax Percent")
darsad_label.grid(row=5, column=0)

button = tk.Button(
    window,
    text="محاسبه",
    command=calculate
)

button.grid(row=6, column=1)

result_label = tk.Label(window, text="", bg="darkblue", fg="white")
result_label.grid(row=7, column=1)

window.mainloop()
