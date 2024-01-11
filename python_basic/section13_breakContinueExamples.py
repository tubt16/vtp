import random

vaccine = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]

# random.shuffle(vaccine)

# print(vaccine)

lucky = random.choice(vaccine)

# print(lucky)

print("###############################")

for vac in vaccine:
	print(f"******Testing vaccine {vac}")
	if(vac == lucky):
		print("#################################")
		print(f"{lucky} vaccine, Test SUCCESS")
		print("#################################")
		print()
		break
		# continue
	print("---------------------------")
	print("Test fail")
	print("---------------------------")
	print()