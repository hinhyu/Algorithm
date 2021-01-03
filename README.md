# BaekJoon_Algorithm
Studying Algorithm

<h2>sum함수</h2>

sum(iterable)<br>
인자 : iterable한 자료형을 받으며 numeric 해야한다.<br>
즉, 리스트나 튜플 처럼 인덱스 순환 접근이 가능한 자료형이고 내부에 숫자로만 이루어져 있어야한다. 여기서 숫자는 정수, 실수 둘다 가능<br>
*iterable 객체 - 반복 가능한 객체, 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range<br>
<br>
반환형 : 인자로 들어온 iterable 내부 모든 요소의 합<br>
<br>
원래는<br>
sum(iterable, start = 0)<br>
이런 모양의 함수<br>
<br>
첫번째 인자 : iterable하고 숫자데이터가 들어간 객체, 변수<br>
두번째 인자 : 처음으로 또 더해줄 숫자<br>
반환 : iterable의 합 + start 값<br>

<h2>sys.stdin.readline</h2>
Python에서 입력값을 받을 때 input() 함수를 사용하지만 시간단축을 위해 sys.stdin.readline을 사용한다.<br>
입출력 속도 비교 : sys.stdin.readline > raw_input() > input()<br>
변형 : num = int(input())   ->   num = int(sys.stdin.readline()) <Br>
사용 시, import sys  선언 필요<br><br>
sys.stdin.readline : 한 라인 입력 받을 때 <br>
sys.stdin : 여러 줄 입력 받을 때 <br>
for line in sys.stdin:<br>
　　print(line)
