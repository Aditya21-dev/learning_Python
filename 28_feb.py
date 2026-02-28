class Employee:

    company_name = "TechVision"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self._salary = salary

    def show_details(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("Company:", Employee.company_name)

    def calculate_bonus(self):
        return self._salary * 0.05


class Manager(Employee):

    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        return self._salary * 0.20

    def show_team_size(self):
        print("Team Size:", self.team_size)


class CEO(Employee):

    def calculate_bonus(self):
        return self._salary * 0.50

    def hire_employee(self, company, employee):
        company.add_employee(employee)

    def fire_employee(self, company, emp_id):
        company.remove_employee(emp_id)


class Company:

    def __init__(self):
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)
        print(employee.name, "added to company")

    def remove_employee(self, emp_id):
        for emp in self.employee_list:
            if emp.emp_id == emp_id:
                self.employee_list.remove(emp)
                print(emp.name, "removed from company")

    def show_all_employees(self):
        print("\nAll Employees:")
        for emp in self.employee_list:
            print(emp.emp_id, "-", emp.name)


company = Company()

ceo = CEO(1, "Adi", 200000)
manager = Manager(2, "Rahul", 100000, 5)
employee1 = Employee(3, "Riya", 50000)

ceo.hire_employee(company, manager)
ceo.hire_employee(company, employee1)

company.show_all_employees()

print("\nBonus Details:")
print("CEO Bonus:", ceo.calculate_bonus())
print("Manager Bonus:", manager.calculate_bonus())
print("Employee Bonus:", employee1.calculate_bonus())

ceo.fire_employee(company, 3)

company.show_all_employees()