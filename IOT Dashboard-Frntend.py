from tkinter import *
rt= Tk()
rt.geometry("700x500")


def Home_Login():
    
    e1=Entry(f1)
    e1.place(x=350,y=150,width=175,height=20)
    e1.insert(2,'Username')
    e2=Entry(f1)
    e2.place(x=350,y=190,width=175,height=20)
    e2.insert(0,'Password')
    b2 = Button(f1,text = "Enter",command= Display_Device)
    b2.place(x=350,y=230)


def Display_Device():
    f2=Frame()
    f2.place(x=0,y=0,width=700,height=500)
    lb1=Label(f2,text = "IOT DASHBOARD", font=("courier",25),bg = "green", fg = "black")
    lb1.pack()
    l2=Label(f2,text="Welcome Board IOT World",font=("courier",14),bg = "orange")
    l2.place(x=30,y=100)
    b1 = Button(text = "Display Device_Name to Connect",font=("courier",14),bg = "light green")
    b1.place(x=330,y=100)
    b2 = Button(text = "Device_Details",font=("courier",12),bg="pink",width=16,height=1,command = Divice_Details)
    b2.place(x=430,y=150)
    b3 = Button(text = "Device Controlls",font=("courier",12),bg="yellow",width=16,height=1,command = Divice_Controlls)
    b3.place(x=430,y=200)
    b4 = Button(text = "Device 3",font=("courier",12), bg="skyblue",width=16,height=1)
    b4.place(x=430,y=250)
    b5 = Button(text = "Device 4",font=("courier",12),bg = "violet",width=16,height=1)
    b5.place(x=430,y=300)
    
    
def Divice_Details():
    f3=Frame()
    f3.place(x=0,y=0,width=700,height=500)
    lb2=Label(f3,text = "Device Details From DataBase", font=("courier",25),bg = "green", fg = "black")
    lb2.pack()
    b1 = Button(text = "Divice Location",font=("courier",12),bg ="red",width=18,height=1)
    b1.place(x=30,y=150)
    b2 = Button(text = "Device Name",font=("courier",12),bg="indigo",width=18,height=1)
    b2.place(x=250,y=150)
    b3 = Button(text = "Device Type",font=("courier",12),bg="orange",width=18,height=1)
    b3.place(x=450,y=150)
    b4 = Button(text = "Device Temperature", font=("courier",12),width=18,height=1,bg="blue")
    b4.place(x=30,y=300)
    b5 = Button(text = "Humidity",font=("courier",12),bg = "light yellow",width=18,height=1)
    b5.place(x=250,y=300)
    b5 = Button(text = "Light Status",font=("courier",12),bg = "violet",width=18,height=1)
    b5.place(x=450,y=300)
b6 = Button(text ="Back",font=("courier",12),bg = "#CAD07E",width=18,height=1,command = Display_Device)
b6.pack(side="bottom",anchor="ne")
    
def Divice_Controlls():
    f4=Frame()
    f4.place(x=0,y=0,height=500,width=700)
    lb3=Label(f4,text = "Device Controll to DB", font=("courier",25),bg = "green", fg = "black")
    lb3.pack()
    b6 = Button(text = "Change Device Name", font=("courier",12),width=20,height=1,bg="blue")
    b6.place(x=30,y=100)
    b7= Button(text = "Change Device Type",font=("courier",12),bg = "pink",width=20,height=1)
    b7.place(x=250,y=100)
    b8 = Button(text = "Change Device Location",font=("courier",12),bg = "orange",width=20,height=1)
    b8.place(x=30,y=200)
    b9 = Button(text = "Light ON/OFF",font=("courier",12),bg = "grey",width=20,height=1)
    b9.place(x=250,y=200)
    b10 = Button(text ="Back",font=("courier",12),bg = "#CAD07E",width=18,height=1,command = Display_Device)
    b10.pack(side="bottom",anchor="ne")
    
    
f1=Frame()
f1.place(x=0,y=0,width=700,height=500)    
l1=Label(f1,text="IOT DASHBOARD",font=("courier",25),bg = "green", fg = "black")
l1.pack()
l2=Label(f1,text="Welcome Board",font=("courier",20),bg = "orange")
l2.place(x=30,y=100)
b1 = Button(text = "Login Details",font=("courier",15),command = Home_Login)
b1.place(x=350,y=100)
    
       
"""b1 = Button(f2,text = "device",command = Enter)
    b1.place(x=190,y=100)
    b2=Label(rt,text="DEVICE DETAILS")
    lb2.pack()
    #b2 = Button(f2,text="Enter",command = Login)
   #b2.place(x=170,y=220)"""
    



rt.mainloop()
