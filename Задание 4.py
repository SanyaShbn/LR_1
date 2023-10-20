import json
final_list = []
list_of_firms = []
dict_of_firms = {}
profit = 0
with open("Firms.txt") as firms:
    for read_line in firms:
        list_of_firms.append(read_line.split())
for firm in list_of_firms:
    if len(firm) == 4:
        dict_of_firms[firm[0]] = firm[3]
    else:
        dict_of_firms[firm[0]] = firm[2]
        profit += int(firm[2])
average_profit = profit/int(len(list_of_firms))
profit_dict = {"average_profit": average_profit}
final_list = [dict_of_firms, profit_dict]
print(final_list)
with open("Firms_json.json", "w") as write_f:
    json.dump(final_list, write_f)
