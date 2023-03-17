from tkinter import *
import pandas as pd
df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")

rt = Tk()
rt.title("Automobile_Details")
rt.geometry('900x500')
#creating label
lb =Label(rt,text = "Automobile Details ",font=("courier",15),fg='darkgreen')
lb.place(x=350,y=40)
lbl = Label(rt, text = " ")

"""Create Label
label = Label(rt, text="Hello World!", font="BOLD")
label.pack()"""


def clicked1():
    dis= df.head(5)
    lbl.configure(text = dis)
    lbl.place(x=250,y=100)
    #lbl.config(text="")

def expensive_car():
   
    df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
    df = df [['company','price']][df.price==df['price'].max()]
    dis= df
    lbl.configure(text = dis)
    lbl.place(x=250,y=100)
   # lbl.config(text="")

def audi_only():
   
    df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
    car_Manufacturers = df.groupby('company')
    toyotaDf = car_Manufacturers.get_group('toyota')
    dis= toyotaDf
    lbl.configure(text = dis)
    lbl.place(x=250,y=100)
   # lbl.config(text="")

def total_cars_per_company():
    df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
    df = df['company'].value_counts()
    dis= df
    lbl.configure(text = dis)
    lbl.place(x=250,y=100)
   # lbl.config(text="")
def Each_comp_High_price_car():
   
    df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
    car_Manufacturers = df.groupby('company')
    priceDf = car_Manufacturers['company','price'].max()
    dis= priceDf
    lbl.configure(text = dis)
    lbl.place(x=250,y=100)
def sort_car_by_price_column():
   
    import pandas as pd
    carsDf = pd.read_csv("D:\\Python\\Articles\\pandas\\automobile-dataset\\Automobile_data.csv")
    carsDf = carsDf.sort_values(by=['price', 'horsepower'], ascending=False)
    dis = carsDf.head(5)
    lbl.configure(text = dis)
    lbl.place(x=250,y=100)
def Each_comp_High_price_car():
   
    df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
    car_Manufacturers = df.groupby('company')
    priceDf = car_Manufacturers['company','price'].max()
    dis= priceDf
    lbl.configure(text = dis)
    lbl.place(x=250,y=100)
def Each_comp_High_price_car():
   
    df = pd.read_csv("C:\\Users\\ambik\\Python\\Automobile_data.csv")
    car_Manufacturers = df.groupby('company')
    priceDf = car_Manufacturers['company','price'].max()
    dis= priceDf
    lbl.configure(text = dis)
    lbl.place(x=250,y=100)
   # lbl.config(text="")
    
#def remove_text():
	#label.config(text="")

    
#button creating    
btn1 = Button(rt, text = "Display" ,
             fg = "blue", command=clicked1)
btn1.place(x=20,y=200)

btn1 = Button(rt, text = "Expensive car" ,
             fg = "blue", command=expensive_car)
btn1.place(x=90,y=200)

btn1 = Button(rt, text = "audi only " ,
             fg = "blue", command=audi_only)
btn1.place(x=200,y=200)

btn1 = Button(rt, text = "Total_cars " ,
             fg = "blue", command=total_cars_per_company)
btn1.place(x=550,y=200)

btn1 = Button(rt, text = "sort_car_by_price_column " ,
             fg = "blue", command=Each_comp_High_price_car)
btn1.place(x=700,y=200)

btn1 = Button(rt, text = "Each_comp_High_price_car " ,
             fg = "blue", command=Each_comp_High_price_car)
btn1.place(x=800,y=200)

# Create Delete Button
#Button(rt, text="Delete", command=remove_text).pack()

"""def clear_data():
    lb1.delete(*lb1.get_children())
    return None"""



rt.mainloop()
