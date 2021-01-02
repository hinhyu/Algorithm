a,x = map(int, input().split())
n=list(map(int,input().split()))

for i in range(a):
    if x>n[i]:
        print(n[i],end=' ')