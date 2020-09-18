
# 나눠지는 수가 존재하면 더 이상 소수가 아니므로, break 
# check를 이용하여 나눠지는 수가 있을 때만 출력용 배열에 append 하여 합과 첫 값을 출력하거나,
# 아무 것도 없을 때는 -1을 출력

M = int(input())
N = int(input())
prime = []
for i in range(M, N+1):
    if i != 1:#1이 아닌 요소(i)를 하나씩 꺼내면서 2~ i-1까지 나눠지는 수가 없을 때만을 골라낸다.
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))