n = input().lower()
words = n.split()
times_in_string = {}
for elem in words:
    if elem in times_in_string:
        times_in_string[elem] += 1
    else:
        times_in_string[elem] = 1
result = []
for key in times_in_string.keys():
    result.append(str(key) + " " + str(times_in_string[key]))
print("\n".join(elem for elem in result))

# for x in range(0, len(times_in_string)):
#     new_dict[x] = times_in_string.keys()[x] + " " + str(times_in_string.values()[x])
# print("\n".join(str(elem) for elem in new_dict.values()))