import main_DS_PYTHON_cz2_zadanie3 as zad3
import numpy as np
import matplotlib.image as ima
import matplotlib.pyplot as plt

# print('test import zad3')
# # Test
# m = [[float(i*j) for i in range(5)] for j in range(5)]
# print(np.array(m))
# print(np.array(zad3.reduce(m, (3, 3))))

file_source = './resources/lab2/meil.png'

tab = ima.imread(file_source)
tab_org = tab.copy()

print(tab.shape)
tab2 = np.array(zad3.reduce(tab, (20, 20)))
print(tab2.shape)

#tab = np.ndarray(tab)
# print(type(tab))
# print(tab.shape)
# print(tab.size)
# ## print(tab.tolist())
# plt.imshow(tab_org)
# plt.show()
# plt.imshow(tab2)
# plt.show()
#plt.imshow(tab2)

fig, (ax1, ax2) = plt.subplots(2)
ax1.imshow(tab_org)
ax2.imshow(tab2)
#ax1.plot(x, y, color="blue", marker=".", linestyle="")
#x2.plot(x, np.cos(x), color="blue", marker="", linestyle="-")

# ax1.grid(True)
ax1.set_title("logo oryginalne")
ax2.set_title("logo przeskalowane")

plt.title("logo przed i po")

plt.savefig('logo_org_i_przeskalowane.png')

plt.show()
