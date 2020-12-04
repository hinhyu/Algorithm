x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for j in range(3):
    if x_list.count(x_list[j]) == 1:    # x값이 저장된 리스트의 요소의 개수를 세어서 개수가 하나인 것을 출력함
        x = x_list[j]
    if y_list.count(y_list[j]) == 1:
        y = y_list[j]

print(x,y)
