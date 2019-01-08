class Animal(object):
	def run(self):
		print('Animal is running')
		
		
class Dog(Animal):
	def run(self):
		print('Dog is running')

class Cat(Animal):
	pass

dog = Dog()
dog.run()

print(type(dog))

l = [ x * x for x in range(1,11)]
print(l)
l1 = [m * n for m in range(1,5) for n in range(1,5)]
print(l1)
d = {'y': 'B','x': 'A',  'z': 'C' }
for k,v in d.items():
	print(k, '=', v)
L = ['Hello', 'World', 'IBM', 'Apple']
print([l2.lower() for l2 in L])
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])
