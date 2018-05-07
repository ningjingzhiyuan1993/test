from functools import reduce

def str2float(s):
	
	def str2num(s):
		digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		return digits[s]
	
	def fun(x, y):
		return x * 10 + y
	
	def fun1(x, y):
		return x * 0.1 + y
	
	s1, s2 = s.split(sep='.')
	s2 = s2[::-1]
	print(s1, s2)
	print(type(s1))
	return reduce(fun, map(str2num, s1)) + reduce(fun1, map(str2num, s2)) * 0.1


print(str2float('125.567'))
		