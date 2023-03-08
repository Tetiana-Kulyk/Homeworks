class Employee:

    def __init__(self, full_name: str, age: int, position: str, salary: float):
        self.__full_name = full_name
        self.__age = age
        self.__position = position
        self.__salary = salary
        print(f"The account of the employee {self.__full_name} is successfully created.")

    @staticmethod
    def greeting_message():
        print("We are glad to welcome you in our company! Hope this time will be the best for you. ")

    @property
    def full_name(self):
        """The function returns the full name of the selected employee."""
        return f'The name of the employee: {self.__full_name}.'

    @full_name.setter
    def full_name(self, new_name: str):
        """The function changes the name of the selected employee."""
        self.__full_name = new_name

    @property
    def age(self):
        """The function returns the age of the selected employee."""
        return f"The age of the employee: {self.__age}."

    @age.setter
    def age(self, new_age):
        """The function changes the age of the selected employee."""
        self.__age = new_age

    @property
    def salary(self):
        """The function returns the salary of employee (for HRs and managers only)."""
        print("The salary of employee can be displayed only for HRs or employee managers. ")
        print(f"If you are an HR or manager of employee {self.__full_name}, enter 'Yes, I am'")
        answer = input()
        if answer == 'Yes, I am':
            return f"The salary of the employee {self.__full_name} is {self.__salary}$."
        else:
            return "This information is private. Your account is not allowed to get it."

    @salary.setter
    def salary(self, new_salary):
        """The function returns the salary of employee (for HRs and managers only)."""
        print("The salary of employee can be displayed only for HRs or employee managers. ")
        print(f"If you are an HR or manager of employee {self.__full_name}, enter 'Yes, I am'")
        answer = input()
        if answer == 'Yes, I am':
            self.__salary = new_salary
            print(f"The salary of the employee {self.__full_name} is successfully changed.")
        else:
            print("Your account is not allowed to perform this operation.")

    @property
    def position(self):
        """The function returns the age of the selected employee."""
        return f"The position of the employee: {self.__position}."

    def career_advancement(self, desired_position: str, worked_years: int):
        """The function creates the request for position up if the employee meets all requirements."""

        if self.__position[0:6] == "Junior" and worked_years >= 2 and desired_position == 'Middle' or self.__position[
                                                                                                      0:6] == "Middle" and worked_years >= 5 and desired_position == 'Senior':
            self.__position = desired_position
            print(f"Your career advancement for position of the {desired_position} position level is approved.")
        elif self.__position[0:6] == "Junior" and worked_years < 2 and desired_position != 'Middle' or self.__position[
                                                                                                       0:6] == "Middle" and worked_years < 5 and desired_position != 'Senior':
            print(
                f"Unfortunately, the career advancement for position of the {desired_position} position level cannot be requested yet.")
        else:
            print("Your case is not usual, please contact your manager to create the request manually.")


if __name__ == '__main__':
    daisy = Employee("Daisy Flower", 25, 'Middle QA Engineer', 1.005)
    daisy.career_advancement("Senior", 5)
    print(daisy.position)
    daisy.age = 30
    print(daisy.age)
