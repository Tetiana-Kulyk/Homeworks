class Company:

    def __init__(self, name: str, number_of_employees: int, country: str, year_of_creation: int):
        self.name = name
        self.number_of_employees = number_of_employees
        self.country = country
        self.year_of_creation = year_of_creation

    def company_info(self):
        """The function returns the short informational note about the created company."""
        if self.number_of_employees != 0:
            if 0 < self.number_of_employees <= 49:
                company_size = "small"
            elif 250 > self.number_of_employees >= 50:
                company_size = "medium-sized"
            elif self.number_of_employees > 250:
                company_size = "large"
        else:
            company_size = "defunct"
        print(
            f"The {self.name} company is a {company_size} enterprise, which was established in {self.year_of_creation} at {self.country}.")

    def hire_employees(self, employees_number: int):
        """The function increases the number of company employees after hiring new staff."""
        self.number_of_employees += employees_number
        print(f"The current number of the {self.name} company is {self.number_of_employees}.")

    def fire_employee(self, employees_number: int):
        """The function returns the number of company employees after the procedure of employee reduction."""
        if employees_number < self.number_of_employees:
            self.number_of_employees -= employees_number
            print(f"The current number of the {self.name} company is {self.number_of_employees}.")
        elif employees_number == self.number_of_employees:
            self.number_of_employees -= employees_number
            print(f"Unfortunately, the {self.name} company is closed, all employees are fired.")
        else:
            print(f"The {self.name} company can not fire more employees that it has!")


if __name__ == '__main__':
    NayaxRetailLTD = Company("NayaxRetailLTD", 800, "Israel", 2005)
    NayaxRetailLTD.company_info()
    NayaxRetailLTD.hire_employees(4)
    NayaxRetailLTD.fire_employee(750)
