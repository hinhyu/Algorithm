from collections import deque

List = list(input().split())
deq = deque(List)               #문자가 요소로된 리스트 형태
basket = deque([])
while deq:
    A = deq.popleft()       #왼쪽에서 값을 뺌
    #print('a1=',A)
    if A.isdigit():         #문자열이 숫자인지 아닌지, 숫자면 true 문자면 flase
        basket.append(A)
    else:
        #print('now=',basket,'a=',A)
        one = int(basket.pop())     #오른쪽값
        #print('one=',one)
        two = int(basket.pop())
        #print('two=',two)
        if A=="+":
            basket.append(one+two)
        elif A=="-":
                basket.append(two-one)      #후위 표기법 이어도 숫자 순서는 -> 방향
        elif A=="*":
                basket.append(one*two)
        
print(basket.pop()) #그냥 basket하면 리스트 그래도 출력