#첫째 줄에는 별 2×N-1개, 둘째 줄에는 별 2×N-3개, ..., N번째 줄에는 별 1개를 찍는 문제
a = int(input())
for i in range(a):
    print(" " * (i) + "*"*((2*(a-i))-1))