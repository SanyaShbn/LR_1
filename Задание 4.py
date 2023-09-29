a = [1, 2, 3, 4, 5]
print(a)
check = False
while check == False:
    print("Введите индекс элемента, который хотели бы заменить в данном списке")
    index = input()
    try:
        index = int(index)
        print("Введите новый элемент, которым хотите заменить выбранный")
        a[index] = input()
        print("a[" + str(index) +"] = " + a[index])
        print("Ваш новый список")
        print(a)
    except IndexError:
        print("Вы вышли за пределы списка! Введите другой индекс")
    except ValueError:
        print("В качестве индекса нужно ввести натуральное число! Попробуйте ещё раз")
    finally:
        if type(index) == int and index <= len(a):
           check = True