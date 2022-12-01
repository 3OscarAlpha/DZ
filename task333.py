import astropy.io.fits as pyfits
import astropy
import matplotlib.pyplot as plt
import numpy
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox



def clicked():
    global words
    words = entry.get()
    print(words)
    return(words)

# def select():
#     lbl.configure(text=str(selected.get()))
# # #
# def mess():
#     messagebox.showinfo('Окно всплыло', 'Работает!')




# x_coord = float(input('Введите координату х: '))
# y_coord = float(input('Введите координату y: '))

x_coord = 730
y_coord = 1891

star_window = tk.Tk()
star_window.title(f"Star with x:{x_coord}, y:{y_coord}")
star_window.geometry('600x600') #почему не в юнитах выдает?

lbl = Label(star_window, text='Добро пожаловать в программу по взлому мира', foreground = 'white', background = 'black')
lbl.pack()

button = Button(text = 'Горизонтальный профиль', bg = 'grey') # width=25, height=5, bg="blue", fg="yellow"
button.pack()

entry = Entry(text = 'Vvedite put', bg='yellow', width = 50)
entry.pack()
btn = Button(star_window, text="Клик!", command=clicked)
btn.pack()

print(words)

#                    Построение графиков
hdulist = pyfits.open(f"{words}")
hdulist.info()
scidata = hdulist[0].data
fig = plt.figure()
ver = fig.add_subplot(1, 2, 1) #колво строк, столбцов, номер позиции
hor = fig.add_subplot(1, 2, 2)
# профиль вертикальный (x const)
damn = [row[730] for row in scidata]
print('damn = ', damn)
ver_y = damn[1875:1910]
ver_x = [i for i in range(1875, 1910)]
ver.set(title = 'Вертикальный профиль')
ver.plot(ver_x, ver_y)
#профиль горизонтальный (y const)
hor_x = [i for i in range(724, 738)]
hor_y = scidata[1891][724:738]
print(hor_x, hor_y)
hor.plot(hor_x, hor_y, color = '#8b00ff')
hor.set(title = 'Горизонтальный профиль')
plt.show()
hdulist.close()

star_window.mainloop()
#
# lbl = Label(star_window, text=f"Добрый день. Пожавуста укажите путь к файлу:", font=("Arial Bold", 10))
# lbl.grid(column=0, row=0)
# #
# txt = Entry(star_window, width=30)
# txt.grid(column=1, row=0)
# # print(name) #C:/Users/3512/Downloads/Telegram Desktop/v523cas60s-001.fit
#
#
# # source = name
# hdulist = pyfits.open("C:/Users/3512/Downloads/Telegram Desktop/v523cas60s-001.fit")
#
#
#
# # chk_state = IntVar()
# # chk_state.set(0)
# # chk = Checkbutton(star_window, text='Выбрать', var=chk_state)
# # chk.grid(column=1, row=0)
# # #
# # # btn = Button(window, text="Ок", command=y_or_n)
# # # btn.grid(column=1, row=2)
# # #
# # selected =IntVar()
# # rad1 = Radiobutton(star_window,text='a', value=1, variable=selected)
# # rad2 = Radiobutton(star_window, text='b', value=2, variable=selected)
# # rad3 = Radiobutton(star_window, text='c', value=3, variable=selected)
# # rad1.grid(column=3, row=0)
# # rad2.grid(column=3, row=1)
# # rad3.grid(column=3, row=2)
# # btn2 = Button(star_window, text="Select", command=select)
# # btn2.grid(column=3, row=3)
# # #
# # #
# # txt = scrolledtext.ScrolledText(star_window,width=40,height=10)
# # txt.insert(INSERT, 'Добрый день. Введите путь к файлу, поЖалУвуСта')
# # txt.grid(column=7, row=5)
#
# # btn3 = Button(star_window, text='Вызвать окно', command=mess)
# # btn3.grid(column=7, row=0)
