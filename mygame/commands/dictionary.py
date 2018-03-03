import sys

class Dictionary():
	"""
	Check if the given word is a word or not

	Used by the make command in commands/tilebag.py
	"""
	def func(self, word):
		"Opens the CSW15 word list and checks if the given word is valid"
		with open("CSW15.txt") as word_file:
    		english_words = set(word.strip().lower() for word in word_file)

		def is_english_word(word):
    		return word.lower() in english_words

		return is_english_word(word)
			