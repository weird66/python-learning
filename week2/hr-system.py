# You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title.
# Requirements:
# Create at least two Employee objects with different data.
# Call the display_info() method to show each employee’s details.
# Call the give_raise() method to increase an employee’s salary and display the updated amount.

class Employee:
    def __init__(self, name: str, salary: int, title: str):
        self.name = name
        self.salary = salary
        self.title = title
    
    def display_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}, Title: {self.title}")

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s new salary: ${self.salary}")

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def display_all_employees(self):
        for employee in self.employees:
            employee.display_info()
    def search_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

def main():
    alice = Employee("Alice", 50000, "Software Engineer")
    bob = Employee("Bob", 60000, "Project Manager")
    cate = Employee("Cate", 70000, "HR Manager")

    company = Company()
    company.add_employee(alice)
    company.add_employee(bob)
    company.add_employee(cate)

    print("Initial Employee Information:")
    company.display_all_employees()

    print("\nGiving Alice a raise...")
    alice.give_raise(5000)

    print("\nUpdated Employee Information:")
    company.display_all_employees()

    while True:
        name = input('Please input the name you want to search: ')
        employee = company.search_employee(name)
        if employee:
            employee.display_info()
            salary_raise = input('How much do you want to raise? ')
            employee.give_raise(int(salary_raise))
            print('Updated employee information:')
            employee.display_info()
            moveNext = input('Search more? y/n')
            if moveNext == 'n':
                break
        else:
            print('Not found')

if __name__ == "__main__":
   
    # main()
    main()