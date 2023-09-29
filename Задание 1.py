import random
def is_prime(a):
    print(a)
    flag = False
    for divider in range(2, a):
        if a % divider == 0:
            flag = True
            break
    if flag == False and a != 0:
        return True
    else:
        return False

numb = (is_prime(random.randint(0, 1000)))
print(numb)
if numb == False :
    print("Число не является простым")
else:
    print("Число является простым")
