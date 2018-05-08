#!/bin/python
class Person:
	def _init_(self, name):
		self.name = name
	def sayHi(self):
		print 'Hello,my name is', self.name
p = Person( 'Swaroop' )
p.sayHi()
