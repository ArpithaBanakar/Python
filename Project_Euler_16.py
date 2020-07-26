total = 0
a = 2**1000
result = [int(x) for x in str(a)]
print(result)
for i in range(0,len(result)):
  total = total+result[i]
print(total)
