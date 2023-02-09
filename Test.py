import pygame
import tkinter
import random

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
                        self.red_16 = convert_to(rgb[0], 16)
                        self.green_10 = rgb[1]
                        self.green_16 = convert_to(rgb[1], 16)
                        self.blue_10 = rgb[2]
                        self.blue_16 = convert_to(rgb[2], 16)
                        self.HTML = f"{self.red_16}{self.green_16}{self.blue_16}"

                        print("RGB-код готов!")
                        break
            else:
                print("Вы ввели не то количество аргументов, введите 3 числа.\n")

# def convert_to(number, base, upper=False):
#     digits = '0123456789abcdefghijklmnopqrstuvwxyz'
#     if base > len(digits):
#         return None
#     result = ''
#     while number > 0:
#         result = digits[number % base] + result
#         number //= base
#     return result.upper() if upper else result




def convert_to(number, base):
    digits = "0123456789abcdef"
    result = ""
    if number < base:
        result = "0" + digits[number % base]
    else:
        while number > 0:
            result = digits[number % base] + result
            number //= base
    return result.upper()

def convert_from(number, base):
    digits = "0123456789abcdef"
    for i in number:
        if i.lower() not in digits[0:base]:
            return None



#
rgb_start = Color()
rgb_start.get_color()
# rgb_end.get_color()
print(f"R10 - {rgb_start.red_10} \nG10 - {rgb_start.green_10} \nB10 - {rgb_start.blue_10}")
print(f"R16 - {rgb_start.red_16} \nG16 - {rgb_start.green_16} \nB16 - {rgb_start.blue_16}")
print(f"{rgb_start.HTML}")
# digit = "0123456789"
# print(digit[0:5])
