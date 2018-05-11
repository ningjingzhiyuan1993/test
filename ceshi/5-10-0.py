i = 0
def sumNum():
	def counter():
		global i
		i += 1
		return i
	return counter

f = sumNum()
print(f())
print(f())
print(f())
print(f())
print(f())