n = int(input())

for row in range(1, n+1):
    print('*' * row)
for reverse_row in range(n-1, 0, -1):
    print('*' * reverse_row)