class Company:

    def __init__(self, name: str, number_of_employees: int, country: str, year_of_creation: int):
        self.__name = name
        self.__number_of_employees = number_of_employees
        self.__country = country
        self.__year_of_creation = year_of_creation

    @property
    def name(self):
        """The function returns the name of the created company."""
        return self.__name

    @name.setter
    def name(self, new_name):
        """The function changes the name of the created company."""
        self.__name = new_name

    @property
    def country(self):
        """The function returns the country name where the company was established."""
        return self.__country

    @country.setter
    def country(self, new_country_name):
        """The function changes the country name where the company was established."""
        self.__country = new_country_name

    @property
    def year_of_creation(self):
        """The function returns the year when the company was established."""
        return self.__year_of_creation

    @year_of_creation.setter
    def year_of_creation(self, new_year_of_creation):
        """The function changes the year when the company was established."""
        self.__year_of_creation = new_year_of_creation

    def company_info(self):
        """The function returns the short informational note about the created company."""
        if self.__number_of_employees != 0:
            if 0 < self.__number_of_employees <= 49:
                company_size = "small"
            elif 250 > self.__number_of_employees >= 50:
                company_size = "medium-sized"
            elif self.__number_of_employees > 250:
                company_size = "large"
        else:
            company_size = "defunct"
        print(
            f"The {self.__name} company is a {company_size} enterprise, which was established in {self.__year_of_creation} year at {self.__country}.")

    def hire_employees(self, employees_number: int):
        """The function increases the number of company employees after hiring new staff."""
        self.__number_of_employees += employees_number
        print(f"The current number of the {self.__name} company is {self.__number_of_employees}.")

    def fire_employee(self, employees_number: int):
        """The function returns the number of company employees after the procedure of employee reduction."""
        if employees_number < self.__number_of_employees:
            self.__number_of_employees -= employees_number
            print(f"The current number of the {self.__name} company is {self.__number_of_employees}.")
        elif employees_number == self.__number_of_employees:
            self.__number_of_employees -= employees_number
            print(f"Unfortunately, the {self.__name} company is closed, all employees are fired.")
        else:
            print(f"The {self.__name} company can not fire more employees that it has!")


if __name__ == '__main__':
    nayax_retail_ltd = Company("NayaxRetailLTD", 800, "Israel", 2005)
    nayax_retail_ltd.year_of_creation = 2003
    print(nayax_retail_ltd.year_of_creation)
    nayax_retail_ltd.name = "Nayax Retail"
    print(nayax_retail_ltd.name)
    nayax_retail_ltd.country = "Ukraine"
    print(nayax_retail_ltd.country)
    nayax_retail_ltd.company_info()
    nayax_retail_ltd.hire_employees(4)
    nayax_retail_ltd.fire_employee(750)
