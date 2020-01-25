#One.py

def func():
	print('I run in func() in one.py')
print('I am at top level')

if __name__ == "__main__":
	print('one.py Being run directly')
else:
	print('One.py Being imported')