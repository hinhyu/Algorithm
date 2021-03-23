# 코드업 1920 : (재귀함수) 2진수 변환

#어떤 10진수 n이 주어지면 2진수로 변환해서 출력하시오.
# 예)
# 10    ----->  1010
# 0    ----->  0
# 1    ----->  1
# 2    ----->  10
# 1024    ----->  10000000000
# 이 문제는 반복문을 이용하여 풀 수 없습니다.

# 금지 키워드 : for while goto

def bin(n):
    if n < 1:
        return '0'
    elif n == 1 :
        return '1'
    elif n > 1:
        if (n%2 == 0):
            return bin(int(n/2)) + '0'
        elif (n%2 == 1):
            return bin(int(n/2)) + '1'

n = int(input())
print(bin(n))