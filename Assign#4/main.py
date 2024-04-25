class Student:
   studentCount = 0

   def __init__(self, name, gender, age, student_num, dept):
      self.name = name
      self.age = age
      self.gender = gender
      self.student_num = student_num
      self.dept = dept
      Student.studentCount += 1
   
   def displayCount(self):
     print("Total Students %d" % Student.studentCount)

   def displayStudent(self):
      print ("Name: ", self.name, ", Age: ", self.age, ", Gender: ", self.gender, ", Student Number: ", self.student_num)
   
   def displayDept(self):
      print ("Department: ", self.dept)

# This would create first object of Student class
stud1 = Student("Zara", "Female", 16, "2012-12345-MN-0", "Computer Science")
stud2 = Student("John", "Male", 25, "2021-32345-MN-0", "Mathematics")
stud3 = Student("Emily", "Female", 30, "2022-12345-MN-0", "Physics")
stud4 = Student("Michael", "Male", 22, "2013-12345-MN-0", "Chemistry")
stud5 = Student("Sarah", "Female", 28, "2014-54321-MN-0", "Biology")
stud6 = Student("David", "Male", 19, "2015-67890-MN-0", "English Literature")
stud7 = Student("Emma", "Female", 24, "2016-09876-MN-0", "History")
stud8 = Student("Daniel", "Male", 27, "2017-11223-MN-0", "Philosophy")
stud9 = Student("Olivia", "Female", 21, "2018-33221-MN-0", "Psychology")
stud10 = Student("James", "Male", 26, "2019-44221-MN-0", "Sociology")

stud1.displayStudent()
stud1.displayDept()
stud2.displayStudent()
stud2.displayDept()
stud3.displayStudent()
stud3.displayDept()
stud4.displayStudent()
stud4.displayDept()
stud5.displayStudent()
stud5.displayDept()
stud6.displayStudent()
stud6.displayDept()
stud7.displayStudent()
stud7.displayDept()
stud8.displayStudent()
stud8.displayDept()
stud9.displayStudent()
stud9.displayDept()
stud10.displayStudent()
stud10.displayDept()

print ("Total Students %d" % Student.studentCount)