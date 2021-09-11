import colorama as color
import control.matlab as matlab
import matplotlib.pyplot as pyplot

def choise():
    inertialessUnitName = "Безынерционное звено"
    aperiodicUnitName = "Апериодическое звено"

    needNewChoice = True
    while needNewChoice:
        print(color.Style.RESET_ALL)
        userInput = input('Введите номер команды: \n'
                          '1 - ' + inertialessUnitName + ';\n'
                          '2 - ' + aperiodicUnitName + '.\n')

        if userInput.isdigit():
            userInput = int(userInput)
            needNewChoice = False
            if userInput == 1:
                name = 'Безынерционное звено'
            elif userInput == 2:
                name = 'Апериодическое звено'
            else:
                print(color.Fore.RED + '\nНедопустимое значение!')
                needNewChoice = True
        else:
            print(color.Fore.RED + '\nПожалуйста, введите числовое значение!')
            needNewChoice = True
    return name

def getUnit(name):
    needNewChoice = True
    while needNewChoice:
        print(color.Style.RESET_ALL)
        needNewChoice = False
        k = input('пожалуйста,введите коэффециент "k": ')
        t = input('пожалуйста,введите коэффециент "t": ')
        if k.isdigit() and t.isdigit():
            k = int(k)
            t = int(t)
            if name == "Безынерционное звено":
                unit = matlab.tf([k], [1])
            elif name == "Апериодическое звено":
                unit = matlab.tf([k],[t, 1])
        else:
            print(color.Fore.RED + '\nПожалуйста, введите числовое значение!')
            needNewChoice = True
    return unit

def graph(num, title, y, x):
    pyplot.subplot(2,1, num)
    pyplot.grid(True)
    if title == "Переходная характеристика":
        pyplot.plot(x, y, 'purple')
    elif title == 'Импульсная характеристика':
        pyplot.plot(x,y,"green")
    pyplot.title(title)
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('Время (с)')





unitName = choise()
unit = getUnit(unitName)


timeLine = []
for i in range(0,10000):
    timeLine.append(i/1000)

[y, x] = matlab.step(unit, timeLine)
graph(1, "Переходная характеристика", y, x)
[y, x] = matlab.impulse(unit, timeLine)
graph(2, "Импульсная характеристика", y, x)
pyplot.show()