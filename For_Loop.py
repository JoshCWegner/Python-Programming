#Loop over different collections of items
#Loop through string, array, numbers

#every letter(variable) in the string "Giraffe Academy" print out each letter
for letter in "Giraffe Academy":
    print(letter)

#Loop through the "friends" array and print out all of the elements
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

#for friend(variable - can be anything) in friends:
friends = ["Jim", "Karen", "Kevin"]
for office in friends:
    print(office)

#Loop through numbers
for index in range(5):
    #print(index) #prints out 0-10 NOT INCLUDING 10
    if index == 0:
        print("===FIRST ITERATION")
    else:
        print("===NOT FIRST===")

#Loop through a specifc range of numbers
 #   for index in range(3, 10):
 #       print(index)  #will not print out the last number in the range

#Loop through to get the length of the array
#friends = ["Jim", "Karen", "Kevin"]
##    print(friends[index]) #prints out friends[0], friends[1], friends[2]