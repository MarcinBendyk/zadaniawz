import sys
import math
"""a = 2
b = 'lol'
c = 'h'
print(a)
print(type(c))
potega = a ** 10
print(potega)
f = potega // 2
print(f)
# funckja pow to drugi sposob na zrobienie potegi
# pow(a,10)
i = 6**1/2 # <-- tak nie robic jak ulamki to w nawias 6**(1/2)
j= pow(6,1/2)
print(i)
print(j)
suma = a + a
print(suma)
str1 = 'wizualizacja danych '
str2 = 'grupa '
grupa = 1
print(str1 + str2 + str(grupa))
print('co tam {} + {} = {}'.format(a,a,suma))
print('co tam {:.2f} + {:f} = {:d}'.format(a,a,suma))
a = input('wprowadz liczbe ')
print(int(a)*int(a))
sys.stdout.write('wprowadz b:')
print(b)
############################################################################
lista = [5,6.6,24,'a','b',[2,4,5],'trtrp']
print(lista)
lista.append(67)
print(lista)
lista.insert(2,34)
print(lista)
lista.reverse()



slownik = {'klucz':'wartosc', 1:2, 'a':3, }
print(slownik)
print(slownik['a'])
slownik.pop(1)
del slownik['a']

#instrukcja if else
a= 1
b = 3
if a>2:
    print(a)
elif a<b:
    print('yoo')
else:
    print('hh')
# if warunek & warunek2 <-- łączenie warunków oba musza byc spełnione
# if warunek | warunek2 <-- łączenie warunków tylko jeden wasrunek musi byc spełniony
for i in range(8):
    print(i)
else:
    print('koniec')
for i in range (1,8,2):# <-- pierwszy to wartosc startowa drugi to limit a trzeci to wartosc skokowa
    print(i)
else:
    print('koniec')
for i in lista:
    print(i)
else:
    print('koniec')
for i in range(8):###
    for j in range(8):###
        print(j)###
    else:###
            print('koniec')###
else:###
    print('koniec')#petla w petli  tam gdzie ###
licznik = 1
while licznik < len(lista):
    licznik +=1
else:
    print('koniec')
# mozna przerwac działanie petli funkcja break
lista2 = [1,2,23,4,5,435,43,6,45,6,7,7,6,78,43,34,43,15]
wejscie = sys.stdin.readline()
i=0
while i < len(lista2):
    i = i + 1
    if int(wejscie) - int(lista[i]) == 0:
        print(i, lista2[i])
    else:
        print('nie ma takiej liczby')
import math
def rownanie_kwadratowe(a,b,c):
    delta = b ** 2 -4 *a*c
    if delta < 0:
        print("brak rozwiązan")
        return 0
    elif delta == 0:
        print('jeden pierwiastek')
        return -b/2
    else:
        print('dwa pierwiastki ')
        x1 = -b - math.sqrt(delta)/2*a
        x2 = -b + math.sqrt(delta)/2*a
        return x1,x2
print(rownanie_kwadratowe(2,3,4))

def dlugosc_odcinka(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(dlugosc_odcinka(1,2,34,5))
print(dlugosc_odcinka(3,32,4,55))
print(dlugosc_odcinka(45,5423,43,23))
plik = open("tekst.txt", "r", encoding="utf-8")
znak = plik.read(10)
linia = plik.readline()
linie = plik.readline()
plik.close()
print(znak)
print(linia)
print(linie)
plik  = open("tekst", 'a+')
plik.write('aaaaaa')
plik.seek(105)
znaki = plik.read(10)
plik.close()
print(znaki)
with open('tekst.txt', 'r') as plik:
    zanki = plik.read(10)
print(znaki)"""
