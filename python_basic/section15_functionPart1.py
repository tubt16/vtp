def sum(arg1, arg2):
	total = arg1 + arg2
	return total

output = sum(10, 20)

print(output)

print(sum(20,60))

print("############################")

def summ(arg1, arg2):
	total = arg1 + arg2
	print(total)

summ(30, 40)

print(summ(80,40))

print("#############################")

def add(arg):
	x = 0
	for i in arg:
		x+=i
	return x

out = add([1,2,3])
print(out)

# add([10,20], [30,50])

#Default Argument
print("###################################")

def greeting(msg="Morning"):
	print(f"Good {msg}")
	print("Welcome to my function")

greeting()

greeting("Evening")