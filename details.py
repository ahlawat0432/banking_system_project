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

def show_details():
    k=int(e1.get())
    k2=e2.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Ahlawat0432@', db='bank_system')
    cur = db.cursor()
    r=(k,k2)
    s="select * from customers where customer_id=%s or name=%s"
    t=cur.execute(s,r)
    result=cur.fetchall()

    if s:
        for col in result:
            customer_id = col[0]
            name = col[1]
            balance = col[2]
            tv.insert("", 'end', values=(customer_id,name,balance))
    else:
        messagebox.showinfo("Result", 'Record not found')

    cur.close()
    db.commit()


tv = ttk.Treeview(top)
tv['columns']=('customer_id', 'name','balance')
tv.column('#0', width=0, stretch=NO)
tv.column('customer_id', anchor=CENTER, width=100)
tv.column('name', anchor=CENTER, width=100)
tv.column('balance', anchor=CENTER, width=100)



tv.heading('customer_id', text='customer_id', anchor=CENTER)
tv.heading('name', text='name', anchor=CENTER)
tv.heading('balance', text='balance', anchor=CENTER)
tv.place(x=700,y=150)


L = Label(top, text='Customer Details', fg='white', bg='red', font=('Arial 25 bold'))
L.place(x=500, y=50)

L2 = Label(top, text='Customer_Id', fg='white', bg='blue', font=('Arial 20 bold'))
L2.place(x=150, y=150)

e1 = Entry(top, font=('Arial 20 bold'))
e1.place(x=350, y=150)

L3 = Label(top, text='Name', fg='white', bg='blue', font=('Arial 20 bold'))
L3.place(x=150, y=300)

e2 = Entry(top, font=('Arial 20 bold'))
e2.place(x=350, y=300)

b1 = Button(top, text='Search', font=('Arial 15 bold'),command=show_details)
b1.place(x=300, y=400)

b2=Button(top,text='Back',font=('Arial 15 bold'),command=back)
b2.place(x=300,y=450)

top.mainloop()