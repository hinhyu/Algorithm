A,B,C = map(int,input().split()) #A:고정비용,B:가변비용,C:노트북비용
#A+(B*n) = C*n
#Bn = Cn
if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))