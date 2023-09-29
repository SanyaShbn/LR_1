def task3(n, m):
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            if(i + j) % 2 == 0:
                a[i].append(".")
            else:
                a[i].append("*")
    for el in a:
        print(' '.join(el))

check = False
while check == False:
    try:
       print("Введите n = ")
       n = input()
       print("Введите m = ")
       m = input()
       n = int(n)
       m = int(m)
       task3(n, m)
    except ValueError:
        print("Необходимо ввести натуральное число! Попробуйте ещё раз")
    finally:
        if(type(m) == int and type(n) == int):
           check = True

