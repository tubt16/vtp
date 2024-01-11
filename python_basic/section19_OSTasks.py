#!/usr/bin/python3

# Add user on system
import os

userlist = ["alpha", "beta", "gamma"]

print("Adding users to system")

print("####################################")

#Loop

for user in userlist:
	exitcode = os.system("id {}" .format(user))
	if exitcode != 0:
		print("User {} does not exist. Adding it" .format(user))
		print("###############################################")
		print()
		os.system("useradd {}" .format(user))
	else:
		print("User already exist. Skipping it")
		print("#############################################")
		print()

# Add group sysad

exitcode = os.system("grep sysad /etc/group")
if exitcode != 0:
	print("Group sysad does not exist. Adding it")
	print("#############################")
	print()
	os.system("groupadd sysad")
else:
	print("Group already exist. skipping it")
	print("#############################")
	print()

# Add user in userlist to group sysad

for user in userlist:
	print("Adding user {} in the sysad group" .format(user))
	print("####################################")
	print()
	os.system("usermod -G sysad {}" .format(user))

# Add a Directory

if os.path.isdir("/opt/science_dir"):
	print("Directory already exist. skipping it")
else:
	os.mkdir("/opt/sysad_dir")

print("Assigning permission")
print("##########################")
print()

os.system("chown root:sysad /opt/sysad_dir")
os.system("chmod 777 /opt/sysad_dir")