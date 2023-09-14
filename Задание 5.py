dict = {
"Кольцо": ["90% - золото 10% - серебро", "2000", "50"],
"Колье": ["50% - золото 50% - серебро", "3500", "25"],
"Ожерелье": ["100% - золото", "10000", "10"],
"Цепь": ["100% - серебро", "5000", "30"],
"Браслет": ["10% - золото 90% - серебро", "8000", "45"]
}

keys = ["Кольцо", "Колье", "Ожерелье", "Цепь", "Браслет"]

def show_info(type_of_value, description, dict):
    while True:
        j = 0
        for i in dict:
            print(keys[j] + ":")
            print(description + dict.get(i)[type_of_value])
            j+=1
        print("Вывести информацию заново - 0, ГЛАВНОЕ МЕНЮ - любая другая клавиша")
        kod = input()
        if kod != "0":
            return

def purchase():
    dict_of_purchases = {}
    name = []
    while True:
        same = False
        flag = False
        name1 = (input("Введите название: "))
        if name1 in keys:
            flag = True
        if flag == False:
            print("Такого изделия в магазине нет!")
        else:
            if name1 in name:
                same = True
            else:
                name.append(name1)
            while True:
                numb1 = input("Введите желаемое количество товаров: ")
                general_numb = int(dict.get(name1)[2])
                if numb1.isdigit():
                    if int(numb1) == 0:
                        break
                    elif int(numb1) > general_numb:
                        print(f'В наличии нет такого количества товаров')
                    else:
                        print("Заказ успешно оформлен!")
                        dict[name1][2] = str(int(dict.get(name1)[2]) - int(numb1))
                        if same == True:
                            dict_of_purchases[name1] += int(numb1)
                        else:
                            dict_of_purchases[name1] = int(numb1)
                        break
                else:
                    print("Введено некорректно значение! Попробуйте ещё раз!")
        print("Оформить ещё одну покупку - 0, ГЛАВНОЕ МЕНЮ - любая другая клавиша")
        kod = input()
        if kod != "0":
            break
    print("-----ЧЕК-----")
    i = 0
    price = 0
    print("Вы приобрели : \n")
    while i < len(name):
        price = price + int(dict.get(name[i])[1]) * dict_of_purchases[name[i]]
        print(name[i] + "\nСостав:" + dict.get(name[i])[0] + "; цена(бел. руб) - " +
              dict.get(name[i])[1]
              + "; приобретённое количество: " + str(dict_of_purchases[name[i]]) + " шт.")
        i+=1
    print("Итого: " + str(price) + " бел.руб")

print("Добро пожаловать в ювелирный магазин!")
while True:
    print("1 - Просмотр описания\n"
          "2 - Просмотр цены\n"
          "3 - Просмотр количества\n"
          "4 - Просмотр всей информации\n"
          "5 - Покупка\n"
          "6 - До свидания!")
    choice = input()
    if choice == "1":
        show_info(0, "Состав: ", dict)
    elif choice == "2":
        show_info(1, "Цена (бел. руб): ", dict)
    elif choice == "3":
        show_info(2, "Количество в наличии: ", dict)
    elif choice == "4":
        while True:
            j = 0
            for i in dict:
                print(keys[j] + ":" + "\n" + "Состав: " + dict.get(i)[0] + "; цена(бел. руб) - " + dict.get(i)[1]
                      + "; количество в наличии: " + dict.get(i)[2] + " шт.")
                j += 1
            print("Вывести информацию заново - 0, ГЛАВНОЕ МЕНЮ - любая другая клавиша")
            kod = input()
            if kod != "0":
                break
    elif choice == "5":
        purchase()
    elif choice == "6":
        break
    else:
        print("Неправильная клавиша! Попробуйте ещё раз.")
