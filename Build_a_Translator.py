#Take in a phrase or word and translate it into a different language
#all vowels become "g"
#Giraffe Language

def translator(phrase):
    word_or_phrase_from_user_to_translate = ""
    for each_letter_in_the_word_or_phrase_from_user_to_translate in phrase:
        if each_letter_in_the_word_or_phrase_from_user_to_translate.lower() in "aeiou":
            if each_letter_in_the_word_or_phrase_from_user_to_translate.isupper():
                word_or_phrase_from_user_to_translate = word_or_phrase_from_user_to_translate + "G"
            else:
                word_or_phrase_from_user_to_translate = word_or_phrase_from_user_to_translate + "g"
        else:
            word_or_phrase_from_user_to_translate = word_or_phrase_from_user_to_translate + \
                                                    each_letter_in_the_word_or_phrase_from_user_to_translate
    return word_or_phrase_from_user_to_translate

print(translator(input("Enter a phrase: ")))