import os

import shutil

# Definiujemy zmienna do przechowywania sciezki do folderu zawierajacego pliki
source = "./resources/lab2/files/"

#list_of_files = os.listdir(source)

print('Wyświerlenie zawartości przed przeniesieniem')
for x in os.listdir(source):
    print (x)

print('\noperacja przenoszenia\n')
for x in os.listdir(source):
    x_source = source + x
    text = ''
    if os.path.isfile(x_source):
        with open(x_source, "r") as plik:
            text = plik.readline()

    place = text.replace('location: ', '')
    dir_to_do = source + place

    if os.path.isdir(dir_to_do):
        pass
    else:
        os.makedirs(dir_to_do)

    shutil.move(x_source, dir_to_do + "\\" + x)


print('Wyświerlenie zawartości po przeniesieniu')
for x in os.listdir(source):
    print (x)
    if os.path.isdir(source + "\\" + x):
        for x2 in os.listdir(source + "\\" + x):
            print(x2)

