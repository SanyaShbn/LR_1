from random import random, randint
numbers1 = [random for _ in range(20)]
numbers2 = [random for _ in range(20)]
same_numbers = ' '
i = 0
j = 0
for i in range(len(numbers1)):
    numbers1[i] = randint(-100, 100)
for j in range(len(numbers2)):
    numbers2[j] = randint(-100, 100)
print(numbers1)
print(numbers2)
i = 0
j = 0
for i in range(len(numbers1)):
    for j in range(len(numbers2)):
        if numbers1[i] == numbers2[j]:
            same_numbers += str(numbers1[i]) + ' '
print('Повторяющиеся элементы в двух множествах:')
print(same_numbers)