#네 번째 점
#세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

import sys

box1 = []
box2 = []

for _ in range(3):
    a,b = map(int, sys.stdin.readline().split())
    box1.append(a)
    box2.append(b)

for j in range(3):
    if box1.count(box1[j]) == 1:
        new1 = box1[j]
    if box2.count(box2[j]) == 1:
        new2 = box2[j]

print(new1,new2)