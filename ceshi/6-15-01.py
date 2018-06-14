class A(object):
	def test(self):
		print('A.test')

class B(object):
	def test(self):
		print('B.test')
		
class C(A,B):
	def test(self):
		print('C.test')

a = C
print(a)
print(a.test)

