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

def process_deposit():
    k = int(e1.get())
    k2 = e2.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Ahlawat0432@', db='bank_system')
    cur = db.cursor()

    cur.execute("UPDATE customers SET balance = balance + %s WHERE customer_id = %s", (k2, k))
    cur.execute("INSERT INTO transactions (customer_id, amount, transaction_type) VALUES (%s, %s, 'deposit')",
                (k, k2))

    db.commit()
    messagebox.showinfo("Deposit", "Deposit Successful")
    cur.close()
    db.commit()

L = Label(top, text='Deposit Funds', fg='white', bg='red', font=('Arial 25 bold'))
L.place(x=500, y=50)

L2 = Label(top, text='Customer_Id', fg='white', bg='blue', font=('Arial 20 bold'))
L2.place(x=150, y=150)

e1 = Entry(top, font=('Arial 20 bold'))
e1.place(x=350, y=150)

L3 = Label(top, text='Amount', fg='white', bg='blue', font=('Arial 20 bold'))
L3.place(x=150, y=300)

e2 = Entry(top, font=('Arial 20 bold'))
e2.place(x=350, y=300)

b1 = Button(top, text='Deposit', font=('Arial 15 bold'),command=process_deposit)
b1.place(x=300, y=400)

b2=Button(top,text='Back',font=('Arial 15 bold'),command=back)
b2.place(x=300,y=450)

top.mainloop()