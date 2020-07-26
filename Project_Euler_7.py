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
