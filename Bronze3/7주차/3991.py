# participant = []
# a = str(input().split())
# participant.append(a)

# completion = []
# b = str(input().split())
# completion.append(b)

# c = participant.count
# for i in range(c):
#     if participant[i] == completion[i]:

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]