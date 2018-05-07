it = iter([1,2,6,"ABC",5,7])
while True:
	try:
		x = next(it)
		print(x)
	except StopIteration:
		break
		
		