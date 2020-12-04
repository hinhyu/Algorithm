#Kn = K(n-1)-1 or K(n-1) or K(n-1) +1
#도착하기 바로 직전의 이동거리는 반드시 1광년
#최소한의 공간이동 장치 작동 회수를 출력한다.

#방법01
def Flymeto(d):#함수 정의
    i=1
    while(True):
        if(i**-2)-i < d and (i**2)+i >=d:
            break
        i+=1
    
    if i**2 < d:
        return i+i
    else:
        return i+i-1


T = int(input())
result = []
for i in range(T):
    x,y = map(int,input().split())

    distance = y-x
    result.append(Flymeto(distance))

for i in range(T):
    print(result[i])

#방법02
from math import sqrt

t = int(input())
dist = []

for i in range(t):
    x, y = input().split()
    dist.append(int(y)-int(x))

for dis in dist:
    n = int(sqrt(dis))
    m = n+1
    if n == 1:
        print(dis)
    elif dis >= n*m + 1:
        print(n+m)
    elif dis >= n**2 + 1:
        print(n*2)
    else:
        print(n*2-1)