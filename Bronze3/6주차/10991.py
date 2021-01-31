#별찍기-16
a = int(input())
for i in range(1,a+1):
    print(" " * ((a+1)-i-1) + "* "*(i))