# strings = ["sun", "bed", "car"]
# n = 1

# def solution(strings, n):

#     answer = []
#     n_answer = []
    
#     for i in strings:
#         n_answer.append(i) #n번 째 문자 저장.
        
#     n_answer.sort()
    
#     #strings[i] == n 인지 비교

#     for j in n_answer:
#         for i in strings:
#             if strings[i] == j:
#                 answer.append(strings)

#     return answer



def solution(strings, n):
    answer = []
    s = strings
    s.sort()
    s.sort(key = lambda x : x[n])
    answer = s
    return answer

strings=["sun", "bed", "car"]
n=1