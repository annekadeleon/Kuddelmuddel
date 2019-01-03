from random import randint

print("Welcome to Kuddelmuddel!")
print("Starting...")

words = [
["Mann","man"],
["Madchen" , "girl"],
["Frau" , "woman"],
["Junge" , "boy"],
["Brot" , "bread"],
["Wasser" , "water"],
["er" , "he"],
["sie" , "she"],
["es" , "it"],
["und" , "and"],
["Kind" , "child"],
["ich" , "I"],
["du" , "you"],
["bist" , "are"],
["ist" , "is"],
["bin" , "am"],
]

#list_name[column][row]
#words[word][german/english]

score = 0
count = 0

print("Score: " + str(score))

while count != 20:

	random = randint(0,15)
	german = words[random][0]
	english = words[random][1]
	answer = ""

	print("Translate this word to English: '" + german + "'")

	while answer.lower() != english.lower():
		answer = raw_input(">")
		if answer.lower() == english.lower():
			score += 1
			print("Well done!")
		else:
			print("Try again.")
	
	print("Score: " + str(score))
	count += 1
