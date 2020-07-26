def triangle(n):
    return sum([i for i in range(1, n+1)])
j = 0
n = 0
divisiors = 0
while divisiors <= 500:
    divisiors = 0
    j+=1
    n = triangle(j)
    i = 1
    while i <= n**0.5:
        if n%i ==0:
            divisiors +=1
        i+=1
    divisiors*=2
print(n)
