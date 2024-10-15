class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.id = emp_id
        self.salary = salary
        self.department = department

    def calculate_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))

    def assign_department(self, emp_department):
        self.department = emp_department

    def print_employee_details(self):
        print("Name: ", self.name)
        print("ID: ", self.id)
        print("Salary: ", self.salary)
        print("Department: ", self.department)


employee1 = Employee("Raki", "E7876", 75000, "MANAGER")
employee2 = Employee("Rohit", "E7499", 45000, "MEDIA SERVICES")
employee3 = Employee("Aadhi", "E7900", 50000, "QA")
employee4 = Employee("Reena", "E7698", 55000, "DEVOPS")

employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()
employee4.print_employee_details()

employee2.calculate_salary(45000, 52)
employee4.calculate_salary(45000, 60)
