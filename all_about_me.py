

my_favorite_food = input("What is your favorite food?")
what_I_like_to_watch = input("What show or shows do you like to watch?")
what_is_your_favorite_team = input("Do you have a team you like to watch?")
do_you_have_any_kids = input("Do you have any kids?")

if do_you_have_any_kids == "yes":
    what_are_their_names = input("What are their names?")

print("My favorite food is " + my_favorite_food)
print(what_I_like_to_watch)
print(what_is_your_favorite_team + " is my favorite team")

if do_you_have_any_kids == "yes":
    print("My kids names are " + what_are_their_names)
elif do_you_have_any_kids == "no":
    print("I do not have any kids")