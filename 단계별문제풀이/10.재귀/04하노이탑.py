def hanoi(n,start,mid,end):
    if n==1:
        print(start, end)
 
    else:               #다음 원판을 옮기기 위해선
        hanoi(n-1,start,end,mid)    #이전완성단계 에서
        print(start, end)           #제일아래에 들어갈 원판을 옮기고
        hanoi(n-1,mid,start,end)    #이전 단계에서 했던방식을  통해 제일 아래에 들어갈 원판 위에 다시쌓는다.
        
        
n=int(input())
sum=1
for i in range(n-1):    #총옮길 횟수는 따로 계산
    sum=sum*2+1     #1, 3, 7, 15로 늘어감 ==> 2배+1만큼 늘어남
print(sum)  #총횟수 출력
hanoi(n,1,2,3)  
