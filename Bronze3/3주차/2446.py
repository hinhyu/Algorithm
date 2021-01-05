a = int(input())
for i in range(a):
    print(" " * (i) + "*"*((2*(a-i))-1))
for i in range(2,a+1):
    print(" " * ((a+1)-i-1) + "*"*(2*i-1))