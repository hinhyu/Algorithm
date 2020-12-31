a = int(input())
for i in range(1,a+1):
    print(" " * ((a+1)-i-1) + "*"*(2*i-1))
for i in range(1,a):
    print(" " * (i) + "*"*((2*(a-i))-1))