import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *


def bam():
    jddate = entr1.get() #C:\Users\ivank\Desktop\tot
    file = open(f"{jddate}", "r")
    file_with_lines = file.readlines()
    # allall = []
    MJD = []
    for line in file_with_lines:
    # a = line.split(" ")
    # f_st = line.split(" ")[:1]
        MJD.append(line.split(" ")[0])  #смотрим где строка делится пробелом, вычленяем объекты с нулевым индексом,
        # выгружаем их в изначально пустой список MJD
        # иначе говоря:
        # m = line.split(' ')[0]
        # MJD.append(m)
    del MJD[0] #мешается падла
    # for i in range(0, len(MJD)):
    #     MJD[i] = float(MJD[i])
    datal = []
    for i in range (0, len(MJD)):
        hjd = float(MJD[i])
        hjd += 2400000
        jdn = int(hjd)
        time = hjd-jdn
        a = jdn + 32044
        b = (4 * a + 3) // 146097
        c = a - (146097 * b // 4)
        d = (4 * c + 3) // 1461
        e = c - (1461 * d) // 4
        m = (5 * e + 2) // 153
        # h = (jddate - jd)*24
        day = e - (153 * m + 2) // 5 + 1
        month = m + 3 - 12 * (m // 10)
        year = 100 * b + d - 4800 + (m // 10)

        h = time*24
        mins = (h - int(h)) * 60
        sec = (mins - int(mins)) * 60
        g_date = f'{day}.{month}.{year} {int(h)}:{int(mins)}:{int(sec)}'
        datal.append(g_date)
        # wiew = Label(f'{g_date}')
        # print(datal)
    lbl2 = Label(text = f'{datal}')
    lbl2.grid(row = 5, column = 1)
date_window = tk.Tk()
date_window.title(f"Перевод из JD в HD")
date_window.geometry('800x800')

lbl1 = Label(text='Введите путь к файлу')
lbl1.grid(column = 2, row = 2)

entr1 = Entry(bg='blue', fg = 'white', width = 60)
entr1.grid(column = 3, row = 2)
entr1.insert(0, 'C:/Users/3512/Downloads/Telegram Desktop/mon.dat')

bttn = Button(date_window, text="Принять", command=bam)
bttn.grid(row = 3, column = 1)

date_window.mainloop()