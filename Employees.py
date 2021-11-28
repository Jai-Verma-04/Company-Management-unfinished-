class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.designation = None

    @property
    def full_name(self):   
        return self.first_name+' '+self.last_name
    
    @property
    def email(self):
        return self.first_name+'.'+self.last_name+"@company.in"
    
    def salary(self, days_worked):
        work_days = 22
        per_day_salary = self.monthly_salary/work_days
        
        try:
            assert days_worked<=22
            return round(per_day_salary*days_worked, 1)
        except AssertionError:
            return "Working days are greater than 22 in one month."

    def __str__(self) -> str:
        return f"Name: {self.full_name} \nDesignation: {self.designation}\nMonthly Salary: {self.salary(22)}"
    

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, payrate):
        Employee.__init__(self, first_name, last_name)
        self.payrate = payrate
        self.designation = "Hourly Employee"

    def salary(self, no_of_hours):
        try:
            assert no_of_hours<16
            return no_of_hours*self.payrate
        except AssertionError:
            return "Working hours are more than 16!"


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, monthly_salary):
        Employee.__init__(self, first_name, last_name)
        self.monthly_salary = monthly_salary
        self.designation ="Salaried Employee"
        

class Manager(Employee):
    def __init__(self, first_name, last_name, monthly_salary):
        SalariedEmployee.__init__(self, first_name, last_name, monthly_salary)
        self.designation = "Manager"


class Executive(Employee):
    def __init__(self, first_name, last_name, monthly_salary):
        SalariedEmployee.__init__(self, first_name, last_name, monthly_salary)
        self.designation = "Executive"
    

# a = SalariedEmployee("J", "V", 100)
# print(a)