A,B,C = map(int,input().split()) #A:고정비용,B:가변비용,C:노트북비용

#예를 들어 A=1,000, B=70이라고 하자. 이 경우 노트북을 한 대 생산하는 데는 총 1,070만원이 들며, 열 대 생산하는 데는 총 1,700만원이 든다.

n = int()

while n:
    if A + (B*n) < C*n:
        print(n.count())