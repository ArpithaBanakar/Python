#Natural number addition that are divisible by 3 or 5
"""n = 0
for i in range(1,1000):
    if i%3 == 0 or i%5 == 0:
        n+=i
print(n)
n = str(n)
file1 = open('pallin.txt','w')
file1.write(n)"""

#Even Fibnocicci number
"""total = 0
a = 1
b = 1
h = 0
while h<=4000000:
    if h%2 ==0:
        total+= h
    a = b
    b = h
    h = a+b
print(total)"""

#greatest prime factor
"""def findLargestPrimeFactor(n):
  primeFactor = 1
  i = 2

  while i <= n / i:
    if n % i == 0:
      primeFactor = i
      n /= i
    else:
      i += 1

  if primeFactor < n: primeFactor = int(n)

  return primeFactor

print(findLargestPrimeFactor(600851475143))"""

#To find the smallest multiple
"""def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i
print(smallest_multiple(20))"""

#sum and square of first 100 numbers
"""f = 0
g = 0
for i in range(0,101):
   f+= i
   g = f*f
print(g)

s = 0
sum=[]
for i in range(0,101):
  sum.append(i*i)
for j in range(0,len(sum)):
  s = s+sum[j]
print(s)

difference = g - s
print(difference)"""

#pythogorean triplet:
"""
def pythagorean():
  for a in range(1,1000):
    for b in range(1,1000):
      c = 1000 - a - b
      if (a**2+b**2) == c**2:
        print(a*b*c)
pythagorean()"""

#Largest Collatz sequence
"""def collatz(n):
  counter = 1
  while n>1:
    if n%2 == 0:
      n = n/2
      counter+=1
    else:
      n = 3*n + 1
      counter+=1
    if n==1:
      return counter
largest_num = 0
large_seq = 0
for i in xrange(1000000,1,-1):
  n = collatz(i)    
  if n > large_seq:
    largest_num = i
    large_seq = n
print(largest_num)"""

#power digit sum
total = 0
a = 2**1000
result = [int(x) for x in str(a)]
print(result)
for i in range(0,len(result)):
  total = total+result[i]
print(total)







  