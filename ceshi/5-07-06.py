from functools import reduce
def nor(s):
	return s[0].upper() + s[1:].lower()
L1 = ['adam','LISA','barT']
L2 = map(nor, L1)
L5 = list(L2)
print(L5)
