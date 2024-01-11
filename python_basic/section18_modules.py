import random

# Keyword Arguments
print("#################Keyword Arguments##################")
def vac_feedback(vac, efficacy):
	print(f"{vac} Vaccine is having {efficacy}% efficacy")
	if (efficacy > 50) and (efficacy <= 75):
		print("Seems not so efficacy. Needs more trial")
	elif (efficacy > 75) and (efficacy <= 90):
		print("Can consider this vacine")
	elif (efficacy > 90):
		print("Sure, will take the shot")
	else:
		print("Needs many more trial")

# vac_feedback("Pfizer", 95)
# vac_feedback("Moderna", 80)
# vac_feedback("unknown", 45)
# vac_feedback(efficacy = 45, vac = "unknown")

def order_food(min_order, *args):
	print(f"You have ordered: {min_order}")
	# print(args)
	for item in args:
		print(f"You have ordered: {item}")
	print("Enjoy the party")

# order_food("Salad", "Pizza", "Biryani", "Soup")

import random
def time_activity(*args, **kwargs):
	print(args)

	print(kwargs)

	min = sum(args) + random.randint(0, 60)

	print(min)

	choice = random.choice(list(kwargs.keys()))
	print(choice)

	print(f"You have to spend {min} for {kwargs[choice]}")

# time_activity(10, 20, 10, hobby="Game", sport="none", work="Sysadmin")