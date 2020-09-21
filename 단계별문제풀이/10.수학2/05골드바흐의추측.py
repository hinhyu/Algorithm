n=int(input())
prime = []
if n%2==0:
    for i in range(1, n+1):
        if i != 1:#1이 아닌 요소(i)를 하나씩 꺼내면서 2~ i-1까지 나눠지는 수가 없을 때만을 골라낸다.
            check = True
            for j in range(2, i):
                if i % j == 0:
                    check = False
                    break
            if check:
                prime.append(i)
    if prime(i) + prime(i) == n:
        print(prime(i),prime(i))