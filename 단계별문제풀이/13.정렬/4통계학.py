# N은 홀수

# 산술평균 : N개의 수들의 합을 N으로 나눈 값 ==> avg
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값 ==> mid
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값 ==> of
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이 ==>gap

# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
from collections import Counter

n = int(input())
i = sorted([int(input()) for _ in range(n)])

def avg(i) : #산술평균
    return round(sum(i)/n)

def mid(i) : #중앙값
    if n == 1 : return (i[0])
    else : return (i[n//2] if n%2!=0 else round((i[n//2]+i[n//2+1])/2))
    #n이 홀수일땐 가운데 값 return, n이 짝수일땐 가운데 두 개 평균

def of(i) : #최빈값
    if n==1 : return i[0]
    a = Counter(i).most_common(2)
    return (a[1][0] if a[0][1] == a[1][1] else a[0][0])

def gap(i) : #범위
    return i[n-1]-i[0] #n으로 하면 list index out of range가 뜨는데 아마 원래 리스트 범위가 0-n-1이니 그런듯..?
#m = 0
# for i in set(arr):
#     if m < arr.count(i): 
#         m = arr.count(i)
#         result = iq
print(avg(i))
print(mid(i))
print(of(i))
print(gap(i))