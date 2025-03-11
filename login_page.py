import os
from tkinter import *
from tkinter import Checkbutton
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

top = Tk()
top.geometry('1500x600')

def showpassword():
    if e3.cget('show') == "*":
        e3.config(show='')
    else:
        e3.config(show="*")

def registration():
    top.destroy()
    import signup

def login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Ahlawat0432@', db='bank_system')
    cur = db.cursor()
    cur.execute("select * from employees where username=%s and password=%s",  (e1.get(),e3.get()))
    row=cur.fetchone()

    if row== None:
        messagebox.showerror("Error","Invalid User Name and Password")
    else:
        top.destroy()
        os.system("python home_page.py")

path = r"C:\Users\rohit\Downloads\bank image [photoutils.com].jpg"
img = ImageTk.PhotoImage(Image.open(path))

L55 = Label(top, image=img)
L55.pack()

L = Label(top, text='Employee Login', fg='white', bg='red', font=('Arial 25 bold'))
L.place(x=500, y=50)

L2 = Label(top, text='UserName', fg='white', bg='blue', font=('Arial 20 bold'))
L2.place(x=200, y=150)

e1 = Entry(top, font=('Arial 20 bold'))
e1.place(x=350, y=150)

L4 = Label(top, text='Password', fg='white', bg='blue', font=('Arial 20 bold'))
L4.place(x=200, y=250)

e3 = Entry(top, font=('Arial 20 bold'), show="*")
e3.place(x=350, y=250)

b1 = Button(top, text='Login', font=('Arial 15 bold'),command=login)
b1.place(x=350, y=400)

b2=Button(top,text='SignUp',font=('Arial 15 bold'),command=registration)
b2.place(x=500,y=400)

cbk = Checkbutton(top, command=showpassword)
cbk.place(x=670, y=255)
top.mainloop()