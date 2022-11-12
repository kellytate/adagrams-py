import random

def draw_letters():

    # Load letter pool. Would be better with helper function
    # TODO try loading letter pool with dictionary
    # Also consider using probability with random to draw from 26-letter list

    # Question 1: In general is it okay to create helper functions or is it best to stick to provided functions when "following directions" is highlighted in instructions?
    # Question 2: Would it be better to create pool using given values or set up A-Z pool and change the probability of randomly choosing the letter?

    letter_pool = []
    # # add a
    # letter_pool = ['A'] * 9
    # # add b
    # letter_pool += ['B'] * 2
    # # add c
    # letter_pool += ['C'] * 2
    # # add d
    # letter_pool += ['D'] * 4
    # # add e
    # letter_pool += ['E'] * 12
    # # add f
    # letter_pool += ['F'] * 2
    # # add g
    # letter_pool += ['G'] * 3
    # # add h
    # letter_pool += ['H'] * 2
    # # add i
    # letter_pool += ['I'] * 9
    # # add j
    # letter_pool += ['J'] * 1
    # # add k
    # letter_pool += ['K'] * 1
    # # add l
    # letter_pool += ['L'] * 4
    # # add m
    # letter_pool += ['M'] * 2
    # # add n
    # letter_pool += ['N'] * 6
    # # add o
    # letter_pool += ['O'] * 8
    # # add p
    # letter_pool += ['P'] * 2
    # # add q
    # letter_pool += ['Q'] * 1
    # # add r
    # letter_pool += ['R'] * 6
    # # add s
    # letter_pool += ['S'] * 4
    # # add t
    # letter_pool += ['T'] * 6
    # # add u
    # letter_pool += ['U'] * 4
    # # add v
    # letter_pool += ['V'] * 2
    # # add w
    # letter_pool += ['W'] * 2
    # # add x
    # letter_pool += ['X'] * 1
    # # add y
    # letter_pool += ['Y'] * 2
    # # add z
    # letter_pool += ['Z'] * 1

    letter_counts = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
    }

    for letter in letter_counts:
        letter_pool += letter * (letter_counts[letter])

    # print(letter_pool)

    # Use random to randomly choose 10 letters from letter_pool
    letters_drawn = random.sample(letter_pool, 10)
    return letters_drawn


def uses_available_letters(word, letter_bank):
    valid = False
    
    word = word.upper()

    # Create dictionary of letter frequency for letter_bank
    letter_bank_count = {}

    for letter in letter_bank:
        if letter in letter_bank_count:
            letter_bank_count[letter] += 1
        else:
            letter_bank_count[letter] = 1
    
    # Create dictionary of letter frequency for word
    word_count = {}

    for letter in word:
        if letter in word_count:
            word_count[letter] += 1
        else:
            word_count[letter] = 1

    # Check that word letter frequency complies with letter_bank 
    for letter in word_count.keys():
        if letter not in letter_bank_count.keys():
            return False
        elif word_count[letter] <= letter_bank_count[letter]:
            valid = True
    
    return valid

def score_word(word):
    
    word = word.upper()

    points = 0

    score_chart = {
    'A': 1, 
    'B': 3, 
    'C': 3, 
    'D': 2, 
    'E': 1, 
    'F': 4, 
    'G': 2, 
    'H': 4, 
    'I': 1, 
    'J': 8, 
    'K': 5, 
    'L': 1, 
    'M': 3, 
    'N': 1, 
    'O': 1, 
    'P': 3, 
    'Q': 10, 
    'R': 1, 
    'S': 1, 
    'T': 1, 
    'U': 1, 
    'V': 4, 
    'W': 4, 
    'X': 8, 
    'Y': 4, 
    'Z': 10
    }

    for letter in word:
        points += score_chart[letter]

    if len(word) >= 7 and len(word) <= 10:
        points += 8

    return points

def get_highest_word_score(word_list):
    pass