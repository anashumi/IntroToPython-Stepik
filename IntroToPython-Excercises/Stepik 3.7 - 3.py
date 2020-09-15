# первой строкой передается кол-во известных слов: str(input()) повторяется столько раз, сколько int(input())
known_words = [str(input()).lower() for i in range(int(input()))]
lines_to_check = [str(input()).lower().split(" ") for i in range(int(input()))]

# check that everything works correctly
# print(known_words)
# print(lines_to_check)

list_of_errors = []
for elem in lines_to_check:
    for i in elem:
        if i not in known_words and i not in list_of_errors:
            list_of_errors.append(i)
# print(list_of_errors)

print("\n".join(elem for elem in list_of_errors))