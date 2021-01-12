#네 번째 수 ------> 런타임에러뜸....왜ㅐㅐ?ㅙㅙㅙ??
a = list(map(int, input().split()))
b=0

if a[1]-a[0] == a[2]-a[1]:
    b = a[1]-a[0]
    a.append(a[2]+b)

print(a[3])