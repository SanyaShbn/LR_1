import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Задание 1
Fun_x = np.array([0])
t = 2
while(t <= 3):
    y = np.log(np.fabs(1.3 + t)) - np.exp(t)
    Fun_x = np.append(Fun_x, y)
    t += 0.03
X = np.arange(2, 3, 0.03)
Fun_x = np.delete(Fun_x, 0)
Res = pd.DataFrame({"t": X, "f(t)": Fun_x})
print(Res)
print("Наибольшее значение - {}".format(Fun_x.max()))
print("Наименьшее значение - {}".format(Fun_x.min()))
print("Среднее значение - {}".format(Fun_x.mean()))
print("Количество элементов массива значений функции f(t) - {}".format(Fun_x.size))
print("Отсортированный по убыванию numpy-массив функций f(t)")
print(np.sort(Fun_x, axis=-1))

plt.plot(X, Fun_x, label="2<=t<=3; -19<f(t)<-6")
plt.axhline(y=Fun_x.mean(), color="red", label="среднее значение f(t)")
plt.title("График изменения значений функции f(t)")
plt.xlabel("Значения аргумента t")
plt.ylabel("Значения функции f(t)")
plt.legend(loc = "upper right", frameon = False)

plt.show()

# Задание 2

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.cos(v) * np.sin(u)
z1 = x**0.25 + y**0.25
z2 = x ** 2 - y ** 2
z3 = 2*x +3*y
z4 = x**2 + y**2
z5 = 2 + 2*x + 2*y -x**2 - y**2

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1, projection='3d')
ax.plot_surface(x, y, z1)
ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.plot_wireframe(x, y, z2)
ax = fig.add_subplot(2, 2, 3, projection='3d')
ax.plot_wireframe(x, y, z3)
ax = fig.add_subplot(2, 2, 4, projection='3d')
ax.scatter(x, y, z4)
ax = fig.add_subplot(2, 1, 1, projection='3d')
ax.plot_surface(x, y, z5)
plt.show()