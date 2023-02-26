from tkinter import *
rt=Tk()
rt.title('Library Image')
canvas1=Canvas(rt,width=2000,height=1500)
#canvas.place(x=20,y=500)
canvas1.pack(side=LEFT, padx=300,pady=300)
my_image=PhotoImage(file='C:\\Users\\ambik\\AMBIKA\\Tkinter\\images\\giphy.gif')
canvas1.create_image(0,0,anchor =NW ,image=my_image)

canvas2=Canvas(rt,width=2000,height=1500)
canvas2.place(x=200,y=500)

#canvas2.pack(side=RIGHT, padx=100,pady=100)
my_image1=PhotoImage(file='C:\\Users\\ambik\\AMBIKA\\Tkinter\\images\\giphy (1).gif')
canvas2.create_image(0,0,anchor =SE ,image=my_image)


