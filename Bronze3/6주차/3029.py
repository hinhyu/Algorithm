#경고 -------------> 다시 해야햄
a = list(map(int, input().split(':')))
b = list(map(int, input().split(':')))
c=[]

for i in range(2,0,-1):
    if a[i]>=b[i]:
        print((int(a[0])-int(b[0])) + ':' + (int(a[1])-int(b[1])) + ':' + (int(a[2])-int(b[2])))
    elif a[i]<b[i]:
        c.append(a[i]+60)
        c.reverse()
        a[0:2]=c[0:2]
        print((int(a[0])-int(b[0])) + ':' + (int(a[1])-int(b[1])) + ':' + (int(a[2])-int(b[2])))