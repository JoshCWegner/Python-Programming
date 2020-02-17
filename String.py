#Strings are just plain text

# just printing to the console
print("Giraffe Academy")
print("Giraffe\nAcademy") #for a new line
print("Giraffe\"Academy") # to print out a quotation mark

# creating a string variable and printing it out
phrase = "Giraffe Academy"
print(phrase)

# string variable plus concatenetation
print(phrase + " is cool")

#functions
print(phrase.lower()) # to make to all lower case
print(phrase.upper()) # to make to all upper case
print(phrase.isupper()) # to check if the variable is in all upper case
print(phrase.upper().isupper()) # to change to uppercase and to check if it is in uppercase
print(len(phrase)) # to count the length of the string variable
print(phrase[3]) # to get a character in a string variable
print(phrase.index("a"))# to tell us where a specific character or phrase is in a string variable
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Elephant"))#2 parameters (values) 1. replace value 2. replacement value
