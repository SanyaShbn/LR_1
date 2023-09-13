check = False
while check != True:
    print('Введите начальное число из диапазона: ')
    numb1 = input()
    print('Введите конечное число из диапазона: ')
    numb2 = input()
    if not numb1.isdigit() or not numb2.isdigit():
        print('Необходимо ввести натуральные числа! Попробуйте ещё раз: ')
        continue
    else:
        check = True
        numb1 = int(numb1)
        numb2 = int(numb2)
print("Все простые числа из заданного диапазона: ")
for i in range(numb1, numb2):
    flag = False
    for divider in range(2, i):
        if i % divider == 0:
            flag = True
            break
    if flag == False and i != 0:
        print(i)


