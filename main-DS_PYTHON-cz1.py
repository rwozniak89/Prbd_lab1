# -*- coding: utf-8 -*-

def test(fun, *args):
    print("".join(['-' for i in range(40)]))
    print(fun.__name__[:-1].upper() + " " + fun.__name__[-1])
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print("Yes, " + decoded.replace("my", "your"))
        else:
            print("No, " + decoded.replace("my", "your").replace("has", "has not") + " yet")
    else:
        print("Is correct? " + str(res == args[-1]))
    print("".join(['-' for i in range(40)]))


def zadanie1(listObject):
    lista = [listObject[0]]
    for x in listObject:
        if x != lista[-1]:
            lista.append(x)
    return lista

test(zadanie1, [1, 2, 3, 3, 5, 68, 68, 24], [1, 2, 3, 5, 68, 24])

def zadanie2(list1, list2):
    lista = []
    len1 = len(list1)
    len2 = len(list2)
    max_len = len1
    if len2 > max_len:
        max_len = len2
    for i in range(0, max_len):
        if i < len1:
            lista.append(list1[i])
        if i < len2:
            lista.append(list2[i])
    return lista

test(zadanie2, [1, 2, 19, 'dd', ':P', ":("], [12, 'c', '5'], [1, 12, 2, 'c', 19, '5', 'dd', ':P', ':('])


def zadanie3(listTuples):
    lista = listTuples
    lista.sort(key=lambda tup: tup[len(tup) - 1], reverse=False)
    return lista


test(zadanie3, [(1, 3), (3, 3, 2), (2, 1)], [(2, 1), (3, 3, 2), (1, 3)])


def zadanie4(text):
    return ' '.join([s.replace('ok', '') for s in text.split('$') if s.startswith('ok')])


test(zadanie4, "okmy$aiaetiaigaafbaf??a$okwatch$oafbusd$okhas$asbrsi31480$okended$aq340af",
     [109, 121, 32, 119, 97, 116, 99, 104, 32, 104, 97, 115, 32, 101, 110, 100, 101, 100])

print('ZADANIE 5')

from random import randint
x = randint(1, 100)
licznik=0
liczba = -1
print('Super Zgadywanko, zgadnij liczbę od 1 do 100 w jak najmniejszej liczbie prób')
print(f'Mała podpowiedź to 1, 2, 3, 4, 5, {x}')
while True:
    licznik +=1
    a = input("Podaj liczbe:")
    try:
        liczba = int(a)
    except:
        print(f'Podane znaki {a} to nie liczba całkowita')
        continue
    if liczba == x:
        print(f'Wygrałeś!!! Szukana liczba to {x}, rozwiązanie znaleziono po {licznik} próbach !')
        break
    elif liczba > x:
        print(f'Podano liczbę większą niż szukana')
    else:
        print(f'Podano liczbę mniejszą niż szukana')


