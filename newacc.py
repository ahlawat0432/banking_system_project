import os
from tkinter import *
from tkinter import Checkbutton
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk

top=Tk()
top.geometry('1500x800')

path =r"C:\Users\rohit\Downloads\bank image [photoutils.com].jpg"
img = ImageTk.PhotoImage(Image.open(path))

L55 = Label(top,image=img)
L55.pack()

def back():
    top.destroy()
    import home_page

def open_account():
    k = int(e1.get())
    k2=e2.get()
    k3=float(e3.get())

    if not k2 or not k3:
        messagebox.showerror("Input Error", "Please provide both name and initial balance.")
        return

    try:
        balance = float(k3)
        if balance < 0:
            messagebox.showerror("Balance Error", "Balance cannot be negative.")
            return
    except ValueError:
        messagebox.showerror("Balance Error", "Please enter a valid number for balance.")
        return
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Ahlawat0432@', db='bank_system')
    cur = db.cursor()

    s= "INSERT INTO customers VALUES ('%s', '%s', '%s')"%(k,k2,k3)
    result = cur.execute(s)
    if (result > 0):
        messagebox.showinfo("Result","Account Opened Successfully")
    else:
        messagebox.showinfo("Result", "Error Account Not Opened")
    db.commit()
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')

L=Label(top,text='New Account',fg='white',bg='Red',font=('Arial 25 bold'))
L.place(x=500,y=50)

L2=Label(top,text='Customer ID',fg='white',bg='green',font=('Arial 20 bold'))
L2.place(x=200,y=150)

e1=Entry(top,font=('Arial 20 bold'))
e1.place(x=400,y=150)

L3=Label(top,text='Name',fg='white',bg='green',font=('Arial 20 bold'))
L3.place(x=200,y=200)

e2=Entry(top,font=('Arial 20 bold'))
e2.place(x=400,y=200)

L4=Label(top,text='Balance',fg='white',bg='green',font=('Arial 20 bold'))
L4.place(x=200,y=250)

e3=Entry(top,font=('Arial 20 bold'))
e3.place(x=400,y=250)

b1 = Button(top, text='Submit', font=('Arial 15 bold'),command=open_account)
b1.place(x=400, y=400)

b2=Button(top,text='Back',font=('Arial 15 bold'),command=back)
b2.place(x=550,y=400)

top.mainloop()