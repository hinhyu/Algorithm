# 01. 배열이 하나씩 늘어남
# 02. 홀수번 배열 : 분자 감소, 분모 증가
# 03. 짝수번 배열 : 분자 증가, 분모 감소

num = int(input())
up = []   #     분모
down = [] #     분자

for i in range(1, num+1):
    if i % 2 == 0:
        # 짝수일 경우
        up += [j for j in range(1, i+1)]
        down += [j for j in range(i, 0, -1)]
    else:
        # 홀수일 경우
        down += [j for j in range(1, i+1)]
        up += [j for j in range(i, 0, -1)]

    if len(up) >= num:
        print(str(up[num-1])+'/'+str(down[num-1]))
        break