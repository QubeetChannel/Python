import random
from tkinter import *

# class Block:
#     def __init__(self, master, func):
#         self.ent = Entry(master, width=20)
#         self.but = Button(master, text="Преобразовать")
#         self.lab = Label(master, width=20, bg='black', fg='white')
#         self.but['command'] = getattr(self, func)
#         self.ent.pack()
#         self.but.pack()
#         self.lab.pack()
#
#     def str_to_sort(self):
#         s = self.ent.get()
#         s = s.split()
#         s.sort()
#         self.lab['text'] = ' '.join(s)
#
#     def str_reverse(self):
#         s = self.ent.get()
#         s = s.split()
#         s.reverse()
#         self.lab['text'] = ' '.join(s)
#
#
# root = Tk()
#
# first_block = Block(root, 'str_to_sort')
# second_block = Block(root, 'str_reverse')
#
# root.mainloop()

class Color:
    def __init__(self):
        self.red_10 = "00"
        self.green_10 = "00"
        self.blue_10 = "00"
        self.red_16 = "00"
        self.green_16 = "00"
        self.blue_16 = "00"
        self.HTML = "000000"

    def get_color(self):
        while True:
            rgb = input("Введите RGB код, через пробел: \n")
            rgb = rgb.split(" ")
            if len(rgb) == 3:
                try:
                    for i in range(3):
                        rgb[i] = int(rgb[i])
                except ValueError:
                    print("Введен неправильный формат, введите 3 целых числа\n")
                else:
                    if min(rgb) < 0 or max(rgb) > 255:
                        print("Числа не могут быть меньше 0 или больше 255.\n")
                    else:
                        self.red_10 = rgb[0]
                        self.red_16 = convert_to_16(rgb[0])
                        self.green_10 = rgb[1]
                        self.green_16 = convert_to_16(rgb[1])
                        self.blue_10 = rgb[2]
                        self.blue_16 = convert_to_16(rgb[2])
                        self.HTML = f"{self.red_16}{self.green_16}{self.blue_16}"

                        print("RGB-код готов!")
                        break
            else:
                print("Вы ввели не то количество аргументов, введите 3 числа.\n")

def convert_to_16(number):
    digits = "0123456789abcdef"
    result = ""
    if number < 16:
        result = "0" + digits[number % 16]
    else:
        while number > 0:
            result = digits[number % 16] + result
            number //= 16
    return result.upper()

def convert_to_10(number):
    digits = "0123456789abcdef"
    for i in number:
        if i.lower() not in digits[0:10]:
            return None


def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result









rgb_start = Color()
# rgb_start.get_color()
# rgb_end.get_color()
print(f"R10 - {rgb_start.red_10}, G10 - {rgb_start.green_10}, B10 - {rgb_start.blue_10}")
print(f"R16 - {rgb_start.red_16} \nG16 - {rgb_start.green_16} \nB16 - {rgb_start.blue_16}")
print(f"{rgb_start.HTML}")
# digit = "0123456789"
# print(digit[0:5])
