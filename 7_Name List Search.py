
import tkinter as tk

names = []

# Add name
def add_name():
    name = name_entry.get().strip()

    if name == "":
        result.config(text="Please enter a name!")
        return

    names.append(name)
    name_listbox.insert(tk.END, name)
    name_entry.delete(0, tk.END)
    result.config(text="Name added successfully!")


# Search name
def search_name():
    search = search_entry.get().strip()

    if search == "":
        result.config(text="Please enter a name to search!")
        return

    for name in names:
        if name.lower() == search.lower():
            result.config(text="Name found!")
            return

    result.config(text="Name not found!")


# Clear search
def clear_search():
    search_entry.delete(0, tk.END)

    name_listbox.delete(0, tk.END)

    for name in names:
        name_listbox.insert(tk.END, name)

    result.config(text="Full list displayed!")


# Window
root = tk.Tk()
root.title("Name List Search")
root.geometry("350x350")

# Add name
name_label = tk.Label(root, text="Enter name:")
name_label.grid(row=0, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

add_button = tk.Button(root, text="Add Name", command=add_name)
add_button.grid(row=1, column=0, columnspan=2, pady=5)

# Listbox
name_listbox = tk.Listbox(root)
name_listbox.grid(row=2, column=0, columnspan=2, pady=5)

# Search
search_label = tk.Label(root, text="Search name:")
search_label.grid(row=3, column=0)

search_entry = tk.Entry(root)
search_entry.grid(row=3, column=1)

search_button = tk.Button(root, text="Search", command=search_name)
search_button.grid(row=4, column=0, pady=5)

clear_button = tk.Button(root, text="Clear Search", command=clear_search)
clear_button.grid(row=4, column=1)

# Result
result = tk.Label(root, text="")
result.grid(row=5, column=0, columnspan=2)

root.mainloop()
