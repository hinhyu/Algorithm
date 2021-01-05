a = int(input())
for i in range(1,a+1):
    print(" " * ((a+1)-i-1) + "*"*(i))
for i in range(a-1,0,-1):
    print(" " * ((a+1)-i-1) + "*"*(i))