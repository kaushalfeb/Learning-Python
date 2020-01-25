#Two.py	
import One

print('Top level in Two.py')

One.func()

if __name__ =="__main__":
	print('Two.py is being run directly')
else:
	print('Two.py is imported')