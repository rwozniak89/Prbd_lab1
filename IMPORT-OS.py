import os


# Definiujemy zmienna do przechowywania sciezki do folderu zawierajacego pliki
source = "./resources/lab2/files"

for x in os.listdir(source):
    print (x)