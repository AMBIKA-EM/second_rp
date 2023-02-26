from tkinter import*
root = Tk()
c=Canvas(root,width=600,height=500)
c.pack()
#c.create_line(0,500,600,0,dash=(3,3))
#c.create_line(0,0,600,500,dash=(3,3))
#c.create_line(0,400,0,400,dash=(3,3))
c.create_rectangle(150,250,450,350)
#c.create_rectangle(150,250,350,450)

root.mainloop()
