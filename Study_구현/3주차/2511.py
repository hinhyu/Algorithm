#카드놀이
#메모리 초과 떠서 오류......

a=list(map(int,input().split()))
b=list(map(int,input().split()))
asum =0
bsum =0

for i in range(10):
    if a[i] > b[i] :
        asum += 3
    elif a[i] == b[i]:
        asum += 1
        bsum += 1
    elif a[i] < b[i]:
        bsum += 3
print(asum,bsum)
print("A") if asum>bsum else (print("B") if asum<bsum else print("D"))

