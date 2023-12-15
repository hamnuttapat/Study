class Name:
    def __init__(self, title, firstName, lastName):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
    
    def setName(self ,t ,f, l):
        self.title = t
        self.firstName = f
        self.lastName = l

    def getFullName(self):
        return (f"{self.title} {self.firstName} {self.lastName}")
    
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month= month
        self.year= year
    
    def setDate(self, d, m, y):
        self.day = d 
        self.month = m
        self.year = y
    
    def getDate(self):
        return (f"{self.day}/{self.month}/{self.year}")
    
    def getDateBC(self):
        return (f"{self.day}/{self.month}/{int(self.year) + 543}")
    
    
class Address:
    def __init__(self, houseNo, street, district, city, country, postcode):
        self.houseNo = houseNo
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode
    
    def setAddress(self, H, st, d, c, ct, pt):
        self.houseNo = H
        self.street = st
        self.district = d
        self.city = c
        self.country = ct
        self.postcode = pt
    
    def getAddress(self):
        return (f"houseNo:{self.houseNo}, street:{self.street}, district:{self.district}, city:{self.city}, country: {self.country} postcode:{self.postcode}")
    
class Department:
    def __init__(self, description, manager, employeeList):
        self.description = description
        self.manager = manager
        self.employeeList = employeeList
        
    def addEmployee(self, employee):
        self.employeeList.append(employee)
        employee.department = self
    
    def deleteEmployee(self, employee):
        self.employeeList.remove(employee)
        employee.department = None
    
    def setManager(self, employee):
        if isinstance(employee, PermEmployee) and   employee in self.employeeList:
            self.manager = employee
            
    def printinfo(self):
        print(f"Department: {self.description}")
        print(f"Manager: {self.manager.name.getFullName() if self.manager else 'None'}")
        print("Employees:")
        for employee in self.employeeList:
            print(f"- {employee.name.getFullName()}")
    
class Person:
    def __init__(self, name, birthdate, address):
        self.name = name
        self.birthdate = birthdate
        self.address = address
    def print_info(self):
        print(f"name:{self.name.getFullName()} birthdate:{self.birthdate.getDate()}, address:{self.address.getAddress()}")


class Employee(Person):
    def __init__(self, name, birthdate, address, startDate, department):
        super().__init__(name, birthdate, address)
        self.startDate = startDate
        self.department = department
    
    def print_info(self):
        super().print_info()
        print(f"startDate:{self.startDate.getDate()} department:{self.department.description}")


class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, department, wage):
        super().__init__(name, birthdate, address, startDate, department)
        self.wage = wage
    
    def print_info(self):
        super().print_info()
        print(f"wage:{self.wage}")

class PermEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, department, salary):
        super().__init__(name, birthdate, address, startDate, department)
        self.salary = salary
    
    def print_info(self):
        super().print_info()
        print(f"salary: {self.salary}")
        
        
        

# Create Name objects
name1 = Name("Mr.", "John", "Doe")
name2 = Name("Ms.", "Jane", "Smith")

birthdate1 = Date(10, 5, 1980)
birthdate2 = Date(15, 8, 1995)

address1 = Address("123 Main St", "Downtown", "Cityville", "City", "Country", "12345")
address2 = Address("456 Elm St", "Suburbia", "Townsville", "Town", "Country", "67890")

department_hr = Department("HR Department", None, [])
department_it = Department("IT Department", None, [])

employee1 = PermEmployee(name1, birthdate1, address1, Date(1, 1, 2020), department_hr, 60000)
employee2 = PermEmployee(name2, birthdate2, address2, Date(1, 1, 2021), department_it, 70000)

department_hr.addEmployee(employee1)
department_it.addEmployee(employee2)

department_hr.setManager(employee1)
department_it.setManager(employee2)

department_hr.printinfo()
department_it.printinfo()

temp_employee = TempEmployee(Name("Mrs.", "Mary", "Johnson"), Date(20, 3, 1990), Address("789 Oak St", "Suburbia", "Townsville", "Town", "Country", "45678"), Date(1, 1, 2022), department_hr, 25)