import astropy.io.fits as pyfits
import astropy
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import *
import pylab #для xlim
from tkinter import scrolledtext
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# def get_text():
#     s = entry.get(1.0, END)
#     label['text'] = s

def click():
    global scidata, fig # X=730, Y=1890
    global сoord_x, coord_y, r_of_star
    global left_x, left_y, right_x, right_y
    source = entr1.get() #C:/Users/3512/Downloads/Telegram Desktop/v523cas60s-001.fit
    coord_x = entr2.get()
    coord_y = entr3.get()
    r_of_star = entr4.get()
    r1_back = float(entr5.get())
    r2_back = float(entr6.get())
    hdulist = pyfits.open(f"{source}")
    hdulist.info()
    scidata = hdulist[0].data
    hdulist.close()

    left_x = int(coord_x) - int(r_of_star)
    right_x = int(coord_x) + int(r_of_star)
    left_y = int(coord_y) - int(r_of_star)
    right_y = int(coord_y) + int(r_of_star)

    def ver_plot():
        # damn = [row[730] for row in scidata]
        damn = [row[int(coord_x)] for row in scidata]
        ver_Y = damn[left_y:right_y]
        ver_X = [i for i in range(left_y, right_y)]

        fig = Figure(figsize=(5, 5), dpi=70)
        plot1 = fig.add_subplot(111)
        plot1.plot(ver_X, ver_Y)
        plot1.set_xlim([left_y, right_y])
        canvas = FigureCanvasTkAgg(fig, master=star_window)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1, row =7)


    def hor_plot():  # профиль горизонтальный (y const)
        hor_X = [i for i in range(left_x, right_x)]
        hor_Y = scidata[int(coord_y)][int(left_x):int(right_x)]
        fig = Figure(figsize=(5,5), dpi=70)
        plot1 = fig.add_subplot(111)
        plot1.plot(hor_X, hor_Y)
        canvas = FigureCanvasTkAgg(fig, master=star_window)
        canvas.draw()
        canvas.get_tk_widget().grid(column=2, row =7)

    def d_plot():
        z_temp, Z = [], []
        i = left_y
        while i < right_y:
            for k in range(left_x, right_x):
                z_temp.append(scidata[i][k]) #type = list
            z_arr = np.asarray(z_temp, dtype=int) #type = ndarray
            Z.append(z_arr)
            z_temp = []
            i = i + 1
        Z = np.asarray(Z)

        x = [i for i in range(left_x, right_x)]
        y = [i for i in range(left_y, right_y)]
        X, Y = np.meshgrid(x, y)
        fig = plt.Figure(figsize=(5,5), dpi=70)
        # ax = plt.axes(projection='3d') #scatters
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='inferno')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        canvas = FigureCanvasTkAgg(fig, master=star_window)
        canvas.draw()
        canvas.get_tk_widget().grid(column=3, row =7)


    var1, var2, var3 = IntVar(), IntVar(), IntVar()
    var1.set(1)
    c1 = Checkbutton(star_window, text='Vertical',
                     variable=var1, onvalue=1, offvalue=0,
                     command=ver_plot)
    c1.grid(column=1, row=6)

    var2.set(2)
    c2 = Checkbutton(star_window, text='Horizontal',
                     variable=var2, onvalue=1, offvalue=0,
                     command=hor_plot)
    c2.grid(column=2, row=6)

    var3.set(3)
    c3 = Checkbutton(star_window, text='3d',
                     variable=var3, onvalue=1, offvalue=0,
                     command=d_plot)
    c3.grid(column=3, row=6)


star_window = tk.Tk()
star_window.title(f"Взлом мира")
star_window.geometry('1400x800') #почему не в юнитах выдает?


lbl1 = Label(text='Vvedite puuuuut')
lbl1.grid(column = 1, row = 1)
entr1 = Entry(text = 'Vvedite put', bg='black', fg = 'white', width = 60)
entr1.grid(column = 2, row = 1)
entr1.insert(0, "C:/Users/3512/Downloads/Telegram Desktop/v523cas60s-001.fit")

lbl2 = Label(text='X')
lbl2.grid(column = 1, row = 2)
entr2 = Entry(width = 25)
entr2.grid(row = 2, column = 2)
entr2.insert(0, '730')

lbl3 = Label(text='Y')
lbl3.grid(column = 1, row = 3)
entr3 = Entry(width = 25)
entr3.grid(row = 3, column = 2)
entr3.insert(0, '1891')

lbl4 = Label(text='R of star')
lbl4.grid(column = 3, row = 2)
entr4 = Entry(width = 25)
entr4.grid(row = 2, column = 4)
entr4.insert(0, '8')

lbl5 = Label(text='R of back1')
lbl5.grid(column = 3, row = 3)
entr5 = Entry(width = 25)
entr5.grid(row = 3, column = 4)
entr5.insert(0, '5')

lbl6 = Label(text='R of back2')
lbl6.grid(column = 3, row = 4)
entr6 = Entry(width = 25)
entr6.grid(row = 4, column = 4)
entr6.insert(0, '6')



btn = Button(star_window, text="Принять", command=click)
btn.grid(row = 5, column = 1)


star_window.mainloop()