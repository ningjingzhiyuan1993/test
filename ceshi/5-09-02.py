def is_opp(n):
	return  filter(lambda a : str(a) == str(a)[::-1], n)
	#return str(n) == str(n)[::-1]
def is_palindrome(n):
	return str(n) == str(n)[::-1]
	
print(is_palindrome(range(10, 1000)))
print(list(is_opp(range(10, 1000))))