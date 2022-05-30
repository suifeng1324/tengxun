class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ",Salary :", self.salary)


emp1 = Employee("sz", 2000)
emp2 = Employee("nc", 3000)
emp3 = Employee("sh", 4000)
emp1.age = 7
emp1.age = 8

emp1.displayEmployee()
emp2.displayEmployee()

print(Employee.empCount)

num1 = lambda x, y: x + y

print(num1(10, 20))
