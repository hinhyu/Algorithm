#세 개의 자연수 A, B, C가 주어질 때 A×B×C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

A = int(input())
B = int(input())
C = int(input())

num = A * B * C

num = str(num) #string형 배열을 만들어줌

for i in range(0, 10):

    print(num.count(str(i)))