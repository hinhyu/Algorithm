# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오
# 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. 
# (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 
# 연산자 우선순위는 무시

def dfs(i, current):
    global arr, op, result
    
    print(i, current)
    if i == n-1:
        result.append(current)
        return
    else:
        # +
        if op[0] > 0:
            op[0] -= 1
            dfs(i+1, current + arr[i+1])
            op[0] += 1
        # -
        if op[1] > 0:
            op[1] -= 1
            dfs(i+1, current - arr[i+1])
            op[1] += 1
        # x
        if op[2] > 0:
            op[2] -= 1
            dfs(i+1, current * arr[i+1])
            op[2] += 1
        # /
        if op[3] > 0:
            op[3] -= 1
            if current < 0:
                dfs(i+1, -1 * (abs(current) // arr[i+1]))
            else:
                dfs(i+1, current // arr[i+1])
            op[3] += 1

n = int(input())
arr = list(map(int, input().split(' ')))
op = list(map(int, input().split(' ')))

result = []

dfs(0, arr[0])
#print(result)
print(max(result))
print(min(result))