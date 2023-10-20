dict_subjects = {}
list_subjects = []
with open("Subjects.txt") as subjects:
    for line in subjects:
        list_subjects.append(line.split())
        i = 1
        sum = 0
        while i < (len(list_subjects[0])):
            subj = list_subjects[0][i].split("(")
            i += 1
            sum += int(subj[0])
        dict_subjects[list_subjects[0][0]] = sum
        del list_subjects[:]
        del subj[:]
print(dict_subjects)

