a=0
num_list = list(map(int,input().split()))
print(num_list)
for i in range(10000):
    if num_list[i] == 1:
        a = a+2
        print(a)