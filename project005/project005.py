# -*- coding: utf-8 -*-
"""project005.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11AVMbSxgnFsf2KurAVpdwQktcURvokig

# **loop:**

*   for 
*   while
"""

#for 

for i in range(5):
  print(i , end = ' ')

print('\n=================\n')

for i in range(2 , 7):
  print(i , end = ' ')

print('\n=================\n')

for i in range(3 , 10 , 2):
  print(i , end = ' ')

print('\n=================\n')

for i in range(10 , 3 , -3):
  print(i , end = ' ')

print('\n=================\n')

#loop without variable
for _ in range(2):
  print('hello')

#string in loop

s = 'amirreza'
v = 'aeiuo'
for i in s:
  print(i)

print('\n=================\n')

c = 0
for i in s:
  if i == 'a':
    c += 1

print('\n=================\n')

z = 0
for i in s:
  if i in v:
    z += 1
    print(i)

print('\n=================\n')
#wtf
a = [i for i in s if i in v]
print(a)

#nisted loop
for i in range(3):
  for j in range(1 , 4):
    print(j , end = ' ')
  print()

print('\n=================\n')

for i in range(2 , 5):
  for j in range(0 , i):
    print(j , end = ' ')
  print()

print('\n=================\n')

for i in range(2 , 5):
  for j in range(1 , i):
    print(j , end = ' ')
  print()

#break and continue
for i in range(6):
  if i == 3:
    break
  print(i , end = ' ')

print('\n=================\n')

for i in range(6):
  if i == 3:
    continue
  print(i , end = ' ')

print('\n=================\n')

for i in range(2 , 10):
  for j in range(2 , i):
    if i % j == 0:
      break
  else:
    print(i , end = ' ')
    
    

print('\n=================\n')

print('1' , end = ' ' )
print('2' , end = ' ' )
for i in range(2 , 10):
  for j in range(2 , i):
    if i % j == 0:
      print(i , end = ' ')
      break

#while
i = 1 
while i <= 3:
  print(i , end = ' ')
  i += 1

print('\n=================\n')

n = 5 
while n <= 9:
  print(i , end = ' ')
  n += 1

print('\n=================\n')

j = 6
while j > 2:
  print(j , end = ' ')
  j -= 1

print('\n=================\n')

s = 'abcdef'
k = 0
while True:
  if s[k] == 'd':
    break
  else:
    print(s[k] , end = ' ')
    k += 1

print('\n=================\n')

a = 0
b = 1
while a < 10:
    print(a,end=' ')  
    a = b
    b = a+b

print('\n=================\n')

a = 0
b = 1
while a < 10:
    print(a,end=' ')   
    a  , b = b , a+b

#game
import random
n = random.randint(0 , 10)
while True:
  i = int(input('Enter an integer(0 - 10)'))
  if i > n:
    print('smaller')
  elif i < n:
    print('bigger')
  else:
    print('True')
    break

print('game over')