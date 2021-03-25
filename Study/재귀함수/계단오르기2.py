# n개의 계단이 있다.
# 어떤 사람이 계단을 오르려 하는데 이 사람은 계단을 한번에 1계단 2계단 또는 3계단씩 오를 수 있다.
# 이 사람이 계단을 오를수 있는 경우의 수를 1000으로 나눈 나머지를 구하여라

# n=int(input())

# def step(x):
#     if x==1:
#         return 1
#     if x==2:
#         return 1+step(1)
#     if x==3:
#         return 1+step(1)+step(2)
#     return step(x-1)+ step(x-2) + step(x-3)

# print(step(n)%1000)

import sys
sys.setrecursionlimit(10**7)

value = int(input())
stair_memo = {}

def function(n):

    if (n == 1):
        stair_memo[1] = 1
    elif (n == 2):
        stair_memo[2] = 2
    elif (n == 3):
        stair_memo[3] = 4
    else:
        stair_memo[n] = function(n-1) + function(n-2) + function(n-3)
    
    return stair_memo[n]

output = function(value)
answer = output % 1000
print(answer)