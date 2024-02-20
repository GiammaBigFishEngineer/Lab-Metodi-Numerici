import math
import numpy
import matplotlib.pyplot as plt

#exercise 1
def printArray():
    arr =  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    newArr = []
    for i in arr:
        if i < 5:
            newArr.append(i)
    print(newArr)

printArray()

#exercise 2
def common():
    myArr = []
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for i in a:
        for l in b:
            if i == l:
                myArr.append(i)
        
    print(myArr)
common()

#exercise 3
def commonList(arr):
    arr = [x for x in arr if x % 2 == 0]
    return arr

print(commonList([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]))

#exercise 4
def draw():
    for x in range(6):
        for i in range(x):
                print("* ",end='')
        print("\n")
    for x in reversed(range(5)):
        for i in range(x):
                print("* ",end='')
        print("\n")
draw()

#exercise 5
def isContained(string1, string2):
    for x in string1:
        if not x in string2:
            return False
    return True

if isContained("byZ","blueberry"):
    print("OK container")
else:
    print("not ok")
    
#exercise 6
def sumOrProd(amount1, amount2, soglia=1000):
    x = amount1*amount2
    if x < soglia:
        return x
    else:
        return amount1 + amount2

print(sumOrProd(100,200))
print(sumOrProd(100,200,50000))

#exercise 7
def sumAndProd(list):
    return sum(list),numpy.prod(list)

print(sumAndProd([1,2,3,4,5,6,7]))

#exercise 8
def quadrato(list):
    return [x**x for x in list]

def drawGraphic(x):
    plt.plot(x, quadrato(x))
    plt.show()
    
drawGraphic([0,1,2,3,4,5,6,7,8,9])