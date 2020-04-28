## 피보나치를 recursion 으로
def fibonachi(n):
    if n == 1 or n == 2:
        return 1
    else :
        return fibonachi(n-1) + fibonachi(n-2)

x = int( input( "구하고자하는 fibonachi 수열의 항의 위치를 입력하세요. (정수) " ) )
print()
print( "피보나치 수열의 ",x," 번째 항은 ",fibonachi( x )," 이다." )
print()

## 하노이의 탑 최소 횟수
def hanoi(n):
    if n == 1:
        return 1
    else :
        return hanoi(n-1) + 2**(n-1)

y = int( input( "하노이의 탑의 층 수를 입력하세요. (정수) " ) )
print()
print( "하노이의 탑이 ",y," 층일 때 다른 기둥으로 옮기는 최소 횟수는 ",hanoi ( y )," 이다." )
print()

## turtle 로 몬드리안 만들기

from turtle import *

color("black", "yellow")
begin_fill()
forward(20)
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(40)
end_fill()

right(90)

color("black", "red")
begin_fill()
forward(70)
right(90)
forward(60)
right(90)
forward(50)
right(90)
forward(60)
end_fill()
backward(40)
right(180)

forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)

right(90)

color("black", "blue")
begin_fill()
forward(30)
right(90)
forward(20)
right(90)
forward(10)
right(90)
forward(20)
end_fill()

forward(40)
right(90)
forward(10)
right(90)
forward(40)
right(90)
forward(10)

right(90)

forward(50)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(10)


done()
