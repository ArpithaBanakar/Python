fib=[0,1]
i = 2
while i<10000:
    fib_new = fib[i-1]+fib[i-2]
    if len(str(fib_new))==1000:
        break
    else:
        fib.append(fib_new)
    i = i+1
print i
