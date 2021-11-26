class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def email(self):
        return self.first_name+'.'+self.last_name+"@company.in"

    def __str__(self) -> str:
        return str(self.first_name)+' '+str(self.last_name)


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, no_of_hours, payrate):
        Employee.__init__(self, first_name, last_name)
        self.no_of_hours = no_of_hours
        self.payrate = payrate

    @property
    def salary(self):
        return self.no_of_hours*self.payrate

class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, monthly_salary, days_worked_in_the_month):
        Employee.__init__(self, first_name, last_name)
        self.monthly_salary = monthly_salary
        self.days_worked_in_the_month = days_worked_in_the_month

    @property
    def salary(self):
        work_days = 22
        per_day_salary = self.monthly_salary/work_days
        return round(per_day_salary*self.days_worked_in_the_month, 1)

class Manager(Employee):
    pass

class Executive(Employee):
    pass

class Company:
    pass

emp = SalariedEmployee("j", "v", 35000, 12)
print(emp.salary)