import random

def rand():
    for i in range (0, 6):
        yield random.randint(0, 100)
    
    yield random.randint(0,10)

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a+b


for randomNumber in rand():
    print("dt = %d" % (randomNumber))
counter = 0
fibx = fib()
while counter < 30:
    print(next(fibx))
    counter+=1

