d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + ' = ' + v for k, v in d.items()])
L = ['HEllo', 'World', 'IBM', 'Apple']
print([s.lower() for s in L ])
print([s.upper() for s in L ])
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])