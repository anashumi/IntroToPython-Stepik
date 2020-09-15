lst = []

with open('/Users/oksana.shumilova/Library/Application Support/JetBrains/PyCharm2020.1/scratches/dataset_3363_4.txt', 'r') as dtaset:
    while True:
        line = dtaset.readline().strip()
        lst.append(line)
        if not line:
            break
# print(lst)

temp_list = []

for elmnt in lst:
    new_elem = str(elmnt).split(';')
    temp_list.append(new_elem)

del temp_list[-1]

total_math = 0
total_physics = 0
total_russian = 0

for elem in temp_list:
    print((int(elem[1]) + int(elem[2]) + int(elem[3])) / 3)
    total_math = total_math + int(elem[1])
    total_physics = total_physics + int(elem[2])
    total_russian = total_russian + int(elem[3])

print(str(total_math / len(temp_list)) + ' ' + str(total_physics / len(temp_list)) + ' ' + str(total_russian / len(temp_list)))