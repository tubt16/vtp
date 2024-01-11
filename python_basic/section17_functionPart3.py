# Variable Length Arguments *args (Non keyword Arguments)
print("############Variable Length Arguments#############")

def order_food(min_order, *args):
	print(f"You have ordered: {min_order}")
	# print(args)
	for item in args:
		print(f"You have ordered: {item}")
	print("Enjoy the party")

order_food("Salad", "Pizza", "Biryani", "Soup")


print("###############################")

def chooseChampion(*pick):
	for item in pick:
		print(f"Your champion are: {item}")
	print("Enjoy your game")

chooseChampion("Darius", "Garen", "Lux")


# Variable Length Arguments **kwargs (keyword Arguments)

print("##########################")

import random
def time_activity(*args, **kwargs):
	print(args)

	print(kwargs)

	min = sum(args) + random.randint(0, 60)

	print(min)

	choice = random.choice(list(kwargs.keys()))
	print(choice)

	print(f"You have to spend {min} for {kwargs[choice]}")

time_activity(10, 20, 10, hobby="Game", sport="none", work="Sysadmin")

