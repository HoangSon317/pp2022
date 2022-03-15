Number_student = int(input("Enter number student in class : "))
print("Number student in class is :", Number_student)
list_student = {}
for i in range(Number_student):
   a1 = input('Student ID: ')
   b1 = input('Name of student: ')
   c1 = input('Date of birth is: ')
   thislist =list((a1,b1,c1))
   print(thislist)

Number_course = int(input("Enter number of course  : "))
print("Number of course :", Number_course)
list_course = {}
for i in range(Number_course):
   a2 = input('CourseID: ')
   b2 = input('Name of course: ')
   print(a1,b2)
   thislist =list((a1,b2))
   print(thislist)
