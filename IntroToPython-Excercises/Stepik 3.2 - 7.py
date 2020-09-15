lst = [int(input()) for i in range(int(input()))]
dict = {}

for elem in lst:
    dict[elem] = 0

for elem in lst:
    if dict[elem] != 0:
        print(dict[elem])
    else:
        dict[elem] = f(elem)
        print(dict[elem])