n = int(input())
a=[]


for i in range(n):
    score=0
    sum=0
    a  = input()
    for j in a:
        if j == 'O':
            score += 1
            sum += score
        else : 
            score = 0
    print(sum)
