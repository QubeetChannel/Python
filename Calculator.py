from tkinter import *

class Block:
    def __init__(self, master, row, column):
        self.Row = row
        self.Column = column

        ###   СОЗДАНИЕ И НАИМЕНОВАНИЕ КНОПКИ   ###
        self.button = Button(master, font=('Verdana', 25), relief="raised", overrelief="ridge")
        self.button.place(x=column * 100, y=row * 100 + 150, width=100, height=100)
        self.button['text'] = buttonList[row + 1][column]
        self.out_touch(self)

        ###   БИНДЫ ДЛЯ КНОПОК   ###
        self.button.bind('<Button-1>', self.handler)
        self.button.bind("<Enter>", self.in_touch)
        self.button.bind("<Leave>", self.out_touch)

    ###   ФУНКЦИИ ДЛЯ ДИЗАЙНА КНОПОК   ###
    def out_touch(self, event):
        if buttonColorList[self.Row + 1][self.Column] == '0':
            self.button.configure(background='#FFC618', relief='raised', overrelief='ridge')
        elif buttonColorList[self.Row + 1][self.Column] == '1':
            self.button.configure(background='#FFFFFF', relief='raised', overrelief='ridge')

    def in_touch(self, event):
        if buttonColorList[self.Row + 1][self.Column] == '0':
            self.button.configure(background='#FFCC00', relief='flat', overrelief='flat')
        elif buttonColorList[self.Row + 1][self.Column] == '1':
            self.button.configure(background='lightgray', relief='flat', overrelief='flat')

    ###   ОБРАБОТЧИК ДЛЯ КНОПОК   ###
    def handler(self, event):
        try:
            int(self.button['text'])
        except Exception:
            if self.button['text'] in '+-*/':
                if label['text'][len(label['text'])-1] in '+-*/':
                    label['text'] = label['text'][0:len(label['text'])-1] + self.button['text']
                else:
                    label['text'] += self.button['text']
            elif self.button['text'] == 'E':
                label['text'] = ''
        else:
            label['text'] += self.button['text']

###   УСТАНОВОЧНЫЕ СЛОВАРИ   ###
buttonList = {
    1: '()%E',
    2: '789/',
    3: '456*',
    4: '123-',
    5: '0.=+'
}

buttonColorList = {
    1: '0000',
    2: '1110',
    3: '1110',
    4: '1110',
    5: '1100'
}

###   НАЧАЛО ПРОГРАММЫ   ###
root = Tk()
root.title('Calculator')
root.geometry('400x650')

label = Label(root, background='#949494', foreground='#FFFFFF', font=('Verdana', 60))
label.place(x=0, y=0, width=400, height=150)
for row in range(0, 5):
    for column in range(0, 4):
        button = Block(root, row, column)

root.mainloop()