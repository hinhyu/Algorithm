#배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

N = int(input())
A = list(map(int, str(N))) 
A.sort() #A.sort(reverse=True)로 해도ㅇㅋㅇㅋ
A.reverse()
for n in A : print(n, end="")