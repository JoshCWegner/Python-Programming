from python.Classes_and_Objects import Student #importing the Student class from the program Classes_and_Objects

student1 = Student("Miles", "Wegner", "Robotics", 3.8, False) #student creation / object storage
student2 = Student("Max", "Y", "General Studies", 4.0, False) #passed in from init fuction, calling fuction

#to print out attributes of the student1 object / access info from student1
print(student1.major)
print(student2.gpa)



