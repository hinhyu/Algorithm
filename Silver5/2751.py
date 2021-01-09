#수 정렬하기 2
n=int(input())
num=[]

for _ in range(n):
    x = int(input())
    num.append(x)

for i in sorted(num):
    print(i)