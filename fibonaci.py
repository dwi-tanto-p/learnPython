fibArray=[1,1]
def fibonaci(number):
    if number <= len(fibArray):
        return fibArray[number-1]
    else:
        for i in range(2, number):
            if len(fibArray) > i :
                continue
            else:
                fib = fibArray[i-1] + fibArray[i-2]
                fibArray.append(fib)

       
        return fibArray[number-1]

# f1 = fibonaci(1)
# print(f1)
# f2 = fibonaci(2)
# print(f2)
f3 = fibonaci(6)
print(f3)

f3 = fibonaci(10)
print(f3)

def fibonaci2(number):
    fn=1
    f0=1
    f1=1
    for n in range(number):
        if n < 2:
            print("%d : %d"%(n,1))
        else:
            fn = f0+f1
            f0 = f1
            f1 = fn
            print ("%d: %d"% (n,fn))

#fibonaci2(10)