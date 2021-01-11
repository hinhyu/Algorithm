#홀수
import sys
s = []
for i in range(7):
    a = int(sys.stdin.readline())
    if (a % 2) != 0 :
        s.append(a)
if s: #if-else로 안하면 런타임에러 뜸...
    print(sum(s))
    print(min(s))
else:
    print(-1)