from aetypes import end
lst = [int(x) for x in input().split()]
x = int(input())

if x not in lst:
    print("Отсутствует")

n = len(lst)
l = []
for i in range(0, n):
    if lst[i] == x:
        l.append(i)
print(' '.join([str(elem) for elem in l]))