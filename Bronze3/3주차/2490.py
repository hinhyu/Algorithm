#윷놀이
for i in range(3):
    n = tuple(map(int, input().split()))
    if sum(n)==0: 
        print('D')
    elif sum(n)==1: 
        print('C')
    elif sum(n)==2: 
        print('B')
    elif sum(n)==3: 
        print('A')
    elif sum(n)==4: 
        print('E')