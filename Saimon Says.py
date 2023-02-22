# from tkinter import *
# import random
#
#
#
#
#
#
#
# root = Tk()
# root.geometry('500x500')
#
# Red = Button(background='#FF0000', activebackground='#c80000')
# Red.place(x=0, y=0, width=100, height=100)
#
# Yellow = Button(background='#FFFF00', activebackground='#c8c800')
# Yellow.place(x=100, y=0, width=100, height=100)
#
# Green = Button(background='#00FF00', activebackground='#00c800')
# Green.place(x=0, y=100, width=100, height=100)
#
# Blue = Button(background='#0000FF', activebackground='#0000c8')
# Blue.place(x=100, y=100, width=100, height=100)

#
#
#
#
#
#
# root.mainloop()




import random

ColorList = []
Colors = ("red", "yellow", "green", "blue")
for i in range(0,10):
    ColorList.append(Colors[random.randint(0, 3)])

print(ColorList)