L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name_score(t):
	return (str.lower(t[0]))

def by_num(t):
	return -t[1]

print(sorted(L, key = by_name_score))
print(sorted(L, key = by_num))