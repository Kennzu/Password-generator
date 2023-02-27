import string
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox

tsifri = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

bukvi = list(string.ascii_letters)
for i in range(10):
    bukvi.append(str(i))

bukvi.append('_')
bukvi.append('-')
bukvi.append('!')
bukvi.append('?')

def parol():
    name = entrySots.get()
    size = int(entryPsw.get())
    # print(bukvi)
    a = random.sample(bukvi, size)
    # print(a)
    soedinenie = ''.join(a[0:])
    # print(soedinenie)

    with open("password.txt", 'a') as file:
        file.write(f'{name}: {soedinenie}\n')
    messagebox.showinfo('bmi-pythonguides', f"Ваш пароль:{soedinenie}\nбыл добавлен в текстовый файл -> {file.name} ")

def pin_pin():
    what_pin = pin_nameEntry.get()
    size_pin = int(entryPin.get())
    if size_pin < 4 or size_pin > 8:
        messagebox.showerror('bmi-pythonguides', f"Размер пин-кода должен составлять от 4 до 8 (Ваш пин-код составляет: {size_pin} цифр)")
    else:
        random_pin = random.sample(tsifri, size_pin)
        soed_pin = ''.join(random_pin[0:])
        with open("password.txt", 'a') as fpin:
            fpin.write(f'{what_pin}: {soed_pin}\n')
        messagebox.showinfo('bmi-pythonguides', f"Ваш пин-код: {soed_pin}\nбыл добавлен в текстовый файл -> {fpin.name} ")

window = tk.Tk()
window.title("Генератор паролей")
window.geometry('500x400')

frame = Frame(window, padx = 10, pady = 10)
frame.pack(expand=True)

sots = Label(frame, text='''Для какой 
соц.сети/аккаунта пароль: ''', font="10")
sots.grid(row=1, column=1)
passw = Label(frame, text='''Какой размер пароля 
вы хотите создать: ''', font="10")
passw.grid(row=2, column=1)

entrySots = Entry(frame, width=15)
entrySots.grid(row=1, column=2)

entryPsw = Entry(frame, width=15)
entryPsw.grid(row=2, column=2)

btn = Button(frame, text='Создать', command=parol)
btn.grid(row=3, column=2)

metkaPin = Label(frame, text='''*Отдельное создание пинкода*''', font="10")
metkaPin.grid(row=4, column=1)

pin_name = Label(frame, text='''Для чего вам нужен пин: ''', font="10")
pin_name.grid(row=5, column=1)

pin_nameEntry = Entry(frame, width=15)
pin_nameEntry.grid(row=5, column=2)

pincode = Label(frame, text='''Какой размерности пинкод 
вы хотите создать: ''', font="10")
pincode.grid(row=6, column=1)

entryPin = Entry(frame, width=15)
entryPin.grid(row=6, column=2)

btnPin = Button(frame, text='Создать', command=pin_pin)
btnPin.grid(row=7, column=2)

window.mainloop()