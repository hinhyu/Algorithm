n = int(input())
location=[0,1,0,0] #list index out of range뜨는거 방지
for i in range(n):
  a,b = map(int,input().split(" "))
  if location[a] == 1 or location[b] == 1:
        temp = location[a]
        location[a] = location[b]
        location[b] = temp

print(location.index(1))