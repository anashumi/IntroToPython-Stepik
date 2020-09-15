def modify_list(l):
    modified_list = []
    for elem in l:
       if elem % 2 == 0:
           modified_list.append(elem / 2)
    del l[:]
    l.extend(modified_list)
    return

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)   # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

lst = [0, 7, 112, 0, 5, 0, 98, 0]
modify_list(lst)
print(lst) # [0, 56, 0, 0, 49, 0]

lst = []
modify_list(lst)
print(lst) # [0, 56, 0, 0, 49, 0]

lst = [1]
modify_list(lst)
print(lst) # [0, 56, 0, 0, 49, 0]

lst = [2]
modify_list(lst)
print(lst) # [0, 56, 0, 0, 49, 0]

lst = [2,2,2,2]
modify_list(lst)
print(lst) # [0, 56, 0, 0, 49, 0]
# def modify_list(l):
#     for i in range(-1, -len(l)-1, -1):
#        if l[i] % 2 == 0:
#            l[i] = l[i] / 2
#        else:
#            del l[i]
#     return l
#
# lst = [1, 2, 3, 4]
# print lst
# print(modify_list(lst))
# print lst