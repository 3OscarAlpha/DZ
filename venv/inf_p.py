import math
# x = math.log(8, 2) - возвращает 3
a = float(input('Введите число а')) #float - дробные числа
b = float(input('Введите число b'))
c = float(input('Введите число c'))
if a>0:
    if a != 1:
        D = b**2+4*c #вычисление дискриминанта
        if D>= 0:
            t_1 = (b+math.sqrt(b**2+4*c))/2 #sqrt - вычисление корня
            if t_1 > 0:
                x_1 = math.log(t_1, a) #логарифм от числа t_1 по основанию а
                print(f'x1 = {x_1}') #выводим на экран вычисленный логарифм
                print('Подставим х1:', a**(2*x_1)-b*a**x_1-c, ' = 0')
            t_2 = (b-math.sqrt(b**2+4*c))/2
            if t_2 > 0:
                x_2 = math.log(t_2, a)
                print(f'x2 = {x_2}')
                print('Подставим х2:', a**(2*x_2)-b*a**x_2-c, ' = 0')
        else:
            print('Корней нет')
    else:
        print('x - любое')
else:
    print('Логарифм не определен при a<=0')

