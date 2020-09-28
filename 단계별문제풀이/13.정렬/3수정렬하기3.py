import sys
 
n = int(sys.stdin.readline())
 
num_list=[]
result_list=[0 for _ in range(10001)]   #받을수의 최대값에 따라 배열을 만든다.
 
for i in range(n):
    result_list[int(sys.stdin.readline())]+=1

for i in range(len(result_list)):
    for j in range(result_list[i]):
        print(i)