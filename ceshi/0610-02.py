L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s for s in L1 if isinstance(s, int)]
print(L2)

def cale(num):
    return num **2

print(cale(5))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def byname(name):
    return name[0]

def byscore(score):
    return score[1]



if __name__ == '__main__':
    print(sorted(L, key=byname))
    print(sorted(L, key=byscore))
