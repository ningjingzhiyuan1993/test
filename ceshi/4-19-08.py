d = {'name':'jake','age':23,'sex':'man'}

print(type(d))

print(d['name'])
a = d.get('nama','tom')
print(a,d)
d.pop('sex')
print(d)
