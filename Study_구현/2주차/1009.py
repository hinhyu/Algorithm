n=int(input())
for i in range(n):
    a,b = map(int,input().split(" "))
    d = list(str(a**b))
    print(d[-1])

#시간초과뜸......