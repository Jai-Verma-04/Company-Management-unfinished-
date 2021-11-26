class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.designation = None
        self.full_name = self.first_name+' '+self.last_name
    
    @property
    def email(self):
        return self.first_name+'.'+self.last_name+"@company.in"

    def __str__(self) -> str:
        return f"Name: {self.full_name} \nDesignation: {self.designation}"


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, no_of_hours, payrate):
        Employee.__init__(self, first_name, last_name)
        self.no_of_hours = no_of_hours
        self.payrate = payrate
        self.designation = "Hourly Employee"

    @property
    def salary(self):
        assert self.no_of_hours<16
        return self.no_of_hours*self.payrate


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, monthly_salary, days_worked_in_the_month):
        Employee.__init__(self, first_name, last_name)
        self.monthly_salary = monthly_salary
        self.days_worked_in_the_month = days_worked_in_the_month
        self.designation ="Salaried Employee"

    @property
    def salary(self):
        work_days = 22
        per_day_salary = self.monthly_salary/work_days
        assert self.days_worked_in_the_month<=22
        return round(per_day_salary*self.days_worked_in_the_month, 1)


class Manager(Employee):
    def __init__(self, first_name, last_name, monthly_salary, days_worked_in_the_month):
        SalariedEmployee.__init__(self, first_name, last_name, monthly_salary, days_worked_in_the_month)
        self.designation = "Manager"
    
    @property
    def salary(self):
        work_days = 22
        per_day_salary = self.monthly_salary/work_days
        assert self.days_worked_in_the_month<=22
        return round(per_day_salary*self.days_worked_in_the_month, 1)

class Executive(Employee):
    def __init__(self, first_name, last_name, monthly_salary, days_worked_in_the_month):
        SalariedEmployee.__init__(self, first_name, last_name, monthly_salary, days_worked_in_the_month)
        self.designation = "Executive"
    
    @property
    def salary(self):
        work_days = 22
        per_day_salary = self.monthly_salary/work_days
        assert self.days_worked_in_the_month<=22
        return round(per_day_salary*self.days_worked_in_the_month, 1)

class Company:
    pass

emp = Executive("j", "v", 50000, 22)
