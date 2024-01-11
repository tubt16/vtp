sysad = ["jenkins", "ansible", "bash", "docker", "python"]

dev = ("nodejs", "java", ".net", "python")

staff1 = {"Name":"Rocky", "skill":"blockchain", "code":1024}

staff2 = {"Name":"Alma", "skill":"AI", "code":2048}

usr_skill = input("Enter your skills: ")

# print(usr_skill)

# Check in the database if we have this skill

if usr_skill in sysad:
	print(f"We have {usr_skill} in sysad team")
elif (usr_skill in dev):
	print(f"We have {usr_skill} in dev team")
elif (usr_skill in staff1.values()) or (usr_skill in staff2.values()):
	print(f"We have contract employees with {usr_skill} skill")
else:
	print("skill not found")