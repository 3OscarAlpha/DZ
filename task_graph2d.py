import astropy.io.fits as pyfits
import astropy
import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker

hdulist = pyfits.open("C:/Users/3512/Downloads/Telegram Desktop/v523cas60s-001.fit")
hdulist.info()
# hm = hdulist[0].header
# print(hm)
# exp = hdulist[0].header['exptime']
# print(exp)
# print(hdulist[0].header[:10])
scidata = hdulist[0].data
# print(scidata[0])

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
# plt.axis([724, 738, 1736, 36912])
# hor.title('Горизонтальный профиль', fontsize=20, fontname='times new roman', color='#822899')
# hor.xlabel('Координата Х', color='#00508a')
# hor.ylabel("Деления", color='#64659e')
# hor.legend(['Грэфик гор пр'], loc=0)
# plt.yaxis.set_minor_locator(ticker.MultipleLocator(1000))

plt.show()
hdulist.close()