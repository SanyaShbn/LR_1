import heapq, operator
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print("Список всех ключей в словаре:")
print(my_dict)
print("Три ключа с самыми высокими значениями в данном словаре")
print(list(zip(*heapq.nlargest(3, my_dict.items(), operator.itemgetter(1))))[0])