
# numpyの配列には数字しか入れられない
# import numpy as np
# a = [0, 1, 2, 3, 4, 5]
# b = np.array(a)

# print(b)

# linspace 範囲を決まった数に等間隔にする
# x = np.linspace(-5 , 5)
# print(x)
# print(len(x))


# 一次関数
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-5, 5)
# y = 2 * x + 1

# plt.plot(x, y) #x,yをプロット
# plt.show() #グラフの表示

# グラフの装飾

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-3, 3)
# y_1 = 1.5 * x 
# y_2 =  -2 * x + 1

# plt.xlabel("x value", size=14)
# plt.ylabel("y value", size=14)

# plt.title("My graph")

# plt.grid()

# plt.plot(x, y_1, label="y_1")
# plt.plot(x, y_2, label="y_2", linestyle="dashed")
# plt.legend()
# plt.show()

# 二次関数・三次関数
# y =2x + 1 , y = x2 - 4, y = 0.5x3 -6x
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(-4, 4)
# y_1 = 2 * x + 1
# y_2 = x **2 - 4
# y_3 = 0.5 * x **3 - 6 * x

# plt.plot(x, y_1, label="1st")
# plt.plot(x, y_2, label="2nd")
# plt.plot(x, y_3, label="3rd")
# plt.legend()

# plt.xlabel("x", size=14)
# plt.ylabel("y", size=14)
# plt.grid()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10,100)

y =  x **2
y_2 = x + 1 / x

# plt.plot(x, y, label="graph")
plt.plot(x, y_2, label="4")
plt.legend()
plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()