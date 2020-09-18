#Kn = K(n-1)-1 or K(n-1) or K(n-1) +1
#도착하기 바로 직전의 이동거리는 반드시 1광년
#최소한의 공간이동 장치 작동 회수를 출력한다.

t = int(input())

for _ in range(t):
    x , y = map(int,input().split()) #현재위치, 목표위치
    g = y-x #두 별 사이의 거리
    cnt = 0 #총 이동거리
    n = 1 #몇 번?
