k= {'name': 'Jack', 'age': 26}

print(k['name'])
print(k.get('age'))
print(k.get('address'))

a={'name':'siva','age':18,'address':'narasaraopet'}
print(type(a))

b=a.get('age')
print(b)

b=a.keys()
print(b)

b=a.values()
print(b)

b=a.pop('age')
print(a)
