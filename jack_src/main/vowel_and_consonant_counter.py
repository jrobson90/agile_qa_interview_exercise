predefined_vowels = ["a", "e", "i", "o", "u"]


def vowel_counter(word):
    vowel_amount = 0
    list_of_letters = list(word)
    for letter in list_of_letters:
        if letter in predefined_vowels:
            vowel_amount += 1
    return vowel_amount


def consonant_counter(word):
    consonant_amount = 0
    list_of_letters = list(word)
    for letter in list_of_letters:
        if letter not in predefined_vowels:
            consonant_amount += 1
    return consonant_amount
