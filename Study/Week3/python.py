import turtle

## 전역 변수 부분 ##

num1,num2, num3 = 0, 0, 0
swidth, sheight = 1000, 500
curX, curY = 0, 0

## 메인 코드 부분 ##

if __name__ == "__main__" :
    turtle.title("거북이로 2진수 표현하기")
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num1 = int(input("숫자1을 입력하세요: "))
    binary1 = bin(num1) #2진수로 바꾸기
    curX = swidth/2 #거북이 초기 위치 잡기
    curY = sheight/3
    print(num1)
    
    for i1 in range(len(binary1)-2) : #변환한 2진수의 개수만큼 변환
        turtle.goto(curX,curY)
        if num1 &1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else : 
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num1 >>= 1
    print(num1)


    num2 = int(input("숫자2를 입력하세요: "))
    binary2 = bin(num2)
    curX = swidth/2
    curY = sheight/5
    for i2 in range(len(binary2)-2) :
        turtle.goto(curX,curY)
        if num2 &1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else : 
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num2 >>= 1
        
    num3 = num1 & num2
    binary3 = bin(num3)
    curX = swidth/2
    curY = sheight/12
    for i3 in range(len(binary3)-2) :
        turtle.goto(curX,curY)
        if num3 &1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else : 
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        num3 >>= 1



turtle.done