#This is the object to work in the Student Class assigning attributes
from Student import Student

student1= Student("Miguel", "Software Eng", 3.5, False)
student2= Student("Ramon", "System eng", 3.5, True)


print(student1.name)
print(student1.major)
print(student1.gpa)
print(student1.is_on_probation)

print(student2.name)
print(student2.major)
print(student2.gpa)
print(student2.is_on_probation)