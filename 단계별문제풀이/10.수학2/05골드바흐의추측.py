n=int(input())
prime = []
if n%2==0:
    for i in range(1, n+1):
        if i != 1:
            for j in range(2, i):
                if i % j == 0:
                    check = False
                    break
            if check:
                prime.append(i)
    if prime(x) + prime(y) == n:
        print(prime(x),prime(y))

#방법02
arr = [0]*10001
arr[1] = 1
for i in range(2, 98):
    for j in range(i * 2, 10001, i):
        arr[j] = 1
        
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n // 2, 1, -1):
        if arr[n - j] == 0 and arr[j] == 0:
            print(j, n - j)
            break