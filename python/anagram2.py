# Don't forget to run the tests (and create some of your own)
def anagrams_for(word, list_of_words):
		matches = []

		# Loops through each word in the list of words
		# Then calls the match function to see if words match
		for each in list_of_words:
			if(is_character_match(word, each)):
				matches.append(each)

		return matches


def is_character_match(string1, string2):
	# create 2 lists of all characters except for white spaces
	x = [i.lower() for i in string1 if i!=' ']	
	y = [j.lower() for j in string2 if j!=' ']

	# Sort the two lists
	sorted_x = sorted(x)
	sorted_y = sorted(y)
	
	# Compare the two lists
	if(sorted_x == sorted_y):
		return True
	else:
		return False


# list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]
# print(anagrams_for("threads", list_of_words))