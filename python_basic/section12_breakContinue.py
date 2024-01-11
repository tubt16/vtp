# Break Statement

for i in "SystemAdmin":
	print(i)
	if (i == "m"):
		print("Found my data")
		break
print("Out of loop")

print ("######################")

# Continue Statement

for i in "SystemAdmin":
	if (i == "m"):
		print("Found my data")
		continue
	print(f"Value of i is {i}")
print("Out of loop")
