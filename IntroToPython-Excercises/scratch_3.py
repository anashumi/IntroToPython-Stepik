n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]

for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = - 1