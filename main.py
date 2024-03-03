import sys
a = 2
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
