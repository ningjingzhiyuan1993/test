import os
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'abc' for n in '123'])
print([d for d in os.listdir()])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
	print(k, '=',  v)
