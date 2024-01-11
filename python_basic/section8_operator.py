# Arithmetic operator
x = 2
y = 5

total = x + y

print(total)

total = x - y

print(total)

total = x * y

print(total)

total = x / 7

print(total)

print(type(total))

total = y % x

print(total)

total = y ** x

print(total)

# Comparation operators

print("##################################")

a = 30

b = 60

output = (a < b)

print(output)

output = (a >b) 
print (output)

output = (a == b)
print (output)

output = (a != b)
print(output)

output = (a >= b)
print(output)


output = (a <= b)
print(output)

# Assignment Operators

print("###################################")

c = 5

d = 11


# c += d 

# print(c)

c-=d 

print(c)

# Logical Operators

# and
# or

print("#####################################")

a = 40 
b = 60

x = 2
y = 3

output = (a < b) or (x < y) # true or true

print(output)

output = (a > b) or (x > y) # false or false

print(output)

output = (a > b) or (x < y) # false or true

print(output)

print("-------------------------------------------")

output = (a < b) and (x < y) # true and true

print(output)

output = (a > b) and (x > y) # false and false

print(output)

outpu= (a > b) and (x < y) # false an true

print(output)

print(not(output))

# Membership operator

print("###############################")

first_tuple = ("abc", "sysadmin", 16, 1.5)

ans = "sysadmin" in first_tuple

print(ans)

ans = "sysadmin" not in first_tuple

print(ans)

# Identity Operators

print("#####################################")

x = 16

y = 17

output = x is y

print(output)

output = x is not y 

print(output)