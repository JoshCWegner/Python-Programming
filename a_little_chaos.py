from random import randrange

random_number_range = randrange(1,100)
fifty_random_number_range = randrange(50,51)

print("Below is random result of a number between 1-100")
print("Here I am storing a random result === " + str(random_number_range) +
      " === in the variable: random_number_range")

print("Here are a bunch of numbers between 1-100")

print(str(randrange(1,100)) + ",", end="")
print(str(randrange(1,100)) + ",", end="")
print(str(randrange(1,100)) + ",", end="")
print(str(randrange(1,100)) + ",", end="")
print(str(randrange(1,100)))



