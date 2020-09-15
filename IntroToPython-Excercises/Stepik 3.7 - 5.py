lst_of_student_heights =[]
with open('/Users/oksana.shumilova/Library/Application Support/JetBrains/PyCharm2020.1/scratches/dataset_3380_5.txt', 'r') as dtaset:
    while True:
        line = dtaset.readline().strip()
        lst_of_student_heights.append(line.split("\t"))
        if not line:
            break
# print(lst)
del lst_of_student_heights[-1]

temp_list = []
for i in range(len(lst_of_student_heights)):
    temp_list.append(int(lst_of_student_heights[i][0]))
    lst_of_student_heights[i][0] = temp_list[i]
temp_list = []
for i in range(len(lst_of_student_heights)):
    temp_list.append(int(lst_of_student_heights[i][2]))
    lst_of_student_heights[i][2] = temp_list[i]
# print(temp_list)
# print(lst_of_student_heights)

avg_height_per_class = [[i] for i in range(1, 12)]
print(avg_height_per_class)

for student in lst_of_student_heights:
    for elem in avg_height_per_class:
        if student[0] == elem[0]:
            elem.append(student[2])
# print(avg_height_per_class)

for elem in avg_height_per_class:
    if len(elem) > 1:
        avgHeight = (sum(elem) - elem[0]) / (len(elem) - 1)
        elem.insert(1, avgHeight)
    if len(elem) == 1:
        elem.insert(1, '-')
for elem in avg_height_per_class:
    del elem[2 : len(elem)]
    print(' '.join(str(i) for i in elem))
# print(avg_height_per_class)
# print("\n".join(str(elem) for elem in avg_height_per_class))