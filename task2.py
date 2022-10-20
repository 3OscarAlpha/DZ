#Считать названия объектов, даты и звездные величины из файла.
#Вывести на экран имена объетов, присутствующих в каталоге (без дублей!!!) и фильтров,
#в которых есть данные для тех или иных объектов.
#Попросить пользователя ввести имя объекта, данные для которого он хочет получить и названия фильтров,
#данные в которых нужны (возможно введение нескольких фильтров).
#Сохранить данные в формате: 1й столбец дата в формате число.месяц.год_пробел_время наблюдения,
#2й столбец - дата в форме юлианских дней, 3й и последующие столбцы - звездные величины в разных фильтрах.
#Столбцы разделять знаком табуляции. Сохранение данных произвести в файл с названием _имя объекта_.dat
#Все столбцы сверху должны быть подписаны. Данные должны быть отсортированы в порядке возрастания даты наблюдения.

import numpy as np #сначала терминал - pip install имя пакета.
import scipy
with open ('task2_data.dat', 'r') as f:  #здесь заменяем опечатки
  old_data = f.read()
new_data = old_data.replace('su hor', 'SU_Hor')
new_data = old_data.replace('SU Hor', 'SU_Hor')
new_data = old_data.replace("RZ Lyr", 'RZ_Lyr')
new_data = old_data.replace("rzlyr", 'RZ_Lyr')
new_data = old_data.replace("RZLyr", 'RZ_Lyr')
with open ('task2_data.dat', 'w') as f:
  f.write(new_data)


f = open('task2_data.dat', 'r')
line_table = f.readlines() #в список закидываем значения из файла. состоит из строк

column_obj = [] #создадим пока пустой список, куда загрузим названия
column_filt = []
for line in line_table:
    column_obj.append(line.split("   ")[0]) #делим посимвольно, вычленяем нулевые объекты,
                                            # выгружаем их в пустой список
    column_filt.append(line.split("    ")[2])
del column_obj[0]
del column_filt[0]
column_filt = [x.strip(' ') for x in column_filt] #убрала пробелы вида '  V'
f.close()
print('objects:', column_obj)
print('filters:', column_filt)



#избавимся от дубликатов:       обширный метод))
column_obj_norm = []
for i in column_obj:
    if i not in column_obj_norm:
        column_obj_norm.append(i)
print("Названия без дубликатов = ", column_obj_norm) #ints_list = [1, 2, 3, 4, 3, 2] ints_list1 = list(set(ints_list)) print(ints_list1) # [1, 2, 3, 4]


#Поделим все фильтры на два списка.
k = 0
for w in range (0, len(column_obj)):
    if column_obj[w] == "SU_Hor":
        k = k + 1
print(f"последний элемент SU_Hor находится на {k} позиции. Начиная с {k+1} идут RZ_Lyr")

su_hor_filters = list(set(column_filt[:k]))#избавляемся от дубликатов более простым сп. сет - пер в набор, лист - в список
rz_lyr_filters = sorted(list(set(column_filt[k:])), key=str.lower) #ААААААААААА КАК ИЗБАВИТЬСЯ ОТ ДУБЛИКАТОВ В ИНОМ РЕГИСТРЕ
# сейчас будем избавляться от дубликатов разного регистра
# dict = {1: su_hor_filters, 2: rz_lyr_filters}
# new_dict = sorted(, key=str.lower)
print(su_hor_filters, "в этих фильтрах su_hor")
print(rz_lyr_filters, "в этих фильтрах rz_lyr")

# catalog = list(zip(su_hor_filters, rz_lyr_filters))
# print(catalog) КАКАЯ-ТО МУТЬ
catalog = [column_obj_norm, [su_hor_filters, rz_lyr_filters]]
print(catalog)

#
# a = input('пж введите имя объекта и названия фильтров в формате')
# print(a)
#
# new_file = open('task2_data_resaved', 'w')

jdn = float(input('пж введите юлианскую дату'))
a = jdn + 32004
b = (4*a + 3) / 146097
c = a - (146097*b/4)
d = (4*c + 3)/1461
e = c - (1461*d/4)
m = (5*e + 2)/153
day = e - (153*m+2)/5 + 1
month = m + 3 - 12*(m/10)
year = 100*b + d - 4800 + (m/10)
print(f"the date is {day} {month} {year}")