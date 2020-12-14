#
# print("###############")
# aList = [ i**(1/2) for i in range(4)]
#
# index=0
# for elmnt in aList:
#     print ( "Element aList[%d]=%f" % (index, elmnt))
#     index += 1
# print("###############")
# aList = [ i**2 for i in range(4)]
#
#
# for index in range(10):
#     print ( "Element aList[%d]=%f" % (index, aList[index]))
#
# print("###############")
# aList = [ i**2 for i in range(4)]
#
# for ind, elmnt in enumerate(aList):
#     print( "Element aList[%d]=%f" % (ind, elmnt))
#
# for i in range(len(aList)):
#     print(i)
# for i in range(len(aList)):
#     print(i)

# print("###############1")
# a = 12
# b = 21
# for x in range(a,b):
#   if (x % 3) == 0:
#      print(x)
#
# print("###############2")
# a = input("Enter a character: ")
# if((a>='a' and a<= 'z') or (a>='A' and a<='Z')):
#     print(a, "to litery")
# else:
#     print(a, "to nie litery, czyli liczby albo znaki specjalne")
#
# class Osoba:
#   def __init__(self, nazwisko, wiek):
#     self.nazwisko = nazwisko
#     self.wiek = wiek
#
# o = Osoba("Jan Kowalski", 25)
# print(o.nazwisko)
# print(o.wiek)

# aList = [ i**2 for i in range(5)]
# bList = [ i*2 for i in range(6)]
# #bList = [ (i-1)**2 for i in range(4)]
# print("###############for p in zip")
# # with pair
# for p in zip(aList, bList):
#     print(p[0], p[1])
#
# # with pair
# for p, a in zip(enumerate(aList), bList):
#     print(p[0], p[1], a)
# print("###############for a, b in zip")
# # or by
# for a, b in zip(aList, bList):
#     print(a, b)

# import numpy as np
#
# tablica1 = np.array([1,2,5,12,5])
# print(tablica1) # >> [ 1  2  5 12  5]
#
# tab = np.zeros(20)
# print(tab)
#
# import numpy as np
#
# tablica1 = np.array([i for i in range(10)])
# print(tablica1)# >> [0 1 2 3 4 5 6 7 8 9]
#
# tablica1 = np.array(range(10))
# print(tablica1)# >> [0 1 2 3 4 5 6 7 8 9]
#
# import numpy as np
#
# tablica1 = np.zeros(10)
# print(tablica1) #>> [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#
# tablica2 = np.ones_like(tablica1)
# print(tablica2) #>> [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
#
# import numpy as np
#
# tablica1 = np.array( [1, 2, 3, 4, 5], dtype=float)
# print(tablica1) #>>[ 1.  2.  3.  4.  5.]
#
# tablica2 = np.zeros(10, dtype=int)
# print(tablica2) #>> [0 0 0 0 0 0 0 0 0 0]

# import timeit
#
# size=1000000
#
# start = timeit.default_timer()
#
# list1 = [i for i in range(size)]
# list2 = [i for i in range(size)]
# list3 = [0 for i in range(size)]
#
# start = timeit.default_timer()
#
# for i in range(size):
#     list3[i] = list1[i] + list2[i]
#
# t1 = float(timeit.default_timer()-start)
# print ("Czas1 :", str(t1))
#
#
# import numpy as np
#
# list1 = np.array(range(size))
# list2 = np.array(range(size))
# list3 = np.zeros_like(list2)
#
# start = timeit.default_timer()
#
# for i in range(size):
#     list3[i] = list1[i] + list2[i]
#
# t2 = float(timeit.default_timer()-start)
# print ("Czas2 :", str(t2))
#
#
# start = timeit.default_timer()
#
# list3 = list1 + list2
#
# t3 = float(timeit.default_timer()-start)
# print ("Czas3 :", str(t3))
#
# print ("t2/t1", t2/t1)
# print ("t1/t3", t1/t3)
# print ("t2/t3", t2/t3)

# import numpy as np
# tab2D = np.zeros((3,3))
# print ("Element z drugiego wiersza i drugiej kolumny to", tab2D[1][1])
#
# import numpy as np
# tab2D = np.zeros((3,3))
# print ("Element z drugiego wiersza i drugiej kolumny to", tab2D[1,1])
#
# import numpy as np
# tab2D = np.zeros((3,3))
# print ("Element z drugiego wiersza i drugiej kolumny to", tab2D[1,1])
#
# import numpy as np
# tab2D = np.ones((10,5), dtype=int)
#
# print (tab2D.shape) # >> (10, 5)
# print ("Pierwszy wymiar", tab2D.shape[0]) # >> Pierwszy wymiar 10
# print ("Drugi wymiar", tab2D.shape[1]) # >> Drugi wymiar 5
#
# import numpy as np
# tab = np.zeros(5)
# tab[:3] = 2
# print(tab )# >> [ 2.  2.  2.  0.  0.]
#
# tab2D = np.zeros((4,4))
# tab2D[:2,:2] = 2
# print (tab2D) #>> [[ 2.  2.  0.  0.]
#                         #        [ 2.  2.  0.  0.]
#                         #        [ 0.  0.  0.  0.]
#                         #            [ 0.  0.  0.  0.]]


import numpy as np

tab = np.zeros(10)
tab[[1,4,8,9]] = 2
print (tab)

mask = tab == 0
print( mask)

tab[ mask ] = -1
print (tab)

from random import randint
tab = np.array( [ randint(0,9) for i in range(10)])

print ("Liczby losowe wieksze od 5 dla tab:", tab )
for i, j in enumerate(tab[tab > 5]):
    print (i, j)



import numpy as np
xy = np.zeros((10,2))
print(xy)
xy[:, 0] = np.linspace(-1, 1, 10)
print (xy[:,0]) #>>[-1.         -0.77777778 -0.55555556 -0.33333333 -0.11111111  0.11111111 0.33333333 0.55555556  0.77777778  1. ]

xy[:, 1] = np.exp( xy[:, 0] )
print (xy[:,1])
print (xy)

