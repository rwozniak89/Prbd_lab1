# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# plt.figure()
#
# plt.plot(x, y)
# plt.plot(x, np.cos(x))
#
# plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# plt.figure()
#
# plt.plot(x, y, "b.")
# plt.plot(x, np.cos(x), "b-")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# plt.figure()
#
# plt.plot(x, y, color="blue", marker=".", linestyle="")
# plt.plot(x, np.cos(x), color="blue", marker="", linestyle="-")
#
# plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# plt.figure()
#
# plt.plot(x, y, color="blue", marker=".", linestyle="")
# plt.plot(x, np.cos(x), color="blue", marker="", linestyle="-")
#
# plt.grid(True)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("sin(x) i cos(x)")
#
# plt.show()
#
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
# y = np.sin(x)
#
# fig, (ax1, ax2) = plt.subplots(2)
#
# ax1.plot(x, y, color="blue", marker=".", linestyle="")
# ax2.plot(x, np.cos(x), color="blue", marker="", linestyle="-")
#
# ax1.grid(True)
# ax1.set_xlabel("x")
# ax1.set_ylabel("y")
# ax1.set_title("sin(x)")
# ax2.set_title("cos(x)")
#
# plt.show()
#
#
# # import matplotlib.pyplot as plt
# # import numpy as np
# #
# # x = np.linspace(0,np.pi, 100)
# #
# # fig = plt.figure()
# #
# # line,  = plt.plot(x, np.zeros_like(x))
# #
# # print(type(line))
#
#
#
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np
#
# x = np.linspace(0,np.pi, 100)
#
# fig = plt.figure()
#
# line,  = plt.plot(x, np.zeros_like(x))
#
# plt.xlim([0, np.pi])
# plt.ylim([-1, 1])
#
# def update_plot(frame):
#     a  = float(frame)/100
#     line.set_ydata(np.sin(a*x))
#
# anim = FuncAnimation(fig, update_plot, frames=300, interval=1, repeat=False)
#
# plt.show()
