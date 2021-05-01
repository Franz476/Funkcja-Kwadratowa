import sys
import math
import numpy as np
import matplotlib as mplt
import matplotlib.pyplot as plt

a = 0
b = 0
c = 0

#print(str(a) + " " + str(b) + " " + str(c))
print('Pamiętaj, aby liczby z ułamkiem zapisywać za pomocą kropki ".", a nie przecinka ",". Gdy liczba nie ma części ułamkowej, to nie musisz się o to martwić.')

def sprawdz_typ(wartosc):
    try:
        val = float(wartosc)
        print("Prawidłowo wprowadzona wartość. Wynosi ona: ", val)

    except ValueError:
        print("Wprowadzono nieprawidłowy typ zmiennej.")
        sys.exit(0)


a=input('Wpisz wartość współczynnika "a": ')
sprawdz_typ(a)

if float(a) == 0:
    print('Współczynnik "a" nie może być równy 0.')
    sys.exit(0)

b=input('Wpisz wartość współczynnika "b": ')
sprawdz_typ(b)

c=input('Wpisz wartość współczynnika "c": ')
sprawdz_typ(c)

print(str(a) + " " + str(b) + " " + str(c))

a_print = str(a)
plus_znak = "+"

if float(b) >= 0:
    b_print = plus_znak + str(b)
else:
    b_print = str(b)

if float(c) >= 0:
    c_print = plus_znak + str(c)
else:
    c_print = str(c)


print('Twoja funkcja ma postać: ' + a_print + 'x^2' + b_print + 'x' + c_print)

delta = float(b) * float(b) - 4 * float(a) * float(c)
delta_sqrt = math.sqrt(delta)
print('Delta wynosi: ' + str(delta_sqrt))

if delta < 0:
    print('Delta wyniosła: ' + str(delta) + ', wiec dana funkcja nie ma rozwiązań w dziedzinie liczb rzeczywistych.')
elif delta == 0:
    x0 = ((-1) * float(b)) / (2 * float(a))
    print('Delta wyniosła dokładnie 0. Miejsce zerowe znajduje się w punkcie x0 = ' + str(x0))
else:
    x1 = ((-1.0) * float(b) - delta_sqrt) / (2 * float(a))
    x2 = ((-1.0) * float(b) + delta_sqrt) / (2 * float(a))
    print('Delta wyniosła: ' + str(delta_sqrt) +', więc ma 2 miejsca zerowe w dziedzinie liczb rzeczywistych i wynoszą one: x1 = ' + str(x1) + ', oraz x2 = ' + str(x2))


x = np.linspace(-10,10,500)
y = (float(a)*(x*x)) + (float(b)*x) + float(c)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y, 'g')


plt.show()

end=input('Wciśnij dowolny przycisk, aby zakończyć')