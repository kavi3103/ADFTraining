'''
  7.	Program to get an application (name , age , gender, salary, state, city)
'''

class Employee:
    def __init__(self,name,age , gender, salary, state, city):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.state = state
        self.city = city

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getSalary(self):
        return self.salary

    def getState(self):
        return self.state

    def getCity(self):
        return self.city

#main
name = input("Enter name")
age = int(input("Enter age"))
gender = input("Enter gender")
salary = int(input("Enter salary"))
city = input("Enter city")
state = input("Enter State")

employee = Employee(name,age,gender,salary,city,state)
print("Name: ",employee.getName())
print("Age: ",employee.getAge())
print("Gender: ",employee.getGender())
print("Salary: ",employee.getSalary())
print("City: ",employee.getCity())
print("State: ",employee.getState())