def star(k):
    for a in range(n // k):
        for b in range(n // k):
            for i in range(k // 3 + a * k, k // 3 + a * k + k // 3):
                for j in range(k // 3 + b * k, k // 3 + b * k + k // 3):
                    li[i][j] = ' '
    if k == 3:
        return
    star(k // 3)
n = int(input())
li = [['*'] * n for i in range(n)]

star(n)
for i in range(n):
    for j in range(n):
        print(li[i][j], end='')
    print()

#02방법

def concat(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
 
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concat(x, x)
    b = concat(x, [' '*n]*n)
 
    return a + b + a
 
print('\n'.join(star10(int(input()))))

#join 연산 : "".join(list) : 리스트에서 문자열로 합쳐줌
# time_list
# ['10','34','17']
# ':'.join(time_list)
# '10:34:17'

#zip 함수 : 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환해주는 역할
# name=['a','b']
# value=[1,2]

# # for n,v in zip(name, value):
# #     print(n,v)

# # 결과
# # a 1
# # b 2