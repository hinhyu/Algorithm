# k=int(input())
# b=[]
# for i in range (k):
#     a=input().split()
#     if(a[0]=='push('):
#         b.append(int(a[1]))
#     elif(a[0]=='pop()'):
#         if(len(b)!=0):
#             b.remove(b[-1])
#     elif(a[0]=='size()'):
#         print(len(b))
#     elif(a[0]=='top()'):
#         if(len(b)!=0):
#             print(b[-1])
#         else:
#             print(-1)
#     elif(a[0]=='empty()'):
#         if(len(b)==0):
#             print("true")
#         else:
#             print("false")

import sys

# 정수 X를 스택에 넣는 연산이다.
def push(x):
    stack.append(x)

# 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

# 스택에 들어있는 정수의 개수를 출력한다.
def size():
    return len(stack)

# 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    return 0 if stack else 1

# 스택의 가장 위에 있는 정수를 출력한다. 
# 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def top():
    return stack[-1] if stack else -1

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())