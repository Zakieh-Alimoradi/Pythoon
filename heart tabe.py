import numpy as np
import matplotlib.pyplot as plt


def f(x, sign):
  return (sign * np.sqrt(1 - x**2) + np.sqrt(abs(x))) * 0.8


x = np.linspace(-1, 1, 1000)


y_positive = f(x, 1)
y_negative = f(x, -1)


plt.plot(x, y_positive, label='possitive ')
plt.plot(x, y_negative, label='negative ')


plt.xlabel('x')
plt.ylabel('y')
plt.title('geraf moadele  y=(+-√1-x² +√|x|)×0.8')
plt.legend()
plt.grid(True)


plt.show()