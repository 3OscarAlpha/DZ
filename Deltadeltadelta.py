import numpy as np
#Предварительно очистим файлы с содержимым каталогов от доп информации в начале
# Убираю Д
with open ('icrf2-all.txt', 'r') as f:
    old_data = f.read()
    new_data = old_data.replace('D', ' ')
with open ('icrf2-all.txt', 'w') as f:
  f.write(new_data)
with open ('icrf3sx.txt', 'r') as f:
    old_data = f.read()
    new_data = old_data.replace('D', ' ')
with open ('icrf3sx.txt', 'w') as f:
  f.write(new_data)

rf2 = open('icrf2-all.txt', 'r')
rf3 = open('icrf3sx.txt', 'r')

icrf2 = rf2.readlines() #в список закинули значения из файла. один элемент - одна строка файла
icrf3 = rf3.readlines()

column_ident2, ra2, dec2, delta_ra2, delta_dec2, temp = [], [], [], [], [], []
for line in icrf2:
    column_ident2.append(line.split(" ")[1]) #идентификаторы
    ra2.append(line.split(' ')[8:11])
    dec2.append(line.split('  ')[4])
    temp.append((line.split('  ')[5]).split())
del column_ident2[0:3], ra2[0:3], dec2[0:3], temp[0:3]
for i in range(0, len(temp)):
    delta_ra2.append(temp[i][0])
    delta_dec2.append(temp[i][1])

#то ж самое для третьего кат
column_ident3, ra3, dec3, delta_ra3_temp, delta_dec3, temp = [], [], [], [], [], []
for line in icrf3:
    column_ident3.append(line.split(" ")[1])
    ra3.append(line.split(' ')[12:15])
    dec3.append(line.split('    ')[3])
    delta_ra3_temp.append((line.split('    ')[4]).split())
    temp.append((line.split('    ')[5]).split())
del column_ident3[0:3], ra3[0:3], dec3[0:3], delta_ra3_temp[0:3], temp[0:3]
for i in range(0, len(temp)):
    delta_dec3.append(temp[i][0])
delta_ra3 = []
for i in range (0, len(delta_ra3_temp)):
    delta_ra3.append(delta_ra3_temp[i][0])

# разборки с прямым восх и скл. надо будет сделать функицю..
for i in range (0, len(ra2)):
        ra2[i] = float(ra2[i][0])*60*60+float(ra2[i][1])*60+float(ra2[i][2])
        dec2[i] = dec2[i].split()
        if float(dec2[i][0])>=0:
            dec2[i] = float(dec2[i][0])*60*60+float(dec2[i][1])*60+float(dec2[i][2])
        else:
            dec2[i] = -(float(dec2[i][0]) * (-60) * 60 + float(dec2[i][1]) * 60 + float(dec2[i][2]))
for i in range (0, len(ra3)):
        ra3[i] = float(ra3[i][0])*60*60+float(ra3[i][1])*60+float(ra3[i][2])
        dec3[i] = dec3[i].split()
        if float(dec3[i][0])>=0:
            dec3[i] = float(dec3[i][0])*60*60+float(dec3[i][1])*60+float(dec3[i][2])
        else:
            dec3[i] = -(float(dec3[i][0]) * (-60) * 60 + float(dec3[i][1]) * 60 + float(dec3[i][2]))

f2, f3 = [], []
a0, a1, a2, a3, a4 = [], [], [], [], []
b0, b1, b2, b3, b4 = [], [], [], [], []
for i in range(0, len(column_ident2)):
    for j in range(0, len(column_ident3)):
        if column_ident2[i] == column_ident3[j]:
            a0.append(column_ident2[i])
            b0.append(column_ident3[j])
            a1.append(ra2[i]), a2.append(float(delta_ra2[i])), a3.append(dec2[i]), a4.append(float(delta_dec2[i]))
            b1.append(ra3[j]), b2.append(float(delta_ra3[j])), b3.append(dec3[j]), b4.append(float(delta_dec3[j]))
f2.append(a0), f2.append(a1), f2.append(a2), f2.append(a3), f2.append(a4) #0-имя 1-првосх 2-откл првосх 3-скл 4-октл скл
f3.append(b0), f3.append(b1), f3.append(b2), f3.append(b3), f3.append(b4)
#Теперь необходимые данные для общих источников хранятся в списках ф2, ф3

#Посчитаем отклонения RA и Dec с учетом неопределенностей
d0_a, d0_d = [], []
for i in range(0, len(a0)):
    d0_a.append(np.sqrt(((f3[1][i]-f2[1][i])**2)+float(f2[2][i])**2+float(f3[2][i])**2))
    d0_d.append(np.sqrt(((f3[3][i]-f2[3][i])**2)+float(f2[4][i])**2+float(f3[4][i])**2))
# Посчитаем ошибки нуль-пунктов
d_A, d_D = 0, 0
for i in range(0, len(a0)):
    d_A += d0_a[i]
    d_D = d_D+d0_d[i]
d_A = d_A/len(a0) #0.000344
d_D = d_D/len(a0) #0.009913
print('d_A =', d_A, ', d_D =', d_D)
# Внесем поправки за нуль-пункт в отклонения
d1_a, d1_d = [], []
for i in range (0, len(a0)):
    d1_a.append(np.abs(d0_a[i]-d_A))
    d1_d.append(abs(d0_d[i] - d_D))
# Поделить на 360 зон по пр восх
d2_a, d2_d = [], []
start = 0
for a in range (0, 360): # наверное стоило сделать проще, чтобы быстрее обрабатывалось. мысли: новый файл и туда уже разбитые по зонам, либо неравенство
    temp_M_a, temp_M_d = [], [] #сюда будем закидывать значения для одной конкретной i-ой зоны
    sum_d1_a, sum_d1_d = 0, 0
    for j in range (start, len(a0)):
        if float(f2[1][j]) >= 240 * a and float(f2[1][j]) < (240*(a+1)):
            temp_M_a.append(d1_a[j])
            temp_M_d.append(d1_d[j])
        elif float(f2[1][j]) >= (240*(a+1)): break
    for k in range(0, len(temp_M_a)):
        sum_d1_a += temp_M_a[k]
        sum_d1_d += temp_M_d[k]
    if len(temp_M_a) == 0: continue
    d_a_a = 1/len(temp_M_a)*sum_d1_a
    d_d_a = 1/len(temp_M_d)*sum_d1_d
    for i in range(0, len(temp_M_a)):
        d2_a.append(np.abs(temp_M_a[i]-d_a_a))
        d2_d.append(np.abs(temp_M_d[i]-d_d_a))
    start += len(temp_M_a)

for a in range (0, 360):
    temp_M_a, temp_M_d = [], []
    sum_d1_a, sum_d1_d = 0, 0
    for j in range (start, len(a0)):
        if float(f2[1][j]) >= 240 * a and float(f2[1][j]) < (240*(a+1)):
            temp_M_a.append(d1_a[j])
            temp_M_d.append(d1_d[j])
        elif float(f2[1][j]) >= (240*(a+1)): break
    for k in range(0, len(temp_M_a)):
        sum_d1_a += temp_M_a[k]
        sum_d1_d += temp_M_d[k]
    if len(temp_M_a) == 0: continue
    d_a_a = 1/len(temp_M_a)*sum_d1_a
    d_d_a = 1/len(temp_M_d)*sum_d1_d
    for i in range(0, len(temp_M_a)):
        d2_a.append(np.abs(temp_M_a[i]-d_a_a))
        d2_d.append(np.abs(temp_M_d[i]-d_d_a))
    start += len(temp_M_a)

d3_a, d3_d = [], []
for d in range (-90, 90):
    temp_M_a, temp_M_d = [], []
    sum_d2_a, sum_d2_d = 0, 0
    for j in range (0, len(a0)):
        if float(f2[3][j])> (3600*d) and float(f2[3][j])<=(3600*(d+1)):
            temp_M_a.append(d2_a[j])
            temp_M_d.append(d2_d[j])
    for k in range(0, len(temp_M_a)):
        sum_d2_a += temp_M_a[k]
        sum_d2_d += temp_M_d[k]
    if len(temp_M_a) == 0: continue
    d_a_d = 1/len(temp_M_a)*sum_d2_a
    d_d_d = 1/len(temp_M_d)*sum_d2_d
    for i in range(0, len(temp_M_a)):
        d3_a.append(np.abs(temp_M_a[i]-d_a_d))
        d3_d.append(np.abs(temp_M_d[i]-d_d_d))

# print(len(d2_a), len(d3_a))
sum_d3_a, sum_d3_d = 0, 0
for i in range (0, len(d3_a)):
    sum_d3_a += d3_a[i]
    sum_d3_d += d3_d[i]
ksi_a = 1/len(d3_a)*sum_d3_a
ksi_d = 1/len(d3_a)*sum_d3_d
print("ksi_a =", ksi_a, ", ksi_d =", ksi_d)