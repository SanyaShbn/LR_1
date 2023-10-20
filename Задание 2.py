from operator import itemgetter

list_of_trains = []
filtered_list = []
count = 0
with open("Railway_station.txt") as trains:
    for line in trains:
        list_of_trains.append(list(line.split()))
    print(list_of_trains)
day = input("Введите желаемый день недели:")
for train in list_of_trains:
    if day in train:
        filtered_list.append(train)
        count += 1
if count == 0:
    print("Подходящие рейсы не найдены")
else:
    print("Подходящие поезда:")
    print(filtered_list)
print("Поезд с максимальной стоимостью билета - " + str(max(list_of_trains, key = itemgetter(4))))
