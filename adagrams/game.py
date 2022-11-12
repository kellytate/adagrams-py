import random

def draw_letters():

    # Load letter pool. Would be better with helper function
    # TODO try loading letter pool with dictionary
    # Also consider using probability with random to draw from 26-letter list

    # Question 1: In general is it okay to create helper functions or is it best to stick to provided functions when "following directions" is highlighted in instructions?
    # Question 2: Would it be better to create pool using given values or set up A-Z pool and change the probability of randomly choosing the letter?

    letter_pool = []
    # add a
    letter_pool = ['A'] * 9
    # add b
    letter_pool += ['B'] * 2
    # add c
    letter_pool += ['C'] * 2
    # add d
    letter_pool += ['D'] * 4
    # add e
    letter_pool += ['E'] * 12
    # add f
    letter_pool += ['F'] * 2
    # add g
    letter_pool += ['G'] * 3
    # add h
    letter_pool += ['H'] * 2
    # add i
    letter_pool += ['I'] * 9
    # add j
    letter_pool += ['J'] * 1
    # add k
    letter_pool += ['K'] * 1
    # add l
    letter_pool += ['L'] * 4
    # add m
    letter_pool += ['M'] * 2
    # add n
    letter_pool += ['N'] * 6
    # add o
    letter_pool += ['O'] * 8
    # add p
    letter_pool += ['P'] * 2
    # add q
    letter_pool += ['Q'] * 1
    # add r
    letter_pool += ['R'] * 6
    # add s
    letter_pool += ['S'] * 4
    # add t
    letter_pool += ['T'] * 6
    # add u
    letter_pool += ['U'] * 4
    # add v
    letter_pool += ['V'] * 2
    # add w
    letter_pool += ['W'] * 2
    # add x
    letter_pool += ['X'] * 1
    # add y
    letter_pool += ['Y'] * 2
    # add z
    letter_pool += ['Z'] * 1


    # Use random to randomly choose 10 letters from letter_pool
    letters_drawn = random.sample(letter_pool, 10)
    return letters_drawn

draw_letters()


def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass