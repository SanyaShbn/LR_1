check1 = False
check2 = False
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
vowels_numb = 0
consonants_numb = 0
i = 0
all_vowels = ' '
print('Введите текст на русском языке')
text = input()
for i in range(len(text)):
    if text[i] in vowels:
        vowels_numb += 1
        if text[i] not in all_vowels:
            all_vowels += ' ' + text[i]
    elif text[i] in consonants:
        consonants_numb += 1

print('Количество гласных русского языка - ' + str(vowels_numb))
print('Количество согласных русского языка - ' + str(consonants_numb))
if vowels_numb == consonants_numb and vowels_numb != 0:
    print('Гласные в тексте:' + all_vowels)
words = len(text.split()) + (len(text.split(',')) - 1) + (len(text.split(':')) - 1) + (len(text.split(';')) - 1) + (len(text.split('.')) - 1)
print('Количество слов в тексте - ' + str(words))

