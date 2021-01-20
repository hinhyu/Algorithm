#짝수를 찾아라
#각 테스트 데이터에 대해, 7개 자연수 중 짝수의 합과 최솟값을 공백으로 구분하여 한 줄에 하나씩 출력한다.

T = int(input())

for _ in range(T):
    input_numbers = list(map(int, input().split()))
    even_numbers = []
    
    for i in input_numbers:
        if i % 2 == 0:
            even_numbers.append(i) 
    
    print(sum(even_numbers), min(even_numbers))