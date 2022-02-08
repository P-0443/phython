class Employee:
    count = 0

    def __init__(self, name, desig, salary):
        self.name = name
        self.desig = desig
        self.salary = salary
        Employee.count += 1

    def displayCount(self):
            print("There are %d employees" % Employee.count)

    def displayDetails(self):
                print("Name:", self.name, ", Designation:", self.desig, ", Salary:", self.salary)


e1 = Employee("Malli", "Manager", 75000)
e2 = Employee("Msd", "Team Leader", 50000)
e3 = Employee("Rohit", "Programmer", 30000)
e4 = Employee("Virat", "Assistant", 25000)
e4.displayCount()
print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()

