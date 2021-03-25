#데이터의 개수가 n개가 들어오고, 
#n개의 데이터를 거꾸로 출력하는 프로그램을 작성하시오.

n = int(input())
b = list(map(int, input().split()))
b.reverse()
for i in b :
    print(i, end=' ')
