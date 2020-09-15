matrix = []
while True:
    n = input()
    if n == 'end':
        break
    else:
        row_in_matrix = [int(x) for x in n.split()]
        matrix.append(row_in_matrix)

# i -> row coordinate
# j -> col coordinate
# every elem in matrix is matrix[i][j]

a = len(matrix[0])  # max width of matrix
b = len(matrix)  # max height of matrix

new_matrix = []
for i in range(b):
    new_matrix_row = []
    for j in range(a):
        if a == 1 and b == 1: # for when input is a single element (1 x 1 matrix)
            elem = matrix[-1][j] + matrix[0][j] + matrix[i][-1] + matrix[i][0]
            new_matrix_row.append(elem)
            continue
        elif b == 1 and a != 1: # for when input is a single row
            if i == 0 and j == 0:
                elem = matrix[0][j] + matrix[0][j] + matrix[0][-1] + matrix[0][j + 1]
            elif i == 0 and j == a - 1:
                elem = matrix[0][j] + matrix[0][j] + matrix[0][j - 1] + matrix[0][0]
            else:
                elem = matrix[0][j] + matrix[0][j] + matrix[0][j - 1] + matrix[0][j + 1]
        elif a == 1 and b != 1: # for when input a single column
            if i == 0 and j == 0:
                elem = matrix[-1][0] + matrix[i + 1][0] + matrix[i][0] + matrix[i][0]
            elif j == 0 and i == b - 1:
                elem = matrix[i - 1][0] + matrix[0][0] + matrix[i][0] + matrix[i][0]
            else:
                elem = matrix[i - 1][0] + matrix[i + 1][0] + matrix[i][0] + matrix[i][0]
        elif i == 0 and j == 0:
            elem = matrix[-1][j] + matrix[i + 1][j] + matrix[i][-1] + matrix[i][j + 1]
        elif i == 0 and j == a - 1:
            elem = matrix[b - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][0]
        elif i == b - 1 and j == 0:
            elem = matrix[i - 1][j] + matrix[0][j] + matrix[i][a - 1] + matrix[i][j + 1]
        elif i == b - 1 and j == a - 1:
            elem = matrix[i - 1][j] + matrix[0][j] + matrix[i][j - 1] + matrix[i][0]
        elif j == 0 and (i != 0 or i != b - 1):
            elem = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][a - 1] + matrix[i][j + 1]
        elif j == a - 1 and (i != 0 or i != b - 1):
            elem = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][0]
        elif i == 0 and (j != 0 or j != a - 1):
            elem = matrix[b - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]
        elif i == b - 1 and (j != 0 or j != a - 1):
            elem = matrix[i - 1][j] + matrix[0][j] + matrix[i][j - 1] + matrix[i][j + 1]
        else:
            elem = matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1]
        new_matrix_row.append(elem)
    new_matrix.append(new_matrix_row)
result_m = []
for row in new_matrix:
    result_m.append(' '.join([str(elem) for elem in row]))

a = '\n'.join([str(elem) for elem in result_m])
print(a)