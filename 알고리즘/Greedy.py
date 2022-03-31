#거스름돈

# n = 1260
# count = 0

# array = [500, 100, 50, 10]

# for coin in array:
#     count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
#     n %= coin

# print(count)

#1이 될 때까지
#입력= 25 5 출력= 2

# n, k = map(int,input().split())

# result = 0

# while (n > 1):
#     if (n%k) == 0:
#         n = n//k
#         result += 1
#         print(n)
#     else:
#         n -= 1
#         result += 1
#         print(n)

# print("출력값",result)

#곱하기 혹은 더하기
#입력:02984 출력:576
data = input()

result = int(data[0])

for i in range(1,len(data)):
    if result == 0 or result ==1:
        result += int(data[i])
    elif (int(data[i]) == 0 or int(data[i]) == 1):
        result += int(data[i])
    else:
        result *= int(data[i])

print("출력값",result)

#모험가 길드
#입력: 5, 2 3 1 2 2 출력: 2
