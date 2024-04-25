# Author: Willie M. Bonavente
# Seatwork #3
class Employee:
#    'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary,gender):
      self.name = name
      self.salary = salary
      self.gender = gender
      Employee.empCount += 1
   
   def displayCount(self):
       return ("Total Employee: %d" % Employee.empCount)

   def displayEmployee(self):
       return ("Name: ", self.name,  "Salary: ", self.salary, "Gender: ", self.gender )


# "This would create first object of Employee class"
emp1 = Employee("Zara", 2000, "male")
# "This would create second object of Employee class"
emp2 = Employee('Manni', 5000, "female")
emp3 = Employee("Lee", 4000, "female")

# Storing Objects into sets and the category for dictionaries
data_base = {
    "names": [
        "Chopin",
        "Liszt",
        "Bach",
        "Debussy",
        "Mozart",
        "Beethoven",
        "Clara"
    ],
    "salary": [
        2000,
        3000,
        5000,
        1000,
        3400,
        3003,
        2500,
    ],
    "gender": [
        "male",
        "male",
        "male",
        "male",
        "male",
        "male",
        "female"
    ]
}

for i in range(len(data_base["names"])):
    emp = Employee(data_base["names"][i], data_base["salary"][i], data_base["gender"][i])
    recent_emp = i + 1
    count = emp.displayCount()
    print(emp.displayEmployee())
    
# Search for specific employee here
search_name = "Robert"  # Example: searching for employee named "Mozart"

for i in range(len(data_base["names"])):
    if data_base["names"][i] == search_name:
        emp = Employee(data_base["names"][i], data_base["salary"][i], data_base["gender"][i])
        recent_emp = i + 1
        count = emp.displayCount()
        print(emp.displayEmployee())
        break
else:
    print(search_name, "is not employee")
print("Recent Employee:",recent_emp)
print(count)