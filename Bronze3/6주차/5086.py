#첫 번째 숫자가 두 번째 숫자의 약수이다. factor 
#첫 번째 숫자가 두 번째 숫자의 배수이다. multiple
#첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다. neither

import sys

while True:
    a,b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')
    
    