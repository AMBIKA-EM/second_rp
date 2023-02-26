import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import datetime as dt

rt=tk.Tk()

rt.geometry('1000x700')


def toggle_menu():

    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)
        
    toggle_menu_fm=tk.Frame(rt,bg='#158aff')
    
    
    home_btn=tk.Button(toggle_menu_fm,text='Home',
                       font=('Bold',20),bd=0,bg='#158aff',fg='white',
                       activebackground='#158aff',activeforeground='white')

    home_btn.place(x=20,y=20)

    myAccount_btn=tk.Button(toggle_menu_fm,text='MyAccount',
                       font=('Bold',20),bd=0,bg='#158aff',fg='white',
                       activebackground='#158aff',activeforeground='white')

    myAccount_btn.place(x=20,y=80)
    

    calender_btn=tk.Button(toggle_menu_fm,text='Calender',
                       font=('Bold',20),bd=0,bg='#158aff',fg='white',
                       activebackground='#158aff',activeforeground='white')

    calender_btn.place(x=20,y=140)

    photoGallery_btn=tk.Button(toggle_menu_fm,text='PhotoGallery',
                       font=('Bold',20),bd=0,bg='#158aff',fg='white',
                       activebackground='#158aff',activeforeground='white')

    photoGallery_btn.place(x=20,y=200)

    about_btn=tk.Button(toggle_menu_fm,text='About',
                       font=('Bold',20),bd=0,bg='#158aff',fg='white',
                       activebackground='#158aff',activeforeground='white')

    about_btn.place(x=20,y=260) 

    window_height = rt.winfo_height()

    toggle_menu_fm.place(x=0,y=50,height=window_height,width=200)

    toggle_btn.config(text='X')
    toggle_btn.config(command=collapse_toggle_menu)
    
head_frame=tk.Frame(rt,bg='#158aff',highlightbackground='white',
                    highlightthickness=1)


toggle_btn=tk.Button(head_frame,text='☰',bg='#158aff',fg='white',
                     font=('Bold',20),bd=0,
                     activebackground='#158aff',activeforeground='white',
                     command=toggle_menu)

toggle_btn.pack(side=tk.LEFT)

title_lb=tk.Label(head_frame,text='SW-LIBRARY',bg='#158aff' 
 ,fg='white',font=('Bold',20))

title_lb.pack(side=tk.LEFT)



head_frame.pack(side=tk.TOP,fill=tk.X)

head_frame.pack_propagate(False)
head_frame.configure(height=50)

rt.title('SW -Library')
canvas=Canvas(rt,width=500,height=500)
#canvas.place(x=20,y=500)
canvas.pack(side=LEFT, padx=200,pady=200)
my_image=PhotoImage(file='C:\\Users\\ambik\\AMBIKA\\Tkinter\\images\\giphy.gif')
canvas.create_image(0,0,anchor =NW ,image=my_image)
'''l=Label(rt,text="SW-Library" ,font=("courier",50),fg="purple")
l.place(x=40,y=25)'''
#.pack(pady=20,side=TOP,anchor="w")
#rt.title("SW-Library")
'''l=Label(rt,text="About us" ,font=("courier",12),fg="black")
l.place(x=500,y=25)
l=Label(rt,text="ASk-a-Librarian" ,font=("courier",12),fg="black")
l.place(x=615,y=25)
l=Label(rt,text="ContactUs" ,font=("courier",12),fg="black")
l.place(x=780,y=25)'''
#rt.geometry("1000x600")
date = dt.datetime.now()
label=Label(rt,text=f"{date:%A,%B %d,%y}",font="calibri,10",fg="navyblue")
#.pack(side=TOP,anchor="se")
label.place(x=700,y=55)

#label.pack()


# TExtBox-Entry Wigdets

#e=Entry(rt,width=75,borderwidth=10)
#e.place(x=400,y=100)

label2=Label(rt, text="Search Book" ,font=("courier", 15))
label2.place(x=445,y=100)

combobox=Combobox(rt,values=['Title','Author''Non-Fiction','Fiction','Kids','Adult','ComputerScience''History/Social Science''Medical/ Biological','Cooking/Foods','Art'],width=50,height=10)
combobox.place(x=600,y=100)

#combobox=Combobox(rt,Values=[])
#combobox.place(x=400,y=100)
#combobox.pack()

'''listbox=Listbox(rt,selectmode=MULTIPLE)
listbox.insert(1,'Non-Fiction')
listbox.insert(1,'Fiction')
listbox.insert(1,'ComputerScience')
listbox.insert(1,'Medical/ Biological')
listbox.insert(1,'History/Social Science')
listbox.insert(1,'Art')
listbox.insert(1,'Cooking/Foods')                  
listbox.insert(1,)
listbox.place(x=20,y=300)
#listbox.pack()'''






rt.mainloop()
