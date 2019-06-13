def cale(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


L = [1, 2, 3, 4]
print(cale(L))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('tom', 20, **extra)


def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n

print(fact(5))

def fact_1(n):
    return fact_item(n, 1)

def fact_item(num, product):
    if num == 1:
        return product
    return fact_item(num - 1, num * product)

print(fact_1(5))
def move(n,a,b,c):

    if n==1:

        print(a,'-->',c)

    else:

        move(n-1,a,c,b)

        print(a,'-->',c)

        move(n-1,b,a,c)

move(3,'A','B','C')

def trim(m):
    while m[:1] == ' ':
        m = m[1:]
    while m[-1:] == ' ':
        m = m[:-1]
    return m


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

d = {'a': 1, 'b': 2, 'c': 3}

for k, v in d.items():
    print(k, ':', v)

def findMinAndMax(L):
    if not len(L):
        return None, None
    else:
        min = L[0]
        max = L[0]
        for n in L:
            if n > max:
                max = n
            if n < min:
                min = n
        return min, max

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')