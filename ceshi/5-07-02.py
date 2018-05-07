from functools import reduce
def add(x,y,f):
	return f(x) + f(y)


a = add(-5,6,abs)
print(a)
max, min = min, max
print(max(1,2,5,6))
print(min(1,2,5,6))
def add(x):
	return  x * x
def sum(x,y):
	return x + y
b = map(add,[1,2,5,6])
print(type(b))
print(list(b))
print(reduce(sum,[1,2,5,6]))
