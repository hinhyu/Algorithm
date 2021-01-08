#삼각 김밥

x,y = map(int, input().split())
const = x*1000 / y #100g당 가격에 1000을 곱하고 y로 나누면 가격이 나옴
n=int(input())

for i in range(n):
    a,b = map(int, input().split())
    cost2 = a*1000/b 
    if const>cost2:
        cost = cost2
print(round(cost,2))
