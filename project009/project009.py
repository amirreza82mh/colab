# -*- coding: utf-8 -*-
"""project009.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sVgvQ3dcM1n7rd8Cxtw3lEgCnb33St8T

# dictionary :0
"""

d = {'brand' : 'cherry' , 'model' : 'arizo5' , 'color' : 'blue'}
print(type(d))
print(d)
print(len(d))
d['year'] = '2010'
print(d)

print('\n#####################\n')

d = dict(brand = 'cherry' , model = 'arizo5' , color = 'blue')
print(type(d))
print(d)
print(len(d))
d['year'] = '2010'
print(d)
print(d['model'])
print(d['year'])
d['brand'] = 'BMW'
print(d)

print('\n#####################\n')

#get
d = dict(brand = 'cherry' , model = 'arizo5' , color = 'blue')
x = d.get('model')
print(f'model = {x}')

x = d.get('cylinder')
print(x)

x = d.get('cylinder' , -1)
print(x)

print('\n#####################\n')

#key and value and items
d = dict(brand = 'cherry' , model = 'arizo5' , color = 'blue')
print(d.keys())
print(list(d.keys()))
print(d.values())
print(list(d.values()))
print(d.items())
print(list(d.items()))

print('\n#####################\n')

#show dictionary
for k,v in d.items():
  print(k, ':' ,v)

#function of divtionary
d = dict(brand = 'cherry' , model = 'arizo5' , color = 'blue')
x = d.pop('model')
print(x)
print(d)

print()

x = d.popitem()
print(x)
print(d)

print()

x = d.popitem()
print(x)
print(d)

del(d)

print('\n#####################\n')

a = ['x', 'y', 'x', 'z', 'y', 'x']
d = {}
print(a)
print()

for i in a:
  if i not in d:
    d[i] = 1
  else:
    d[i] += 1

for k,v in d.items():
  print(k, ':' ,v)

print('\n#####################\n')

#or
a = ['x', 'y', 'x', 'z', 'y', 'x']
d = {}
print(a)
print()
for i in a:
  d[i] = d.get(i , 0) + 1

for k,v in d.items():
  print(k, ':' ,v)

print('\n#####################\n')

#copy
b = d.copy()
print(b)
print()
for k,v in b.items():
  print(k, ':' ,v)

#Ex1
s = 'abfgbfdcdcbaaak'
d = {}

for i in s:
  d[i] = d.get(i , 0) + 1
print(d)
print()

for k,v in d.items():
  print(k, ':' ,v)

print('\n#####################\n')

#Ex2
line = 'a dictionary is a datastructure.'
d = {}
s = line.split()
print(s)
print()
for i in s:
  d[i] = d.get(i , 0) + 1
print(d)

print('\n#####################\n')

#Ex3
d = {'a': 4, 'b': 3, 'f': 2, 'g': 1, 'd': 2, 'c': 2, 'k': 1}
print(d)
s = 0
for i in d:
  s += d[i]
print(f'sum = {s}')
#or
print(f'sum with secound way = {sum(d.values())}')

#sort
d = {'a': 4, 'b': 3, 'f': 2, 'g': 1, 'd': 2, 'c': 2, 'k': 1}
print(f'unsorted dictionary : {d}')
import operator
k = operator.itemgetter(1)
print('sorted dictionary : ' , end = '')
print(sorted(d.items() , key = k))

print('\n#####################\n')

#sorted with key
d = {'a': 4, 'b': 3, 'f': 2, 'g': 1, 'd': 2, 'c': 2, 'k': 1}
print(f'unsorted dictionary : {d}')
k = operator.itemgetter(0)
print('sorted dictionary : ' , end = '')
print(sorted(d.items() , key = k))

print('\n#####################\n')

#Ex
num ={
    'ali' : [12,13,8],
    'sara': [15,7,14],
    'taha': [5,18,13]
}
d = {k : sorted(v) for k,v in num.items()}
for k,v in d.items():
  print(k, ':' ,v)  

print('\n#####################\n')

#combine
d1 = {'x' : 3 , 'y' : 2 , 'z' : 1}
d2 = {'w' : 8 , 't' : 7} 
d = {}

d = d1.copy()
d.update(d2)
print(d)
print()
for k,v in d.items():
  print(k, ':' ,v)
print('\n#####################\n')
#or
d = {}
for i in (d1 , d2):
  d.update(i)
print(d)
print()
for k,v in d.items():
  print(k, ':' ,v)
print('\n#####################\n')
#or
d = {**d1 , **d2}
print(d)
print()
for k,v in d.items():
  print(k, ':' ,v)