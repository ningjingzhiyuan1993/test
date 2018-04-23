

def mul(x,y=2):
	while y > 1:
		x = x * x
		y = y - 1
	return x
	
	
	
print(mul(5,3))