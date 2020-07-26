"""a = int(input("Enter the lower limit:  "))
b = int(input("Enter the upper limit: "))
primelist = []
for i in range(a,b+1):
	if i > 1:
		for j in range(2,i//2+1):
			if (i%j) == 0:
				break
		else:
			primelist.append(i)
print(primelist)


with open('prime.txt', 'w') as f:
    for item in primelist:
        f.write("%d\n" % item)
	#print(item)
"""
"""
data = data2 = data3 = []
with open('your_file.txt') as fp:
	data = fp.read()
with open('prime.txt') as fp:
	data2 = fp.read()
#data = int(data)
#data2 = int(data2)

"""





"""
data3 = sum(int(data),int(data2))
with open ('add.txt','w') as fp:
	 fp.write(data3)

f = open('ranprime.txt', 'r')
for line in f:
	line = int(line)
	if line > 1:
		for line1 in range(2,line//2+2):
			if(line % line1) == 0:
				break
			else:
				if line1 == line//2+1: 
					with open('primecheck.txt','a') as b:
						b.write("%d\n" % line) 
					#print(line)

data = []
data2 = []
with open('your_file.txt','r') as fp:
	for k in fp:
		stripped = k.strip()
		data.append(int(stripped))
	#print(data)
with open('prime.txt','r') as fp:
	for l in fp:
		stripprime = l.strip()
		data2.append(int(stripprime))
	#print(data2)
data4 = []
mintmp = min(len(data), len(data2))
maxtmp = max(len(data), len(data2))
for k in range(0,mintmp):
	data4.append(data[k] + data2[k])
for o in range(mintmp, maxtmp):
	if len(data) > len(data2):
		data4.append(data[o])
	else:
		data4.append(data2[o])
print(data4)
with open('add.txt','a') as fp:
	fp.write(str(data4))
"""
"""
to find the nth prime!!
def isprime(n):
	if n<2:
		return "Neither prime nor composite"
	for i in range(2, int(n*0.5)+1):
		if n%i ==0:
			return False
	return True

def nthprime(n):
	numberofprimes = 0
	prime = 1
	while numberofprimes < n:
		prime += 1
		if isprime(prime):
			numberofprimes += 1
	return prime
 print(nthprime(10001))
"""
#to find sum of primes below 2 million

primelist = []
for i in range(0,2000000):
	if i > 1:
		for j in range(2,i//2+1):
			if (i%j) == 0:
				break
		else:
			primelist.append(i)
total = 0
for k in range(0,len(primelist)):
	total = total+primelist[j]
print(total)