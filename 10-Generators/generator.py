def create_cubes(n):
	result = []
	for x in range(n):
		result.append(x**3)
	return result

#print(create_cubes(10))

# This actually keeps all the values in the memory and then returns each value. Wastage of memory.
# use yield keyword to return the result. Saves memory.
	
def create_sq(num):
	for x in range(num):
		yield x**2

create_sq(20) #it actually shows a generator at a specific location

#Instead what you can do is iterate through the create_sq(55) which will return each value squared.
for val in create_sq(20):
	print(val)

def gen_fib(n):
	a = 1
	b = 1

	for i in range(n):
		yield a
		a,b = b,a+b

for num in gen_fib(10):
	print(num)

# yield creates a iteration to save memory.

print('Simple_gens')

def simple_gen():
	for x in range(3):
		yield x

for numb in simple_gen():
	print(numb) 

g = simple_gen()
print(g)


print(next(g))
print(next(g))

# next remembers next value in the yield iteration.
# if you keep going on in iteration after end then it produces error.

s = 'hello'
s_iter = iter(s)
print(next(s_iter))

# By using iter()method now string can be iterated using next

# yield() , next() and iter()