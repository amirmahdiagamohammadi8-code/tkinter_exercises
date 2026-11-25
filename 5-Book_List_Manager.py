import tkinter as tk

#تابع
def add_book():
    book=book_entry.get().strip()

    if book == "":
        return

    book_listbox.insert(tk.END,book)
    book_entry.delete(0,tk.END)

#تابع حذف کتاب
def delete_book():
    selected = book_listbox.curselection()
    if selected:
        book_listbox.delete(selected[0])


#پنجره
root=tk.Tk()
root.title("Book List Manager")

#اینتری ها 

book_entry =tk.Entry(root)
book_entry.grid(row=0,column=0)

#لیتباکس

book_listbox =tk.Listbox(root)
book_listbox.grid(row=1,column=0)

#باتن

add_book_Button =tk.Button(root,text="Add Book",command=add_book)
add_book_Button.grid(row=0,column=1)

delete_book_Button = tk.Button(root,text="Delete Book", command=delete_book)
delete_book_Button.grid(row=2,column=0)



root.mainloop()