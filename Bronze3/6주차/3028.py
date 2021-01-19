#창영마을
cups = [1, 0, 0]
for i in input():
    if i == 'A': cups[0], cups[1] = cups[1], cups[0] #배열 순서 바꿔줌
    elif i == 'B': cups[1], cups[2] = cups[2], cups[1]
    elif i == 'C': cups[0], cups[2] = cups[2], cups[0]

print(cups.index(1) + 1)