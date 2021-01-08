import tkinter as tk
from tkinter import messagebox
import random
from tkinter import *


root = tk.Tk()
root.title("Log-in Lottery Portal")
root.geometry("500x300")
root.configure(bg='Yellow')


kid1 = tk.Canvas(root, width=500, height=450)
kid1.pack()

label1 = tk.Label(root, text='Type your Age: ', font="helvetica")
kid1.create_window(88, 100, window=label1)

entry1 = tk.Entry(root)
kid1.create_window(225, 100, window=entry1)


label2 = tk.Label(root, text='Name: ',font="helvetica")
kid1.create_window(60, 50, window=label2)


entry2 = tk.Entry(root)
kid1.create_window(170, 50, window=entry2)


label3 = tk.Label(root, text='Surname: ',font="helvetica")
kid1.create_window(67, 75, window=label3)

entry3 = tk.Entry(root)
kid1.create_window(190, 75, window=entry3)


def values():
    global Age
    Age = float(entry1.get())

    if Age >= 18:
        age_check = ('You qualify!!')
        messagebox.showinfo(age_check, "Welcome to Ithuba National Lottery Of SA" )
        root.destroy()
        import lotto_file
        lotto_file.confirm()

    else:
        age_check = ('Ohhhw sorry')
        messagebox.showerror(age_check, "You don't qualify!")


#button
button1 = tk.Button(root, text='Submit', command=values,
                    bg='orange')
kid1.create_window(270, 160, window=button1)

labe3 = Button(root,text='Exit', height="1",width="20", bd=3, font=('arial', 11, 'bold'), relief="groove", fg="white",
bg="red" ,command= quit)


labe3.pack()
Label(root,text="").pack()

root.mainloop()