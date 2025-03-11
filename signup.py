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

path = r"C:\Users\rohit\Downloads\bank image [photoutils.com].jpg"
img = ImageTk.PhotoImage(Image.open(path))

L55 = Label(top, image=img)
L55.pack()


def back():
    top.destroy()
    import login_page

def insert():
    k=e1.get()
    k2=e2.get()
    k3=e3.get()

    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Ahlawat0432@',db='bank_system')
    cur=db.cursor()
    s="insert into employees values('%s','%s','%s')"%(k,k2,k3)
    result=cur.execute(s)
    if(result>0):
        messagebox.showinfo("Result","Record insert successfully")
    else:
        messagebox.showinfo("Result","Record not insert successfully")
    db.commit()
    e1.delete(0,'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')

L=Label(top,text='Employee Registration',fg='white',bg='Red',font=('Arial 25 bold'))
L.place(x=500,y=50)

L2=Label(top,text='Employee ID',fg='white',bg='green',font=('Arial 20 bold'))
L2.place(x=200,y=150)

e1=Entry(top,font=('Arial 20 bold'))
e1.place(x=400,y=150)

L3=Label(top,text='UserName',fg='white',bg='green',font=('Arial 20 bold'))
L3.place(x=200,y=200)

e2=Entry(top,font=('Arial 20 bold'))
e2.place(x=400,y=200)

L4=Label(top,text='Password',fg='white',bg='green',font=('Arial 20 bold'))
L4.place(x=200,y=250)

e3=Entry(top,font=('Arial 20 bold'),show="*")
e3.place(x=400,y=250)

b1 = Button(top, text='Submit', font=('Arial 15 bold'),command=insert)
b1.place(x=350, y=400)

b2=Button(top,text='Back',font=('Arial 15 bold'),command=back)
b2.place(x=500,y=400)

cbk = Checkbutton(top, command=showpassword)
cbk.place(x=730, y=260)

top.mainloop()