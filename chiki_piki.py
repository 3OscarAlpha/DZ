# 1
# 1) Из файла catalog выбрать все данные для объекта введенного пользователем. 2) Создать интерфейс для программы (1 кнопка и 1 поле ввода)


import tkinter as tk
from tkinter import *
# Сначала посмотри то, что с 24 строки.
# Короче 1) это чисто второе задание со звездами
def click():
    # Открываем файл, закинем все значения из него в переменную f
    f = open('C:/Users/3512/Downloads/Telegram Desktop/catalog.txt', 'r') # r - режим для чтения
    lines_list = f.readlines() #в список под названием lines_list закидываем значения файла, деленные по строкам
    name_object = entr.get() #в эту переменную поместится введенный в окошко объект
    for i in range (0, len(lines_list)): #пробегаемся по каждой строке
        if name_object in lines_list[i]: #проверяем на наличие названия нужного нам объекта
            lbl2 = Label(text = f'Все данные для этого объекта: \n {lines_list[0]} \n {lines_list[i]}') #\n это чтобы на новую строку перенести.
                                        # lines_list[0] это заголовки
            lbl2.grid(column=1, row = 3)
    f.close()

# Создать интерфейс. Подгружаем пакет tkinter (в самом начале)
window = tk.Tk()
window.title("Данные из catalog.txt")
window.geometry('800x800')


lbl = Label(text='Введите имя объекта') #делаем надпись
lbl.grid(column = 1, row = 1) #с помощью грида размещаем

entr = Entry(width = 60) #делаем окно для ввода имени объекта
entr.grid(column = 2, row = 1)

btn = Button(window, text='Ok', command=click) # делаем кнопку, которая выполняет функцию click
btn.grid(column=2, row=2)

window.mainloop() #чтобы интерфейс появлялся
