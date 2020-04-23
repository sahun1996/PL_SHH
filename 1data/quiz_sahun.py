## 1 ~ 100000까지 홀수

count = 1
list_odd = []

while count <= 10:
    if count % 2 != 0:
        list_odd.append(count)
        count += 1
    else:
        count += 1
        continue

print(list_odd)

## 1 ~ 100000 까지 123으로 나누어 74가 남는 숫자

count = 1
list_div = []

while count <= 10:
    if count % 123 == 74:
        list_div.append(count)
        count += 1
    else:
        count += 1
        continue

print(list_div)

## 1 ~ 100000 까지 피보나치 수

Fibo1 = 1
Fibo2 = 1
list_Fibo = []

while Fibo1 <= 10:
    n = Fibo2
    Fibo2 = Fibo1 + Fibo2
    Fibo1 = n
    list_Fibo.append(Fibo1)

print(list_Fibo)


## 1 ~ 100000 까지 모든 소수

count = 1
list_prime = []
while count <= 10:
    list_prime = []
    for n in range(1,count+1):
        if count % n == 0:
            list_prime.append(n)
        else:
            continue
    if len(list_prime) == 2:
        #print(count)
        list_prime.append(count)
        count += 1
    else:
        count += 1
print(list_prime)


## 1 ~ 100000 까지 369 게임
count = 1
while count <= 10:
    String = ""
    n = 4
    m = count
    while n >= 0:
        nPiece = m // (10**n)
        nRest = m % (10**n)
        if nPiece != 0 :
            if nPiece % 3 == 0 :
                String = String + "짝"
                n -= 1
                m = nRest
            else :
                n -= 1
                m = nRest
        else:
            n -= 1
            m = nRest
    print(count," : ",String)
    count += 1

## alphabet rangoli

list_rangoli = []
list_alphabet = ["a","b","c","d","e","f","g","h",
"i"]

n = len(list_alphabet)

while len(list_rangoli) <= (4 * n - 4):
    list_rangoli.append("-")

for i in range(1,n+1):
    for m in  range(0,i):
        list_rangoli[2*n-2 - (2*i-2) + 2 * m] = list_alphabet[-m-1]
        list_rangoli[2*n-2 + (2*i-2) - 2 * m] = list_alphabet[-m-1]
    print(list_rangoli)

for i in range(2,n+1):
    for m in  range(0,n-i+1):
        list_rangoli[2*n-2+(2*n-2*i)-2*m] = list_alphabet[-m-1]
        list_rangoli[2*n-2-(2*n-2*i)+2*m] = list_alphabet[-m-1]
    list_rangoli[2*n-2+(2*n-2*i)+2] = "-"
    list_rangoli[2*n-2-(2*n-2*i)-2] = "-"
    print(list_rangoli)


## unsortedList = [3, 6, 1, 19, 8, 47, 2, 5] 정렬

unsortedList = [3, 6, 1, 19, 8, 47, 2, 5]
sortedList = []

while len(unsortedList) >0:
    sortedList.append(min(unsortedList))
    unsortedList.remove(min(unsortedList))

unsortedList = sortedList
print(unsortedList)
