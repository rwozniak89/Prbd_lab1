import main_DS_PYTHON_cz2_zadanie3 as zad3
import numpy as np
import matplotlib.image as ima
import matplotlib.pyplot as plt
import matplotlib.colors as col


file_source = './resources/lab2/meil.png'

tab = ima.imread(file_source)
tab_org = tab.copy()

print(tab.shape)
tab2 = np.array(zad3.reduce(tab, (30, 30)))
print(tab2.shape)


tab4 = col.rgb_to_hsv(tab2)
tab3 = tab2.copy()
print(tab3.shape)

# print(tab3)

print(tab3.shape)
print(tab4.shape)
np.set_printoptions(threshold=np.inf)
#print(tab4[:3,:3,:3])
print(tab4.size)
#print(tab4[:,:,2])
print(tab4[:,:,2].size)
#plt.imshow(tab3)
#plt.imshow(tab4)
#plt.show()

tab5 = tab4[:,:,2]
print(tab5)
print(type(tab5))

progCzarne = 0.60
progBiale = 0.20

mask1 = (tab5 >= progCzarne)
mask2 = (np.array(tab5 >= progBiale) & (tab5 < progCzarne))
mask3 = (tab5 < progBiale)
tab6 = tab5.copy()
tab6[mask1] = 1
tab6[mask2] = 0.5
tab6[mask3] = 0

with open("logo_jako_tekst.txt", "w+") as plik:
    for index in range(0, len(tab6)):
        plik.write("\n")
        for el in tab6[index]:
            if el == 1:
                plik.write("  ")
            elif el == 0:
                plik.write("||")
            else:
                plik.write("--")
            if index >= len(tab6):
                break
