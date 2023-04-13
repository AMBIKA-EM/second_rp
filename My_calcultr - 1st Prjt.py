# import tkinter module

from tkinter import *

from tkinter.ttk import Combobox

#creating window

rt=Tk()
rt.title("CalculatorAmb")
rt.geometry("500x500")

#add widgets

e=Entry(rt,width=65,borderwidth=10)
e.place(x=50,y=90)

label=Label(rt,text="CALCULATOR - AMBI",font =("courier",20),fg ="Purple").pack(side=TOP,padx=20,pady=20)


#usin Lamda function

def btclick(num):

  current=e.get()
  e.delete(0,END)
  e.insert(0,str(current)+str(num))


#creating  buttons

b=Button(rt,text='1',width=15,command=lambda:btclick(1))
b.place(x=20,y=150)

b=Button(rt,text='2',width=15,command=lambda:btclick(2))
b.place(x=150,y=150)

b=Button(rt,text='3',width=15,command=lambda:btclick(3))
b.place(x=280,y=150)

b=Button(rt,text='4',width=15,command=lambda:btclick(4))
b.place(x=20,y=200)

b=Button(rt,text='5',width=15,command=lambda:btclick(5))
b.place(x=150,y=200)

b=Button(rt,text='6',width=15,command=lambda:btclick(6))
b.place(x=280,y=200)

b=Button(rt,text='7',width=15,command=lambda:btclick(7))
b.place(x=20,y=250)

b=Button(rt,text='8',width=15,command=lambda:btclick(8))
b.place(x=150,y=250)

b=Button(rt,text='9',width=15,command=lambda:btclick(9))
b.place(x=280,y=250)
  
b=Button(rt,text='0',width=15,command=lambda:btclick(0))
b.place(x=20,y=300)

#b=Button(rt,text="=",width=15,command=lambda:btclick('='))
#b.place(x=150,y=300)

#b=Button(rt,text="clear",width=15,command=lambda:btclick(clear))
#b.place(x=280,y=300)

# calculating 

def add():
    firstno=e.get()
    global math
    math='addition'
    global f
    f=int(firstno)
    e.delete(0,END)
b= Button(rt,text='+',width=5,command=add)
b.place(x= 410,y= 150)
def sub():
    firstno=e.get()
    global math
    math='subtraction'
    global f
    f=int(firstno)
    e.delete(0,END)
b= Button(rt,text='-',width=5,command=sub)
b.place(x= 410,y= 200)
def mul():
    firstno=e.get()
    global math
    math='multiplication'
    global f
    f=int(firstno)
    e.delete(0,END)
b= Button(rt,text='*',width=5,command=mul)
b.place(x= 410,y= 250)
def div():
    firstno=e.get()
    global math
    math='division'
    global f
    f=int(firstno)
    e.delete(0,END)
b= Button(rt,text='/',width=5,command=div)
b.place(x= 410,y= 300)

def clear():
    e.delete(0,END)    
b= Button(rt,text='clear',width=15,command=clear)
b.place(x= 280,y= 300)

def eq():
  secondno=e.get()
  e.delete(0,END)
  if math=='addition':
     e.insert(0,f+int(secondno))
  elif math=='subtraction':
    e.insert(0,f-int(secondno))
  elif math=='multiplication':
    e.insert(0,f*int(secondno))
  elif math=='division':
    e.insert(0,f/int(secondno))
              
b= Button(rt,text='=',width=15,command=eq)
b.place(x= 150,y= 300)

# ANOTHER METHOD FOR ENTRY WIGDETs

lbl=Label(rt,text="Name",font =(" courier",15))
#lbl.pack(side=LEFT,padx=20,pady=250)
lbl.place(x=20,y=350)


entry=Entry(rt)
#entry.pack(side=LEFT,padx=20,pady=250)
entry.place(x=100,y=355)

lb2=Label(rt,text="Place",font =(" courier",15))
lb2.place(x=20,y=400)
#lb2.pack()

combobox=Combobox(rt,values=['Tamil Nadu ', 'Andra Pradesh','Kerala' , 'Karnataka'])
combobox.place(x=90,y=400)
#combobox.pack(side=LEFT,padx=70,pady=70)


#listbox
l3=Label(rt,text="Technical Skills",font=("courier",15))
l3.place(x=250,y=350)
#l3.pack()
listbox=Listbox(rt,selectmode=MULTIPLE)
listbox.insert(1,'Python')
listbox.insert(1,'C')
listbox.insert(1,'Java')
listbox.insert(1,'Html/Css')
listbox.insert(1,'Java Script')
listbox.insert(1,'C++')
listbox.insert(1,'SQL/Oracle')
listbox.place(x=280,y=370)
#listbox.pac()




#entry=Entry(rt)
#entry.place(x=150,y=395)

#entry=Entry(rt)
#entry.place(x=300,y=400)

#combobox

#lb1=Label(rt,text='Select your State')





#mainloop
rt.mainloop()
