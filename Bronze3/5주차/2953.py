#나는 요리사다
tsum = 0
index = 0

for i in range(1, 6):
    temp = list(map(int, input().split()))
    if sum(temp) > tsum:
        tsum = sum(temp)
        index = i

print(index, tsum)