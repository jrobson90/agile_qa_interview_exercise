from jack_src.main import vowel_and_consonant_counter


def vowel_and_consonant_calculator(words):
    user_strings = words.replace(" ", "")

    list_of_strings = user_strings.split(',')
    output = []

    if len(list_of_strings) > 4:
        print("You have entered more than 4 words. Please try again.")
    else:
        for string in list_of_strings:
            if string.isdigit():
                print("You have entered a digit. Please try again.")
            else:
                number_of_vowels = vowel_and_consonant_counter.vowel_counter(word=string)
                number_of_consonants = vowel_and_consonant_counter.consonant_counter(word=string)
                my_dict = {"word": string, "vowels": number_of_vowels, "consonants": number_of_consonants}
                output.append(my_dict)
        return output

