from tkinter import *

buttonList = {
    1: '()%A',
    2: '789/',
    3: '456*',
    4: '123-',
    5: '0.=+'
}

class Block:
    def __init__(self, master, row, column):
        self.but = Button(master)
        self.but['text'] = buttonList[row + 1][column]
        self.but['command'] = getattr(self, 'handler')
        self.but.place(x=column * 100, y=row * 100 + 150, width=100, height=100)

    def handler(self):
        label['text'] += self.but['text']
        print(type(label['text']))

root = Tk()
root.title('Calculator')
root.geometry('400x650')
label = Label(root, bg='black', fg='white')
label.place(x=0, y=0, width=400, height=150)

for row in range(0, 5):
    for column in range(0, 4):
        button = Block(root, row, column)

root.mainloop()