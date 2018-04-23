
def add_list(L = None):
	if L is None:
		L = []
	L.append('END')
	return L


L = ['1','2','3']
add_list(L)
print(L)
add_list(L)
print(L)
