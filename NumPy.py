import numpy as np

a = 0.3
b = -21.17
f1 = np.array([1 / np.tan(np.pi / 4 - 1) ** 4])
f2 = np.array([(a + 1.5)**1/3])
f3 = np.array([-(b/np.arcsin(abs(a)**2))])
result = f1 + f2 + f3
print("Задание 1.1:")
print(result)

X_column1 = np.ones((12,1))
X_column2 = np.random.randint(15, 27, (12,1))
X_column3 = np.random.randint(60, 82, (12,1))
X = np.hstack((X_column1, X_column2, X_column3))
Y = np.random.uniform(13.5, 18.6, (12,1))

A = np.linalg.inv((X.transpose().dot(X))).dot(X.transpose().dot(Y))
print("\nЗадание 1.2:")
print(A)
