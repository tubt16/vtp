message = "lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod"

print(message)

print(message.capitalize())

Message = message.capitalize()

print(Message)

# dir() funcion 

print("########################################")

# print(dir(""))

# print(dir([]))

# print(dir(()))

# print(dir({}))

upperMessage = message.upper()

print(upperMessage)

print(upperMessage.islower())

print(upperMessage.isupper())

print(message.find("sum"))

print(message[8:11])

print("#################################")

seq1 = ("192", "168", "40", "90")

print(".".join(seq1))

print("-".join(seq1))

print("####################################")

champions = ["Vayne", "Ashe", "Aphelios", "Yasuo", "Lux"]

champions.append("Sivir")

print(champions)

champions.extend(["Darius", "Samira", "Zed"])

print(champions)

champions.insert(3, "Anivia")

print(champions)

champions.pop(0)
champions.pop(-1)
champions.pop()

print(champions)

print("#############################")

Demacia= {"Name":"Lux", "Skill":"Ultimate rainbow", "code":1024}

print(Demacia.keys())
print(Demacia.values())

Demacia.clear()

print(Demacia.keys())