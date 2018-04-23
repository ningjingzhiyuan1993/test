n = 0
sum = 0
while n < 10:
	n = n + 1
	if	n % 2 == 0:
		sum = sum + n
	else:
		continue
print(n,sum)