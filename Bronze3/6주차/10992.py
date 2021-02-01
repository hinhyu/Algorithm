n = int(input())

for a in range(1, n+1):
    if a == 1 or a == n:
        print(' ' * (n-a), '*' * (2*a-1), sep='')
    else:
        print(' ' * (n-a), '*', ' ' * ((a-1) * 2 -1), '*', sep='')