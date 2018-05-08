#!/bin/python
name = 'Swaroop'

if name.startswith('Swa'):
	print 'Yes,the string starts with "Swa"'

if 'a' in name:
	print 'Yes,it contains the string "war"'

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print delimiter.join(mylist)
