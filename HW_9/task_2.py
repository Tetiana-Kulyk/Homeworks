class Employee:

    def __init__(self, full_name: str, age: int, position: str, salary: float):
        self.full_name = full_name
        self.age = age
        self.position = position
        self.salary = salary

    def description(self):
        """The function gives the short description of the selected employee (full name, age, position and salary)."""
        print(f'The name of the employee: {self.full_name}')
        print(f'The age of the employee: {self.age}')
        print(f'The position of the employee: {self.position}')
        print(f'The salary of the employee: {self.salary}')


if __name__ == '__main__':
    daisy = Employee("Daisy Flower", 25, 'QA Engineer', 1.505)
    daisy.description()
