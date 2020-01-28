'''
Decorators are used to overcome the problem of updating a certain block of code.
If developer has to add new functionality to the function he has to add changes at specific part and make sure everything still
works perfectly. To remove the same functionality developer has to re modify the code. 
It would be convenient for programmer to just do this with some kind of ON/OFF switch which
would make it super efficient and would save a lot of time.
using @decorator tag helps with this.
'''
def func():
	return 1

func()
# prints 1

func 
# prints object type or you have a function here

def hello():
	return('Hello !!')

hello
# returns hello is a function

greet = hello
greet()
# now greet return "Hello !!"

# Is greeting pointing towards hello's memory location or is it a new function in itself
# Test by deleting hello and then printing greet()

del hello
greet()
# It will still return "Hello !!"
# greet is still pointing towards this function object
# Functions are object which cannot be passed into another object.

def hello(name = "Jenny"):
	print("Does hello() function execution.")

	def greet():
		return '\t This  is the greet function inside hello()'

hello()
# prints Does hello() function execution
# we just defined greet but not execute it yet so.

print(greet())
# scope of greet is limited only inside hello function hence it will show an error.


def hello(name = "Jenny"):
	print("Does hello() function execution.")

	def greet():
		return '\t This  is the greet function inside hello()'

	def welcome():
		return 'Welcoming you '

	print(greet())
	print(welcome())

#Output would be:
# Does hello() function execution 
# 	 	This is the greet funciton inside hello()
#		Welcoming you
 

#We can ask the function to return a function
def hello(name='Raj'):
	print('The hello() function has been executed!')

	def pushup():
		return 'Doing pushups'

	def crunches():
		return 'Doing crunches now'

	print("I am the end of hello function")

	if name == 'Raj':
		return pushup
	else:
		return crunches

my_new_func = hello('Raj')

# Output:
#The hello() function has been executed!
#I am the end of hello function

print(my_new_func())
#Output:
#Doing pushups
