"""string = input("Enter the sring: ")
string_rev = ""
asci = []
total = 0
for i in string:
    string_rev = i + string_rev
if (string == string_rev):
    print("It is a pallindrome")
    for j in string_rev:
        a = ord(j)
        asci.append(a)
    print(asci)
        
    for k in range(0,len(asci)):
        total = total + asci[k]
    print(total)
    total =str(total)
    file1 = open('pallin.txt','w')
    file1.write(total)
else:
    print("It is not a pallindrom")"""


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

