
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import datetime as dt

rt=tk.Tk()

rt.geometry('1000x700')


def toggle_menu():

    def collapse_toggle_menu():
        option_fm.destroy()
        toggle_btn.config(text='☰')
        toggle_btn.config(command=toggle_menu)

    

    def hide_indicators():
        home_indicate.config(bg='#c3c3c3')
        myAccount_indicate.config(bg='#c3c3c3')
        calender_indicate.config(bg='#c3c3c3')
        photoGallery_indicate.config(bg='#c3c3c3')
        about_indicate.config(bg='#c3c3c3')
        
    def indicate(lb,):
        hide_indicators()
        lb.config(bg='#158aff')
      
        
    option_fm=tk.Frame(rt,bg='#c3c3c3')

    
    home_btn=tk.Button(option_fm,text='Home', font=('Bold',20),
                      bd=0,bg='#c3c3c3',fg='white',
                      activebackground='#c3c3c3',activeforeground='white', 
                      command=lambda: indicate(home_indicate,))
    
    
    home_btn.place(x=20,y=20)

    home_indicate = tk.Label(option_fm,text='', bg='#c3c3c3')

    home_indicate.place(x=20,y=20,width=5,height=45)

    myAccount_btn=tk.Button(option_fm,text='MyAccount', font=('Bold',20),
                            bd=0,bg='#c3c3c3',fg='white',
                            activebackground='#c3c3c3',activeforeground='white', 
                            command=lambda: indicate(myAccount_indicate))

    myAccount_btn.place(x=20,y=80)
    
    myAccount_indicate=tk.Label(option_fm,text='',bg='#c3c3c3')

    myAccount_indicate.place(x=20,y=80,width=5,height=45)
    
    calender_btn=tk.Button(option_fm,text='Calender', font=('Bold',20),
                           bd=0,bg='#c3c3c3',fg='white',
                           activebackground='#c3c3c3',activeforeground='white', 
                           command=lambda: indicate(calender_indicate))

    calender_btn.place(x=20,y=140)

    calender_indicate =tk.Label(option_fm,text='',bg='#c3c3c3')

    calender_indicate.place(x=20,y=140,width=5,height=45)
    

    photoGallery_btn=tk.Button(option_fm,text='PhotoGallery', font=('Bold',20),
                               bd=0,bg='#c3c3c3',fg='white',
                               activebackground='#c3c3c3',activeforeground='white', 
                               command=lambda: indicate(photoGallery_indicate))

    photoGallery_btn.place(x=20,y=200)

    photoGallery_indicate=tk.Label(option_fm,text='',bg='#c3c3c3')

    photoGallery_indicate.place(x=20,y=200,width=5,height=45)

    about_btn=tk.Button(option_fm,text='About', font=('Bold',20),
                        bd=0,bg='#c3c3c3',fg='white',
                        activebackground='#c3c3c3',activeforeground='white', 
                        command=lambda:indicate(about_indicate))

    about_btn.place(x=20,y=260)

    about_indicate=tk.Label(option_fm,text='',bg='#c3c3c3')

    about_indicate.place(x=20,y=260,width=5,height=45)
    

    window_height = rt.winfo_height()

    option_fm.place(x=0,y=50,height=window_height,width=200)

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
canvas=Canvas(rt,width=700,height=500)
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
l2=Label(rt,text=f"{date:%A,%B %d,%y}",font=("courier",12),fg="blue")
#.pack(side=TOP,anchor="se")
l2.place(x=750,y=55)

#label.pack()


# TExtBox-Entry Wigdets

#e=Entry(rt,width=75,borderwidth=10)
#e.place(x=400,y=100)

label2=Label(rt, text="Search Book" ,font=("courier", 15))
label2.place(x=520,y=100)

combobox=Combobox(rt,values=['Title','Author','Non-Fiction',
                             'Fiction','Kids','Adult','ComputerScience',
                             'History/Social Science','Medical/ Biological',
                             'Cooking/Foods','Geographical''Art'],width=50,height=10)
combobox.place(x=670,y=100)

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
