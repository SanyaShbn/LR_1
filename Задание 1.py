import os

check = False
while check == False:
    F1 = open("F1.txt", "w")
    try:
        print("Сколько строк хотите ввести?")
        count = input()
        count = int(count)
        for i in range(count):
            print("Введите строку для записи в файл:")
            string = input()
            F1.write(string + "\n")
    except TypeError:
        print("Необходимо ввести натуральное число! Попробуйте ещё раз")
    except ValueError:
        print("Необходимо ввести натуральное число! Попробуйте ещё раз")
    finally:
        if type(count) == int:
            check = True
        F1.close()
try:
    with open("F1.txt") as f1_file, open("F2.txt", "w") as f2_file:
        i = 1
        for line in f1_file:
            if i % 2 != 0:
                f2_file.write(line)
            i += 1
except IOError:
    print("Ошибка ввода-вывода!")
print("Размер файла F1 в батах - " + str(os.path.getsize("F1.txt")) + "; F2 - " + str(os.path.getsize("F2.txt")))
