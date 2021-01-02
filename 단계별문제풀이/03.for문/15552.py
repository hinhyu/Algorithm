import sys
 
t = int(input())
for i in range(t):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

#Python에서 입력값을 받을 때 input() 함수를 사용하지만 시간단축을 위해 sys.stdin.readline을 사용한다.