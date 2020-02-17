#can modify the class or give us specific information about those objects

class Student:
    def __init__(self, first_name, last_name, major, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.gpa = gpa
#create a class function to be used by the objects in the class
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False