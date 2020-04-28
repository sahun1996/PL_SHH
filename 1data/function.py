def motorAngle(sensorInput):
    angle = sensorInput * 180
    return angle

print( motorAngle( motorAngle( 0.5 ) ) )

def sensor():
    a = float( input() )
    return a

## built in function
print ( motorAngle( sensor() ) )

print("wow")

# b = Input()
# print(b)

## return value 없는거
def sayHi(words = "happy"):
    print(words)

sayHi("merry")

print(" input 값이 없을 수도 있다. 없으면 에러가 ")
print(" 나기때문에 happy 라는 기본값을 넣어줬다. ")

def eStop (code):
    if (code == 0 ):
        return "stop!!!"
    else:
        return "move"

print( eStop(0))

## recursion

def factorial(n):
    answer = 1
    while n > 0:
        answer *= n
        n -= 1
    return answer

print(factorial(5))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print( factorial(7) )
print( fact(7) )
