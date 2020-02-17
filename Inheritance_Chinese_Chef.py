#to have the Inheritnace_Chinese_Chef class inheriate the functionality from the Inheritance_Chef class
#you are able to use all of the functionality from the Inheritance_Chef class inside the Inheritance_Chinese_Chef class
from Inheritance_Chef import Chef

class ChineseChef(Chef):

    def make_fried_rice(self):
        print("This chef can make fried rice")
    def make_special_dish(self):
        print("The chef makes orange chicken") #to override the make_special_dish function in Inheritance_Chef class
