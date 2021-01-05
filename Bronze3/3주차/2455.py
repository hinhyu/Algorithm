#지능형기차
sum = 0
t = []
for i in range(4):
    a, b=map(int, input().split())
    sum = sum - a + b
    t.append(sum)
print(max(t))