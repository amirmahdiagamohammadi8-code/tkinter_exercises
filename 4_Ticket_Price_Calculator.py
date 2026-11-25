import tkinter as tk

def calculater():
    try:
        type_entry = entry_type.get()
        count_entry =int(entry_count.get())
        price_ticket=int(entry_price.get())
    except ValueError:
        total.config(text="Enter valid numbers!")
        return
    total_price = count_entry * price_ticket
    
    total.config(text=f"Total price: {total_price}")
    
root=tk.Tk()
root.title("Ticket Price Calculator")

# لیبل ها
 
label_type =tk.Label(root,text="ticket type :")
label_type.grid(row=0,column=0)

label_count =tk.Label(root,text="ticket count :")
label_count.grid(row=1,column=0)

label_price =tk.Label(root,text="ticket price :")
label_price.grid(row=2,column=0)

#اینتری ها

entry_type=tk.Entry(root)
entry_type.grid(row=0,column=1)

entry_count=tk.Entry(root)
entry_count.grid(row=1,column=1)

entry_price=tk.Entry(root)
entry_price.grid(row=2,column=1)

#دکمه محاسبه

button_caculate=tk.Button(root,text=" Calculate ",command=calculater)
button_caculate.grid(row=4,column=1)


total=tk.Label(root,text="")
total.grid(row=5,column=1)

root.mainloop()
