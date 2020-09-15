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
        if j+1 > a-1:
            matrix_elem_right = matrix[i][0]
        else:
            matrix_elem_right = matrix[i][j+1]

        if j - 1 < 0:
            matrix_elem_left = matrix[i][-1]
        else:
            matrix_elem_left = matrix[i][j - 1]


        new_matrix_elem = matrix_elem_left + matrix_elem_right

        new_matrix_row.append( new_matrix_elem)
    new_matrix.append(new_matrix_row)
print new_matrix