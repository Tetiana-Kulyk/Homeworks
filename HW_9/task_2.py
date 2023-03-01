class Employee:

    def __init__(self, full_name: str, age: int, position: str, salary: float):
        self.full_name = full_name
        self.age = age
        self.position = position
        self._salary = salary
        print(f"The account of the employee {self.full_name} is successfully created.")

    def description(self):
        """The function gives the short description of the selected employee (full name, age and position.)."""
        print(f'The name of the employee: {self.full_name}')
        print(f'The age of the employee: {self.age}')
        print(f'The position of the employee: {self.position}')

    def get_salary(self):
        """The function returns the salary of employee (for HRs and managers only)."""
        print("The salary of employee can be displayed only for HRs or employee managers. ")
        print(f"If you are an HR or manager of employee {self.full_name}, enter 'Yes, I am'")
        answer = input()
        if answer == 'Yes, I am':
            print(f"The salary of the employee {self.full_name} is {self._salary}$.")
        else:
            print("This information is private. Your account is not allowed to get it.")

    def career_advancement(self):
        """The function creates the request for position up if the employee meets all requirements."""
        print(f"Your current position is {self.position}. Please enter the position level you want to request for.")
        position_level = input()
        print(f"Please enter the number of years you are working at the position of {self.position}.")
        number_of_years = int(input())
        if self.position[0:6] == "Junior":
            if number_of_years >= 2 and position_level == 'Middle':
                print(
                    f"Your career advancement for position of the {position_level}{self.position[6:]} is successfully requested.")
            elif number_of_years < 2 and position_level != 'Middle':
                print(
                    f"Unfortunately, the career advancement for position of the {position_level}{self.position[6:]} cannot be requested yet.")
            else:
                print("Your case is not usual, please contact your manager to create the request manually.")
        elif self.position[0:6] == "Middle":
            if number_of_years >= 5 and position_level == 'Senior':
                print(
                    f"Your career advancement for position of the {position_level}{self.position[6:]} is successfully requested.")
            elif number_of_years < 5 and position_level != 'Senior':
                print(
                    f"Unfortunately, the career advancement for position of the {position_level}{self.position[6:]} cannot be requested yet.")
            else:
                print("Your case is not usual, please contact your manager to create the request manually.")


if __name__ == '__main__':
    daisy = Employee("Daisy Flower", 25, 'Junior QA Engineer', 1.005)
    daisy.description()
    daisy.get_salary()
    daisy.career_advancement()
