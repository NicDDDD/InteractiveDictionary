import json
from difflib import get_close_matches

data = json.load(open("data.json", encoding= "utf8"))

def translate(word):
	word = word.lower()
	if word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys()))>0:
		index = 0
		wordList = get_close_matches(word,data.keys())
		while index != len(wordList):
			correctWord = input("Is %s your word? Input Y for yes or N for no " % wordList[index])
			if correctWord == "Y":
				return data[wordList[index]]
			else: 
				index += 1
		return "The word does not exist"
	else:
		return "The word does not exist"

word = input("What is the word you want? ")
output = translate(word)
if type(output) == list:
	for i in output:
		print(i)
else:
	print(output)