with open('/Users/oksana.shumilova/Library/Application Support/JetBrains/PyCharm2020.1/scratches/dataset_3363_2.txt', 'r') as dtaset:
    n = dtaset.readline()
    new_string = n + 'A'

    acc = ''
    letter = ''
    temp_list = []
    for i in range(len(new_string)):
        if new_string[i].isdigit():
            acc = acc + new_string[i]
            # acc = acc * 10 + int(n[i])
        else:
            if len(acc) != 0:
                temp_list.append(letter * int(acc))
            letter = new_string[i]
            acc = ''
    output = ''
    for elem in temp_list:
        output = output + str(elem)
    print(output)


# temp_string = ''
# output = ''
# j = 0
# temp_list = []
#
# for i in range(len(n)):
#     if n[i].isdigit() is True and n[i + 1].isdigit() is False and n[i + 2].isdigit() is False:
#         temp_string = n[j:i]
#         temp_list.append(temp_string * int(n[i]))
#         j = i + 1
#     elif n[i].isdigit() is True and n[i + 1].isdigit() is True and n[i + 2].isdigit() is False:
#         temp_string = n[j:i]
#         temp_list.append(temp_string * int(n[i:i + 2]))
#         j = i + 2
#     elif n[i].isdigit() is True and n[i + 1].isdigit() is True and n[i + 2].isdigit() is True:
#         temp_string = n[j:i]
#         temp_list.append(temp_string * int(n[i:i + 3]))
#         j = i + 3
# print(temp_list)