n = int(input())
# matrix = [[0 for j in range(n)] for i in range(n)]
# print matrix
matrix = [[0 for j in range(n)] for i in range(n)]
elem = 1

for x in range(0, int(n / 2)):
    for j in range(x, n - x):
        matrix[x][j] = elem
        elem = elem + 1
    for i in range(x + 1, n - x):
        matrix[i][n - (x + 1)] = elem
        elem = elem + 1
    for j in range(x, n - (x + 1)):
        matrix[n - (x + 1)][-j - 2] = elem
        elem = elem + 1
    for i in range(x + 1, n - (x + 1)):
        matrix[-i - 1][x] = elem
        elem = elem + 1

if n % 2 !=0:
    matrix[int(n / 2)][int(n / 2)] = n**2

result_m = []
for row in matrix:
    result_m.append(' '.join([str(elem) for elem in row]))

a = '\n'.join([str(elem) for elem in result_m])
print(a)