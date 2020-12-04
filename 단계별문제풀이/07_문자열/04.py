t = int(input())
for i in range(t):
    r, s = input().split()
    for j in range(len(s)):
        print(s[j]*int(r), end='')
    print()

# T=int(input())

# result=''
# for i in range(T):
#     N, word = input().split()

#     for i in word:
#         for j in range(int(N)):
#             result+=i
    
#     result+='\n'

# print(result)