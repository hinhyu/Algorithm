#???이게 정확한 풀이가뜬다...
# a=int(input())
# b=int(input())
# print(a+b)

# 이걸 스택으로 푸는 방법이 뭔지를 더 모르겠음;;

# --> 아이디어
# 문자열로 받고 그 문자열을 하나하나 스택에 넣어서 뒤집은 다음에 더하고 10
# 10의 자리 넘어가는거 계산 처리 하고 한 다음에 다시 뒤집어서 출력... 홀리쉿
a=list(input())
b=list(input())

c = a.reverse
d = b.reverse

print(c)
print(d)

