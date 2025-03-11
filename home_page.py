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
    import login_page


def customer_details():
    top.destroy()
    import details

def deposit_funds():
    top.destroy()
    import dpstfunds

def withdraw_funds():
    top.destroy()
    import withdrawwfunds

def transaction_history():
    top.destroy()
    import transhistory

def new_acc_open():
    top.destroy()
    import newacc

L=Label(top,text='Welcome',fg='white',bg='black',font=('Arial 25 bold'))
L.place(x=550,y=30)

b1=Button(top,text='Customer Details',font=('Arial 15 bold'),command=customer_details)
b1.place(x=300,y=150)

b2=Button(top,text='Deposit Funds',font=('Arial 15 bold'),command=deposit_funds)
b2.place(x=750,y=150)

b3=Button(top,text='Withdraw Funds',font=('Arial 15 bold'),command=withdraw_funds)
b3.place(x=300,y=300)

b4=Button(top,text='Transaction History',font=('Arial 15 bold'),command=transaction_history)
b4.place(x=750,y=300)

b5=Button(top,text='Open New Account',font=('Arial 15 bold'),command=new_acc_open)
b5.place(x=300,y=450)

b6=Button(top,text='Back',font=('Arial 15 bold'),command=back)
b6.place(x=750,y=450)

top.mainloop()