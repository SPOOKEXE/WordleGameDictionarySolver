# GET ALL THE WORDLE WORDS LOOOOOOOOOOOOOL
# TRY THESE TO LOSE SOME LETTERS
# CRANES
# RITUAL
# MONKEY
# AGENCY

# You can change the amount of characters by adding extra character strings
# in the 'CURRENT_WORD' and another list in the 'Blacklist'.

# Current word unlocked, use "-" for unknown letters.
CURRENT_WORD = ["A", "-", "-", "I", "N", "-"]

# available/used letters on the keyboard (include white, yellow, green characters)
avaiable_characters = ["Q", "W", "I", "P", "A", "D", "F", "G", "H", "J", "Z", "X", "V", "B", "N"]

# Put letters that are orange in here with corrosponding spots
Blacklist = [
	[],
	["G", "I"],
	["A", "N", "D"],
	["N"],
	["A"],
	["G"]
]

# If the program says its missing enchant,
# do this below in command prompt
# pip install PyEnchant

# ========= MAIN =============

from itertools import product
from multiprocessing.dummy import Pool as ThreadPool
import enchant

base_word = "".join(CURRENT_WORD)
total_dashes = str.count(base_word, "-")
print("Missing Characters; ", total_dashes)

character_products = list(product( avaiable_characters, repeat=total_dashes ))
print("Total Mixes; ", len(character_products))

dictionary_info = enchant.Dict("en_US")

def checkPermutation( permutation_list ):
	word = base_word
	for val in list(permutation_list):
		word = word.replace("-", val, 1)
	if dictionary_info.check(word):
		print(word)

pool = ThreadPool(12)
pool.map(checkPermutation, character_products)


# potentially support https://numba.pydata.org/