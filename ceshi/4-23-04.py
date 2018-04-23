def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)


person('jason',21)
person('lili',21,city='beijing')
person('wang',21,gender='M',city='zheng',high='170')
