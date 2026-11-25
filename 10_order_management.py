
import tkinter as tk
from tkinter import messagebox

orders = []

# Add Order
def add_order():
    customer = name_entry.get().strip()
    order = order_entry.get().strip()

    if customer == "" or order == "":
        messagebox.showwarning("Error", "Please fill in all fields!")
        return

    orders.append((customer, order))

    order_listbox.insert(tk.END, f"{customer} - {order}")

    name_entry.delete(0, tk.END)
    order_entry.delete(0, tk.END)

    count_label.config(text=f"Total Orders: {len(orders)}")


# Show Order Details
def show_order():
    selected = order_listbox.curselection()

    if not selected:
        messagebox.showwarning("Error", "Please select an order!")
        return

    index = selected[0]
    customer, order = orders[index]

    messagebox.showinfo(
        "Order Details",
        f"Customer: {customer}\nOrder: {order}"
    )


# Delete Order
def delete_order():
    selected = order_listbox.curselection()

    if not selected:
        messagebox.showwarning("Error", "Please select an order!")
        return

    index = selected[0]

    order_listbox.delete(index)
    orders.pop(index)

    count_label.config(text=f"Total Orders: {len(orders)}")


# Window
root = tk.Tk()
root.title("Order Management System")
root.geometry("400x400")

# Customer Name
name_label = tk.Label(root, text="Customer Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Order Title
order_label = tk.Label(root, text="Order Title:")
order_label.grid(row=1, column=0, padx=5, pady=5)

order_entry = tk.Entry(root)
order_entry.grid(row=1, column=1)

# Add Button
add_button = tk.Button(
    root,
    text="Add Order",
    command=add_order
)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Listbox
order_listbox = tk.Listbox(root, width=40)
order_listbox.grid(row=3, column=0, columnspan=2, pady=10)

# Show Details Button
show_button = tk.Button(
    root,
    text="Show Details",
    command=show_order
)
show_button.grid(row=4, column=0, pady=5)

# Delete Button
delete_button = tk.Button(
    root,
    text="Delete Order",
    command=delete_order
)
delete_button.grid(row=4, column=1, pady=5)

# Count Label
count_label = tk.Label(root, text="Total Orders: 0")
count_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
