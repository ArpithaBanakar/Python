largestpallin = 0
def Ispallin(n):
    pallin = str(n)
    if pallin == pallin[::-1]:
        return 1
    else:
        return 0    
for i in range(100,1000):
    for j in range(100,1000):
        if Ispallin(i*j) == 1 and (i*j) > largestpallin:
            largestpallin = (i*j)
print(largestpallin)
