#To make your programs more powerful and orgaized
#data - strings, numbers / booleans
#to create your own data type
#Class - here is another data type we want to use in python - define your own data type
#real world object student
#Class - template
#OBject - actual object

class Student: #to create the student class, creating a student data type

    #this is the student datatyp
    def __init__(self, first_name, last_name, major, gpa, is_on_probation): #initialized function to map out the class
        self.first_name = first_name #object name is equal name that is passed in
        self.last_name = last_name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


