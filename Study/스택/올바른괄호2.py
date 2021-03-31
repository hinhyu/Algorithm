gwalho = list(input())
def confirm(list):
    stack = []
    for g in gwalho:
        if g == ')':
            if not len(stack):  # stack이 비어있는데 처음이 )이면 자동 탈락
                return False
            else:
                stack.pop()     #그게 아니라면)와 쌍을 이루는 거니까 제거
        else:
            stack.append(g)
    if len(stack):
        return False
    return True

if confirm(gwalho):
    print("good")
else:
    print("bad")