from random import randint

check = False
numbers = []
cube_of_numbers = []
sum = 0
pr = 1
while check != True:
    print('Введите количество элементов списка: ')
    numb = input()

    if not numb.isdigit():
        print('Необходимо ввести натуральное число! Попробуйте ещё раз: ')
        continue
    else:
        check = True
numb = int(numb)
print('Ваш список чисел: ')
for i in range(numb):
    numbers.append(randint(-100, 100))
print(numbers)
print('Список из кубов чисел, предложенных в предыдущем списке: ')
for i in range(numb):
    cube_of_numbers.append(numbers[i]**3)
    sum += cube_of_numbers[i]
    pr *= cube_of_numbers[i]
print(cube_of_numbers)
print('Список из кубов чисел, представленный в обратном порядке: ')
print(cube_of_numbers[::-1])
print('Сумма чисел списка = ' + str(sum),' , произведдение = ' + str(pr))