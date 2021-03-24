#SuperSum 함수는 다음과 같이 정의된다.
#      SuperSum(0,n)=n (n은  모든 양의 정수)
#      SuperSum(k,n)=SuperSum(k−1,1)+SuperSum(k−1,2)+...+SuperSum(k−1,n)
#k와 n이 여러개 주어진다. SuperSum의 값을 각각 출력하시오

def supersum(k,n):
    if k == 0:
        return n
    mysum = 0
    for i in range(1, n+1):
        mysum += supersum(k-1,i)
    return mysum
 
k , n = map(int,input().split())
print(supersum(k,n))