n = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        n+=i
print(n)
n = str(n)
file1 = open('pallin.txt','w')
file1.write(n)
