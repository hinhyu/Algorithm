#짝수를 찾아라
x = int(input())

for i in range(x):
    s = []
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            s.append(i)
    print(sum(s), min(s))