from tkinter import *
from tkinter import ttk

root = Tk()  # создаем корневой объект - окно
root.title("Калькулятор")  # устанавливаем заголовок окна
root.geometry("400x600")  # устанавливаем размеры окна


output = Label(background="gray",width=40)
entry = Entry()

buttonList = {
    1: ["(", ")", "%", "A"],
    2: ["7", "8", "9", "/"],
    3: ["4", "5", "6", "*"],
    4: ["1", "2", "3", "-"],
    5: ["0", ".", "=", "+"]
}
buttonList2 = {
    1: "()%A",
    2: "789/",
    3: "456*",
    4: "123-",
    5: "0.=+"
}




def One():
    output.configure(text=output["text"]+"1")
def Two():
    output.configure(text=output["text"]+"2")
def Three():
    output.configure(text=output["text"]+"3")
def Four():
    output.configure(text=output["text"]+"4")
def Five():
    output.configure(text=output["text"]+"5")
def Six():
    output.configure(text=output["text"]+"6")
def Seven():
    output.configure(text=output["text"]+"7")
def Eight():
    output.configure(text=output["text"]+"8")
def Nine():
    output.configure(text=output["text"]+"9")
def Zero():
    output.configure(text=output["text"]+"0")
def Plus():
    output.configure(text=output["text"]+"+")
def Minus():
    output.configure(text=output["text"]+"-")
def Multiply():
    output.configure(text=output["text"]+"*")
def Divide():
    output.configure(text=output["text"]+"/")
def OpenBracket():
    output.configure(text=output["text"]+"(")
def ClosingBracket():
    output.configure(text=output["text"]+")")
def Equals():
    output.configure(text=output["text"]+"=")
def Dot():
    output.configure(text=output["text"]+".")
def Percent():
    output.configure(text=output["text"]+"%")
def Erase():
    output.configure(text="")


output.grid(row=1, column=1, columnspan=4)

One = ttk.Button(text="1", command=One)
One.grid(row=5, column=1)

Two = ttk.Button(text="2", command=Two)
Two.grid(row=5, column=2)

Three = ttk.Button(text="3", command=Three)
Three.grid(row=5, column=3, padx=0)

Four = ttk.Button(text="4", command=Four)
Four.grid(row=4, column=1)

Five = ttk.Button(text="5", command=Five)
Five.grid(row=4, column=2)

Six = ttk.Button(text="6", command=Six)
Six.grid(row=4, column=3)

Seven = ttk.Button(text="7", command=Seven)
Seven.grid(row=3, column=1)

Eight = ttk.Button(text="8", command=Eight)
Eight.grid(row=3, column=2)

Nine = ttk.Button(text="9", command=Nine)
Nine.grid(row=3, column=3)

Zero = ttk.Button(text="0", command=Zero)
Zero.grid(row=6, column=1)

Plus = ttk.Button(text="+", command=Plus)
Plus.grid(row=6, column=4)

Minus = ttk.Button(text="-", command=Minus)
Minus.grid(row=5, column=4)

Multiply = ttk.Button(text="*", command=Multiply)
Multiply.grid(row=4, column=4)

Divide = ttk.Button(text="/", command=Divide)
Divide.grid(row=3, column=4)

OpenBracket = ttk.Button(text="(", command=OpenBracket)
OpenBracket.grid(row=2, column=1)

ClosingBracket = ttk.Button(text=")", command=ClosingBracket)
ClosingBracket.grid(row=2, column=2)

Equals = ttk.Button(text="=", command=Equals)
Equals.grid(row=6, column=3)

Dot = ttk.Button(text=".", command=Dot)
Dot.grid(row=6, column=2)

Percent = ttk.Button(text="%", command=Percent)
Percent.grid(row=2, column=3)

Erase = ttk.Button(text="AC", command=Erase)
Erase.grid(row=2, column=4)

root.mainloop()