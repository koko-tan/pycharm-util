import matplotlib.pyplot as plt
import numpy as np


# 生成一个二次曲线
x = np.linspace(-2, 7, 200)
y = (x - 2.5)**2 + 1

plt.plot(x, y)
plt.show()
