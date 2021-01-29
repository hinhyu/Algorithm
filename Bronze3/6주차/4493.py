#첫째 줄에는 테스트 케이스의 개수 t(0 < t < 1000)가 주어진다. 각 테스트 케이스의 첫째 줄에는 가위 바위 보를 한 횟수 n(0 < n < 100)이 주어진다. 
# 다음 n개의 줄에는 R, P, S가 공백으로 구분되어 주어진다. 
# R, P, S는 순서대로 바위, 보, 가위이고 첫 번째 문자는 Player 1의 선택, 두 번째 문자는 Player 2의 선택이다.
# 각 테스트 케이스에 대해서 승자를 출력한다. (Player 1 또는 Player 2) 만약, 비겼을 경우에는 TIE를 출력한다.

import sys

t=int(input())
for _ in range(t):
    n=int(input())
    sum=0
    for _ in range(n):
        a,b = map(str, sys.stdin.readline().split())
        if a==b:
            pass
        elif (a=='R' and b=='S') or (a=='P' and b=='R') or (a=='S' and b=='P'):
            sum += 1
        else:
            sum -= 1
    if sum > 0:
        print("Player 1")
    elif sum == 0:
        print("TIE")
    else:
        print("Player 2")
