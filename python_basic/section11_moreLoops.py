sysadmin = ["jenkins", "ansible", "bash", "docker", "python"]

for skills in sysadmin:
	print(skills)
	print(f"Get element in {skills}")
	for i in skills:
		print(i)

print("######################################")

import time
x = 2
while True:
	print("Value of x is:", x)
	print("Looping")
	x*=2
	time.sleep(3)