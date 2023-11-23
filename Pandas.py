import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Задание 1 и 2
test = pd.read_csv("test-1.csv", nrows=1000)

# Задание 3
check = test.isnull().sum()
print(check)

test2 = test.fillna("unknown")

# Задание 4
x = 1
for col_name in test.columns:
    new_series_array = np.array(test[col_name])
    plt.subplot(4, 5, x)
    plt.subplots_adjust(hspace=0.5)
    plt.hist(new_series_array)
    plt.title(col_name)
    x += 1

plt.show()

x = 1
for col_name in test.columns:
    new_series_array = np.array(test[col_name])
    plt.subplot(4, 5, x)
    plt.subplots_adjust(hspace=0.5)
    plt.plot(new_series_array)
    plt.yscale(value="log")
    plt.title(col_name)
    x += 1

plt.show()

# Задание 5
x = 10
for values in test2["LifeSquare"]:
    if(x > 80):
       x = 15
    if(values != "unknown"):
        if (type(values) == float):
            test2 = test2.replace(values, x)
    x+=1
for values in test2["Square"]:
    if(x > 150):
       x = 15
    if(values != "unknown"):
        if (type(values) == float):
            test2 = test2.replace(values, x)
    x+=1
for values in test2["KitchenSquare"]:
    if(x > 50):
       x = 15
    if(values != "unknown"):
        if (type(values) == float):
            test2 = test2.replace(values, x)
    x+=1
for values in test2["Floor"]:
    if(x > 25):
       x = 10
    if(values != "unknown"):
        if (int(values) <= 0 or int(values) > 25):
            test2 = test2.replace(values, x)
    x+=1
for values in test2["HouseFloor"]:
    if(x > 25):
       x = 10
    if(values != "unknown"):
        if (int(values) <= 0 or int(values) > 25):
            test2 = test2.replace(values, x)
    x+=1
for values in test2["HouseYear"]:
    if(x > 2023):
       x = 1990
    if(values != "unknown"):
        if (values < 1975 or values > 2023):
            test2 = test2.replace(values, x)
    x+=1

# Задание 6
rooms_kol = pd.DataFrame(test.groupby(test["Rooms"].tolist(), as_index=False).size())
rooms_kol.columns = ["Кол-во комнат", "Кол-во квартир с таким количеством комнат"]
print(rooms_kol)

# Задание 7
districts_info = pd.pivot_table(test, index=["DistrictId"], columns=["Rooms"], values=["LifeSquare"])

print(districts_info.fillna("unknown"))

# Задание 8
test2.to_csv("Shubin_Task_2.csv")