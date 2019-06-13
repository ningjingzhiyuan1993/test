# /usr/bin/env python3
#-*- coding:UTF-8 -*-

print('hello %s, this is %d' % ('mike', 10000))
a = 72
b = 85
c = (b - a)/a * 100
print('提升了%.1f%%' % c)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

inpu = input('please input age:')
age = int(inpu)
if age >= 18:
    print('adult')
elif age >= 6:
    print('age is %s' % (age))
else:
    print('kid')


