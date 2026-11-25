import tkinter as tk

def clear():
    pasw.delete(0, tk.END)
    result.config(text="نتیجه بررسی")
    
def pas():
    
    password = str(pasw.get())
    count = len(password)

    if count >= 8 :
        has_letter = False
        for i in password:
            if i.isalpha():
                has_letter = True
        has_number = False
        for i in password:
            if i.isdigit() :
                has_number = True
        if has_letter == True and has_number == True:
           result.config(text="رمز عبور معتبر است  ")

        else :
            result.config(text="رمز عبور باید شامل حداقل یک حرف و عدد باشد")
    else :
          result.config(text="رمز عبور حداقل باید 8 کاراکتر باشد")

root = tk.Tk()
root.title("Password Checker")

pasw = tk.Entry(root)
pasw.grid(row=0,column=0)


btn = tk.Button(root,text="بررسی رمز ورود ",command=pas)
btn.grid(row=1,column=0)

btn_clear = tk.Button(root, text="clear", command=clear)
btn_clear.grid(row=3,column=0)

result = tk.Label(root, text="نتیجه بررسی")
result.grid(row=2, column=0)


root.mainloop()