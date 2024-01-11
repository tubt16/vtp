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
vac_feedback(efficacy = 45, vac = "unknown")


