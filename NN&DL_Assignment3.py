# QUE 1

class Employee:
    # DATA MEMBER TO COUNT THE NUMBER OF EMPLOYEES
    empCount = 0

    # CONSTRUCTOR TO INITIALIZE NAME, FAMILY, SALARY, DEPARTMENT
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1    

    # FUNCTION FOR AVERAGE SALARY OF EMPLOYEE
    def avg_salary(self):
        total_salary = 0
        total_salary += float(self.salary)
        avg = total_salary / Employee.empCount
        print('Average salary of the Employee:', avg)

    # TO DISPLAY DETAILS OF EMPLOYEE
    def display(self):
        print('Employee Name:', self.name)
        print('Family Members:', self.family)
        print('Employee Annual Salary:', self.salary)
        print('Department:', self.department)
        print("==========")

# INHERITING - EMPLOYEE CLASS
class Fulltime_Employee(Employee):
    def __init__(self, name, family, salary, department, emp_type):
        Employee.__init__(self, name, family, salary, department)
        self.emp_type = emp_type

    #FUNCTION TO DISPLAY EMPLOYEE DETAILS
    def display(self):
        print("Employee Name :", self.name)
        print('Family Members:', self.family)
        print('Employee Annual Salary:', self.salary)
        print('Department:', self.department)
        print('Type of Employment :', self.emp_type)
        print("==========")


# # INSTANCE FOR FULL TIME EMPLOYEE & INSTANCES FOR EMPLOYEE CLASS
emp1 = Employee('Deepika', '6', '800000', 'Software developer')
emp2 = Fulltime_Employee('Mounica', '7', '230000', 'Software Engineer', 'Fulltime')
emp3 = Fulltime_Employee('Mahidhar', '8', '500000', 'Data Analyst', 'Fulltime')

print("Count of the Employees :", emp1.empCount)
emp1.avg_salary()
emp1.display()
emp2.display()
emp3.display()
