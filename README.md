# BaekJoon_Algorithm
Studying Algorithm

## sum함수

sum(iterable)<br>
인자 : iterable한 자료형을 받으며 numeric 해야한다.<br>
즉, 리스트나 튜플 처럼 인덱스 순환 접근이 가능한 자료형이고 내부에 숫자로만 이루어져 있어야한다. 여기서 숫자는 정수, 실수 둘다 가능<br>
* iterable 객체 - 반복 가능한 객체, 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range<br>
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

## sys.stdin.readline
Python에서 입력값을 받을 때 input() 함수를 사용하지만 시간단축을 위해 sys.stdin.readline을 사용한다.<br>
입출력 속도 비교 : sys.stdin.readline > raw_input() > input()<br>
변형 : num = int(input())   ->   num = int(sys.stdin.readline()) <Br>
사용 시, import sys  선언 필요<br><br>
sys.stdin.readline : 한 라인 입력 받을 때 <br>
sys.stdin : 여러 줄 입력 받을 때 <br>
```python
for line in sys.stdin:<br>
　　print(line)
```  
## math.factorial()함수
파이썬에서는 팩토리얼값을 구하는 표준 라이브러리로 math모듈에서 factorial()함수를 제공한다. <br>
math.factorial(x)는 정수 x의 팩토리얼값을 반환<br>
음수를 인수로 전달받으면 ValueError 예외 처리를 내보냄<br>
  
## map함수
map은 리스트의 요소를 지정된 함수로 처리해주는 함수<br>
a라는 리스트를 정수형으로 바꿀 때 
```
  list(map(int, a))
```
입력값 받을 때
```
  a, b = map(int, input().split())
```
  
## Print와 Return
1. print는 출력 값을 보여주는 기능이며, 출력 값 생성을 위해 함수를 호출하게 된다.
2. return은 정의된 함수에 대한 호출이 있을 때 값을 반환시켜주는 기능이다.
3. 모든 함수는 어떤 값을 return 해야한다. 이때 함수 내에 반환값인 return이 정의되지 않은 경우 None을 결과 값으로 뱉어내게 된다.
