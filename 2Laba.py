import control.matlab as matlab
import matplotlib.pyplot as pyplot
import numpy as numpy
from sympy import *
import control
import math
# ввод исходных данных

choiseOS = True
while choiseOS:
    userInput = input ("Bведите номер нужной обратной связи: \n"
                      "1 - Жесткая обратная связь \n"
                      "2 - Гибкая обратная связь \n"
                      "3 - Апериодическая жесткая обратаная связь\n"
                      "4 - апериодически гибкая обратная связь. \n")
    if userInput.isdigit():
        choiseOS = False
        userInput = int(userInput)
        if userInput == 1:
            os = True
            while os:
                print("Bведите исходные данные ")
                kos = input("Kos = ")
                if kos.replace('.', '', 1).isdigit():
                    kos = float(kos)
                    wos = matlab.tf([kos], [1])
                    os = False
                    asa = 1
                else:
                   print("Bведите допустимое значение! ")
        elif userInput == 2:
            os = True
            while os:
                print("Bведите исходные данные ")
                kos = input("Kos = ")
                if kos.replace('.', '', 1).isdigit():
                    kos = float(kos)
                    wos = matlab.tf([kos, 0], [1])
                    os = False
                    asa = 2
                else:
                   print("Bведите допустимое значение! ")
        elif userInput == 3:
            os = True
            while os:
                print("Bведите исходные данные")
                kos = input("Kos = ")
                tos = input("Tos = ")
                if kos.replace('.', '', 1).isdigit() and tos.replace('.','', 1).isdigit():
                    kos = float(kos)
                    tos = float(tos)
                    wos = matlab.tf([kos], [tos, 1])
                    os = False
                    asa = 3
                else:
                   print("Bведите допустимое значение! ")
        elif userInput == 4:
            os = True
            while os:
                print("Bведите исходные данные")
                kos = input("Kos = ")
                tos = input("Tos = ")
                if kos.replace('.', '', 1).isdigit() and tos.replace('.', '', 1).isdigit():
                    kos = float(kos)
                    tos = float(tos)
                    wos = matlab.tf([kos, 0], [tos, 1])
                    os = False
                    asa = 4
                else:
                    print("Bведите допустимое значение! ")
        else:
            print("Bведите допустимое значение ! ")
            choiseOS = True
    else:
            print("Bведите допустимое значение! ")
wl = wos
print(wl)

w2 = True
while w2:
    print("Bведите исходные данные ")
    tg = input("Tg = ")
    if tg.replace('.', '', 1).isdigit():
        tg = float(tg)
        wg = matlab.tf([1], [tg, 1])

        w2 = False
    else:
        print("Bведите допустимое значение! ")

w2 = wg
print(w2)
choiseTurbine = True
while choiseTurbine:
    userInput = input("Введите номер нужной турбины: \n"
                      "1 - Гидравлическая турбина \n"
                      "2 - Паровая турбина \n")

    if userInput.isdigit():
        choiseTurbine = False
        userInput = int(userInput)
        if userInput == 1:
            turbine = True
            while turbine:
                print("Введите исходные данные")
                tgt = input("Tgt = ")
                tg = input("Tg = ")
                if tgt.replace('.', '', 1).isdigit() and tg.replace('.', '', 1).isdigit():
                    tgt = float(tgt)
                    tg = float(tg)
                    wt = matlab.tf([0.01 * tgt, 1], [0.05 * tg, 1])
                    turbine = False
                else:
                    print("Bведите допустимое значение! ")

        elif userInput == 2:
            turbine = True
            while turbine:
                print("Введите исходные данные")
                kpt = input("Kpt = ")
                tpt = input("Tpt = ")
                if kpt.replace('.', '', 1).isdigit() and tpt.replace('.', '', 1).isdigit():
                    kpt = float(kpt)
                    tpt = float(tpt)
                    wt = matlab.tf([kpt], [tpt, 1])
                    turbine = False
                else:
                    print("Bведите допустимое значение!")
        else:
            print('Bведите допустимое значение! ')
            choiseTurbine = True
    else:
        print("Bведите допустимое значение! ")




w3 = wt
print(w3)

w4 = True
while w4:
    print("Bведите исходные данные ")
    ky = input("Ky = ")
    ty = input("Ty = ")
    if ky.replace('.', '', 1).isdigit() and ty.replace('.', '', 1).isdigit ():
        ky = float(ky)
        ty = float(ty)
        wy = matlab.tf([ky], [ty, 1])
        w4 = False
    else:
        print("Bведите допустимое значение! ")

w4 = wy
print(w4)







# Обозначаем коэфф. для ПИД регулятора
Kp = input('Введите коэф. Кр для ПИД регулятора')
Ki = input('Введите коэф. Кр для ПИД регулятора')
Kd = input('Введите коэф. Кр для ПИД регулятора')

Wp = control.tf([Kp], [1])
print(Wp)
Wi = control.tf([Ki], [1, 0])
print(Wi)
Wd = control.tf([Kd, 0], [1])
print(Wd)

Wpid = control.parallel(Wp, Wi, Wd)
print(Wpid)

w5 = w2 * w3 * w4
Wposl_pid = control.series(Wpid, w5)
print(Wposl_pid)

Wsum_pid = control.feedback(Wposl_pid, wl)
print(Wsum_pid)




# Задаем размкнутую передаточную функцию
print("Paзомкнутая передаточная функция")

w55 = matlab.series(Wpid, w5)
print(w55)

# Задаем замкнутую передаточную функцию
print("Замкнутая передаточная функция")
w = matlab.feedback(Wposl_pid, wl)
print(w)

time = []
for i in range(0, 2500):
    time.append(i / 100)





# Строим переходную характеристику
pyplot.subplot()
pyplot.grid(True)
[y, x] = matlab.step(Wsum_pid, time)
pyplot.plot(x, y)
pyplot.title("Переходна характеристика")
pyplot.ylabel('Амплитуда')
pyplot.xlabel('Bpeмя')
pyplot.show()

# находим корни характеристичкского уравнения и определяем устойчивость системы
korny = matlab.pzmap(Wposl_pid)
pyplot.axis([-3, 1, -1, 1])
pyplot.show()
pole = matlab.pole(Wposl_pid)
print(pole)
deistv = []
for i in pole:
    kx = i.real
    deistv.append(kx)
if (min(deistv) > 0.0001):
    print("система неустйочива по корням характеристического уравнения")
elif (max(deistv) < -0.0001):
    print("cистема устойчива по корням характеристического уравнения")
else:
    print("система на границе устойчивости")


# Построение Диаграммы Найквиста и ЛУХ
def graph(title):
    pyplot.subplot()
    pyplot.grid(True)
    if title == "Диаграмма Найквиста":
        nyquist = matlab.nyquist(w55)
        pyplot.title(title)
        pyplot.xlabel("Re")
        pyplot.ylabel("Im")
        pyplot.axis([-5, 20, -15, 5])
        pyplot.plot()

    elif title == "Логорифмические характеристики":
        mag, phase, omega = matlab.bode(w55)
        pyplot.plot()

graph("Диаграмма Найквиста")
pyplot.show()

graph("Логорифмические характеристики")
pyplot.show()

# Построение годогрофа Михайлова
v = symbols('v', real=True)  # равно омего
koef = w.den                 # создаем массиф козффициентов знаменателя
a = 1
uravnenie = 0
pole = []

for i in koef[0]:
    for b in i:
        n = len(i) - a # показатель степени (n-1)
        uravnenie = uravnenie + b * (I * v) ** n
        a = a + 1
        pole.append(b)
print(uravnenie)  # итоговое уравнение после замены переменной
wr = re(uravnenie)
wm = im(uravnenie)
print("Действительная часть = ", wr)
print("Mнимая часть = ", wm)
x = [wr.subs({v: q}) for q in numpy.arange(0, 100, 0.1)]
y = [wm.subs({v: q}) for q in numpy.arange(0, 100, 0.1)]
pyplot.axis([-40, 25, -10, 10])
pyplot.plot(x, y)
pyplot.grid(True)
pyplot.show()

# Определение предельного значения козффициента обратной связи

for kockrit in numpy.arange(0, 5, 0.001):
    if (asa == 1):
        koc = matlab.tf([kockrit], [1])
    elif (asa - 2):
        koc = matlab.tf([kockrit, 0], [1])
    elif (asa - 3):
        koc = matlab.tf([kockrit], [tos, 1])
    elif (asa - 4):
        koc = matlab.tf([kockrit, 0], [tos, 1])
    wo = matlab.feedback(w5, koc)
    koef = wo.den[0][0]
    position = {}
    nomer = len(koef)
    for j in range(nomer):
        position["%s" % j] = koef[j]
    matrix = numpy.array([[position["1"], position["3"]], [position["0"], position["2"]]])

    if (numpy.linalg.det(matrix) >= -0.1) & (numpy.linalg.det(matrix) <=0.1):
        print(matrix)
        print("пределитель =", numpy.linalg.det(matrix))
        print("предельное значение", kockrit)
        kocitog = kockrit

# Производим экспериментальную проверку предельного значения коэффициента

os = kocitog
if (asa == 1):
    wockrit = matlab.tf([os], [1])
elif (asa == 2):
    wockrit = matlab.tf([kocitog, 0], [1])
elif (asa == 3):
    wockrit = matlab.tf([kocitog], [tos, 1])
elif (asa == 4):
    wockrit = matlab.tf([kocitog, 0], [tos, 1])
w = matlab.feedback(w5, wockrit)
print("Pазомкнутая передаточная функция")
wraz = matlab.series(w3, w4, w2, wockrit)
print(wraz)
print("Замкнутая передаточная функция")
print(w)

pyplot.subplot()
pyplot.grid(True)
[y, x] = matlab.step(w, time)

pyplot.plot(x, y)
pyplot.title("Переходная характеристика")
pyplot.ylabel('Амплитуда')
pyplot.xlabel('Bpeмя')
pyplot.show()

korny = matlab.pzmap(w)
pyplot.axis([-3, 1, -1, 1])
pyplot.show()
pole = matlab.pole(w)
print(pole)
deistv = []
for i in pole:
    kx = i.real
    deistv.append(kx)
if (min(deistv) > 0.0001):
    print("cистема неустйочива по корням характеристического уравнения")
elif (max(deistv) < -0.0001):
    print("система устойчива по корням характеристического уравнения")
else:
    print ("cистема на границе устойчивости")

def graph(title):
    pyplot.subplot()
    pyplot.grid(True)
    if title == "Диаграмма найквеста":
         nyquist = matlab.nyquist(wraz)
         pyplot.title(title)
         pyplot.xlabel("Re")
         pyplot.ylabel("Im")
         pyplot.axis([-10, 40, -25, 5])
         pyplot.plot()

    elif title == "Логорифмические характеристики":
         mag, phase, omega = matlab.bode(wraz)
         pyplot.plot()

graph("Диаграмма найквеста")
pyplot.show()

graph("Логорифмические характеристики")
pyplot.show()

koef = w.den  #создаем массив коэффициентов знаменателя
a = 1
uravnenie = 0
pole = []

for i in koef[0]:
    for b in i:
        n = len(i) - a  #показатель степени (n-1)
        uravnenie = uravnenie + b * (I * v) ** n  #замена р на jw
        a = a + 1
        pole.append(b)
print(uravnenie) # итоговое уравнение после замены переменной

wr = re(uravnenie)
Wm = im(uravnenie)
print("Действительная часть = ", wr)
print("Mнимая часть = ", wm)
x = [wr.subs({v: q}) for q in numpy.arange (0, 100, 0.1)]
y = [wm.subs({v: q}) for q in numpy.arange (0, 100, 0.1)]
pyplot.axis([-40, 40, -20, 10])
pyplot.plot(x, y)
pyplot.grid(True)
pyplot.show()
#

