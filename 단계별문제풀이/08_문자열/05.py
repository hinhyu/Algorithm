# # 모두 대문자로 
# word = input().upper() 

# # 알파벳 한개만 입력된경우. 
# if len(word) == 1 : 
#     print(word) 
#     quit() 
    
# h_word = {} 

# # 알파벳별 dict 

# for i in set(word): #set은 집합함수임!!
#     h_word[i] = 0 
    
# # 알파벳별 사용횟수 
# for i in word: 
#     h_word[i] += 1 

# # value별로 dict 정렬 
# h_word = sorted(h_word.items(),reverse=True,key=lambda item:item[1]) 

# # 첫번째와 두번째가 같으면 ? 출력 
# if h_word[0][1] == h_word[1][1]: 
#     print("?") 
# else: 
#     print(h_word[0][0].upper())

#인혜
a = list(map(input().upper().count,map(chr,range(65,91)))) #a리스트 안에 문자가 숫자로 카운트?됨

m=max(a)#제일 많이 나온 문자(제일 높은 숫자)

if a.count(m)>1: #최댓값 숫자가 1보다 높으면 최댓값이 여러개라인 거임
    print("?")
else:
    print(chr(a.index(m)+65)) #다시 문자로 바꿔줌

#지원
word = input().upper()
s = list(set(word))
countArray = []
for i in s:
    countArray.append(word.count(i))

if countArray.count(max(countArray))>1: print('?')
else: print(s[countArray.index(max(countArray))])

