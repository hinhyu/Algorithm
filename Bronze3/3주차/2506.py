#점수계산
total=0
sum=0
n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    if a[i] == 1:
        sum += 1
        total += sum
    elif a[i] == 0:
        sum = 0
print(total)