def check_type(n):
    if type(n) == tuple:
        count = 0
        for i in n:
            if(type(i) == str):
                if i.isalpha():
                    count += len(i)
        if count == 0:
            print("В кортеже нет слов")
        else:
            print("Длина всех элементов кортежа, являющихся словами:")
            print(count)
    elif type(n) == list:
        a = list(set(n))
        print("Ваш список без повторяющихся элементов \n")
        print(a)
        pr = 1
        for i in range(len(a)):
            if a[i] == 0:
                index = i
                break
        b = a[index + 1:]
        for i in b:
            if type(i) == int or type(i) == int:
                pr *= i
        print(pr)
    elif type(n) == int:
        flag = False
        for divider in range(2, n):
            if n % divider == 0:
                flag = True
                break
        if flag == False and n != 0:
            print("Вы ввели простое число")
        else:
            print("Число не является простым")
    elif type(n) == str:
        print("Символы из таблицы Unicode для вашей строки:")
        print(n.encode("utf-8"))


a = [122,0,234, 1, 1, 00 , 0, 0, 234, "4345"]
check_type(a)



