a = input()
print(*map(a.find,map(chr,range(97,123))),sep=" ")

#"문자열".find("문자") 로 "문자열"에서 "문자"의 위치를 찾을 수 있다.단, "문자"가 "문자열"에 포함되지 않을 경우 -1을 return한다.
# list(map(chr,range(97,123))) # 아스키코드 활용
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']