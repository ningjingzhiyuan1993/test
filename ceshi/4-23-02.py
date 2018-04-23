def calc(*num):
	sum = 0
	for i in num:
		sum = sum + i * i
	return sum

print(calc(1,2,3))
print(calc(1,2,3))
print(calc())