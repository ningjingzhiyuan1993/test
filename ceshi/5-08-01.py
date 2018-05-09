from functools import reduce

def is_odd(sit):
	return sit % 2 == 0


	
a = filter(is_odd, [1, 2, 3, 4, 5, 6])

print(list(a))