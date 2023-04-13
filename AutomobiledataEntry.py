import tkinter as tk
import datetime as dt
from tkinter.ttk import Combobox
from tkinter import *

root = tk.Tk()
root.geometry('1200x900')
root.title('AutomobileDataEntry')

def home_page():
    home_frame = tk.Frame(main_fm)
    lb1 = tk.Label(home_frame,text="Search Car" ,font=("courier", 15))
    lb1.pack()

    combobox=Combobox(root,values=['Audi','BMW','Honda',
                             'Chevrolet','Jaguar','Mazda','Toyota',
                             'Nisan','Volvo',
                             'Porche','Volkswage''Alpha-romen'],width=50,height=10)
    combobox.place(x=670,y=100) 
    home_frame.pack(pady=20)
     
    
def login_page():
    login_frame = tk.Frame(main_fm)
    lb = tk.Label(login_frame,text = "login",font=("courier", 15),)
    lb.pack()
    login_frame.pack(pady=20)
def carcheck_page():
    carcheck_frame = tk.Frame(main_fm)
    lb = tk.Label(carcheck_frame,text="carcheck",font=("courier",15))
    lb.pack()
    carcheck_frame.pack(pady=20)
def gallery_page():
    gallery_frame = tk.Frame(main_fm)
    lb = tk.Label(gallery_frame)
    lb.pack()
    gallery_frame.pack(pady=20)
def about_page():
    about_frame = tk.Frame(main_fm)
    lb = tk.Label(about_frame)
    lb.pack()
    about_frame.pack(pady=20)
    
def hide_indicators():
    home_indicate.config(bg='#3f90ab')
    login_indicate.config(bg='#3f90ab')
    carcheck_indicate.config(bg='#3f90ab')
    gallery_indicate.config(bg='#3f90ab')
    about_indicate.config(bg='#3f90ab')

def delete_pages():
    for frame in main_fm.winfo_children():
        frame.destroy()
        
def indicate(lb,page):
    hide_indicators()
    lb.config(bg='#161717')
    delete_pages()
    page()


option_fm=tk.Frame(root,bg='#3f90ab')

head_frame=tk.Frame(root,bg='#3f90ab',highlightbackground='black',
                     highlightthickness=1)
title_lb=tk.Label(head_frame,text='Automobile DataEntry',bg='#3f90ab' 
                   ,fg='white',font=('Bold',20))

title_lb.pack(side=tk.LEFT)

head_frame.pack(side=tk.TOP,fill=tk.X)

head_frame.pack_propagate(False)
head_frame.configure(height=50)

#button
home_btn = tk.Button(option_fm,text='Home',font=('bold' , 15),
                     fg ='#161717',bd=0,bg='#3f90ab',activebackground='#3f90ab',
                     command=lambda: indicate(home_indicate,home_page))

home_btn.place(x=10,y=50)


#label
home_indicate = tk.Label(option_fm,text=' ', bg='#3f90ab')
home_indicate.place(x=3,y=50, width =5 ,height=40)

login_btn = tk.Button(option_fm,text='Login',font=('bold' , 15),
                     fg ='#161717',bd=0,bg='#3f90ab',activebackground='#3f90ab',
                      command=lambda: indicate(login_indicate,login_page,) )

login_btn.place(x=10,y=120)

login_indicate = tk.Label(option_fm,text=' ', bg='#3f90ab')
login_indicate.place(x=3,y=120, width =5 ,height=40)


carcheck_btn = tk.Button(option_fm,text='Carcheck',font=('bold' , 15),
                     fg ='#161717',bd=0,bg='#3f90ab',activebackground='#3f90ab',
                          command=lambda: indicate(carcheck_indicate,carcheck_page))

carcheck_btn.place(x=10,y=190)

carcheck_indicate = tk.Label(option_fm,text=' ', bg='#3f90ab')
carcheck_indicate.place(x=3,y=190, width =5 ,height=40)

gallery_btn = tk.Button(option_fm,text='Gallery',font=('bold' , 15),
                     fg ='#161717',bd=0,bg='#3f90ab',activebackground='#3f90ab',
                         command=lambda: indicate(gallery_indicate,gallery_page))

gallery_btn.place(x=10,y=260)

gallery_indicate = tk.Label(option_fm,text=' ', bg='#3f90ab')
gallery_indicate.place(x=3,y=260, width =5 ,height=40)

about_btn = tk.Button(option_fm,text='About',font=('bold' , 15),
                     fg ='#161717',bd=0,bg='#3f90ab',activebackground='#3f90ab',
                       command=lambda: indicate(about_indicate,about_page))

about_btn.place(x=10,y=310)

about_indicate = tk.Label(option_fm,text=' ', bg='#3f90ab')
about_indicate.place(x=3,y=310, width =5 ,height=40)


#frame for buttons
option_fm.pack(side=tk.LEFT)
option_fm.pack_propagate(False)
option_fm.configure(width=100,height=900)


main_fm = tk.Frame(root,highlightbackground='black',
                      highlightthickness=1)
main_fm.pack(side=tk.LEFT)
main_fm.pack_propagate(False)
main_fm.configure(height=900,width=1435)
#current Date and Time
date = dt.datetime.now()
l2= tk.Label(root,text=f"{date:%A,%B %d,%y}",font=("courier",12),fg="#3f90ab")
#.pack(side=TOP,anchor="se")
l2.place(x=970,y=55)
#search bar


root.mainloop()
