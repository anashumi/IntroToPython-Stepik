lst = []

with open('/Users/oksana.shumilova/Library/Application Support/JetBrains/PyCharm2020.1/scratches/dataset_3363_3.txt', 'r') as dtaset:
    while True:
        line = dtaset.readline().strip()
        lst.append(line)
        if not line:
            break
# print(lst)

strng = ''
for element in lst:
    strng = strng + ' ' + str(element)
# print(strng)

temp_string = strng.lower()
# print(temp_string)
temp_lst = temp_string.split()
# print(temp_lst)
temp_dict = {}
for elem in temp_lst:
    if elem in temp_dict.keys():
        temp_dict[elem] = temp_dict[elem] + 1
    else:
        temp_dict[elem] = 1
# print(temp_dict)
# print(max(temp_dict.values()))
output = []
for key in temp_dict:
    if temp_dict[key] == max(temp_dict.values()):
        output.append(str(key) + ' ' + str(temp_dict[key]))
output.sort()
print(output[0])