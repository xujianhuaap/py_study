#!/usr/bin/python
# coding=utf-8

import pprint
spam=0
index=0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1

while index < 5:
	print (index)
	index=index+1

for i in range(0,3):
	print('hello',i)
	
#print more arguments
print('cats', 'dogs', 'mice')

#try except
def math_div(divideBy):
	try:
		print(20/divideBy)
	except ZeroDivisionError:
		print('argument can not 0')

#div=input()		
#math_div(div)

# list 
arr = ['xu','li','feng','wang']
pprint.pprint(arr)
arr1=arr[2:]
arr.append('song')
for i in arr1:
	print(arr1.index(i),i)

del arr1[0]
arr1.remove('wang')
for i in arr1:
	print(arr1.index(i),i)
	
#dictionary
student={'name':'xu','age':23,'agender':True}
student.setdefault('funny','swimming')
for k in student.keys():
	print(k)
	
for k,v in student.items():{
	print('k'+k+'value'+str(v))
}

#strings

str='list'
print(str.capitalize())
print(str.upper())

print(str.center(20,'*'))
print(str.rstrip())

strList=['hello','jiaqianwen','love','you']
print('*'.join(strList))	 

