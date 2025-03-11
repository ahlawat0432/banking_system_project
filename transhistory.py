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

def show_history():
    k = int(e1.get())
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Ahlawat0432@', db='bank_system')
    cur = db.cursor()

    s="SELECT * FROM transactions WHERE customer_id = %s"
    t = cur.execute(s,k)
    result = cur.fetchall()

    if t:
        for col in result:
            transaction_id= col[0]
            customer_id= col[1]
            amount= col[2]
            transaction_type= col[3]
            date=col[4]
            tv.insert("", 'end', values=(transaction_id,customer_id,amount,transaction_type,date))
    else:
        messagebox.showinfo("Result", 'Record not found')

    cur.close()
    db.commit()

tv = ttk.Treeview(top)
tv['columns']=('transaction_id','customer_id','amount','transaction_type','date')
tv.column('#0', width=0, stretch=NO)
tv.column('transaction_id', anchor=CENTER, width=150)
tv.column('customer_id', anchor=CENTER, width=150)
tv.column('amount', anchor=CENTER, width=150)
tv.column('transaction_type', anchor=CENTER, width=150)
tv.column('date', anchor=CENTER, width=150)



tv.heading('transaction_id', text='Transaction ID', anchor=CENTER)
tv.heading('customer_id', text='Customer ID', anchor=CENTER)
tv.heading('amount', text='Amount', anchor=CENTER)
tv.heading('transaction_type', text='Type', anchor=CENTER)
tv.heading('date', text='Date', anchor=CENTER)
tv.place(x=300,y=300)

L = Label(top, text='Transaction History', fg='white', bg='red', font=('Arial 25 bold'))
L.place(x=500, y=50)

L2 = Label(top, text='Customer_Id', fg='white', bg='blue', font=('Arial 20 bold'))
L2.place(x=150, y=150)

e1 = Entry(top, font=('Arial 20 bold'))
e1.place(x=350, y=150)

b1 = Button(top, text='Search', font=('Arial 15 bold'),command=show_history)
b1.place(x=350, y=200)

b2=Button(top,text='Back',font=('Arial 15 bold'),command=back)
b2.place(x=500,y=200)

top.mainloop()