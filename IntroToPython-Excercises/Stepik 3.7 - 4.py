turtle_commands = [str(input()).lower().split(" ") for i in range(int(input()))]
# print(turtle_commands)

temp_list = []
for i in range(len(turtle_commands)):
    temp_list.append(int(turtle_commands[i][1]))
    turtle_commands[i][1] = temp_list[i]
# print(turtle_commands)

initial_coordinates = [0, 0]
for elem in turtle_commands:
    if elem[0] == 'север':
        initial_coordinates[1] = initial_coordinates[1] + elem[1]
    elif elem[0] == 'юг':
        initial_coordinates[1] = initial_coordinates[1] - elem[1]
    elif elem[0] == 'восток':
        initial_coordinates[0] = initial_coordinates[0] + elem[1]
    elif elem[0] == 'запад':
        initial_coordinates[0] = initial_coordinates[0] - elem[1]
print(" ".join(str(elem) for elem in initial_coordinates))