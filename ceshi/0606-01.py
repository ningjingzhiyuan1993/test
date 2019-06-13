#-*- coding:UTF-8 -*-
high = input('high is:')
weight = input('weight is:')
BMI = float(weight)/float(high) ** 2
print('BMI is %.2f' % (BMI))
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
else:
    print('肥胖')
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
