from statistics import median
a,b,c = map(int, input().split())
num_list = [a,b,c]
mid_num=median(num_list)
print(mid_num)