def star(k):
    for a in range(n // k):
        for b in range(n // k):
            for i in range(k // 3 + a * k, k // 3 + a * k + k // 3):
                for j in range(k // 3 + b * k, k // 3 + b * k + k // 3):
                    li[i][j] = ' '
    if k == 3:
        return
    star(k // 3)
n = int(input())
li = [['*'] * n for i in range(n)]

star(n)
for i in range(n):
    for j in range(n):
        print(li[i][j], end='')
    print()