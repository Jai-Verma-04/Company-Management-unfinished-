import Employees

class Admin:
    def __init__(self, f_name, l_name, monthly_salary):
        Employees.SalariedEmployee.__init__(self, f_name, l_name, monthly_salary)
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name+' '+self.l_name
        self.designation = "Admin Staff"

    def __str__(self):
        return Employees.Employee.__str__(self)

    def salary(self, days_worked):
        work_days = 22
        per_day_salary = self.monthly_salary/work_days
        
        try:
            assert days_worked<=22
            return round(per_day_salary*days_worked, 1)
        except AssertionError:
            return "Working days are greater than 22 in one month."

    @property
    def permissions(self):
        # Add_Admins = True
        # View_Employees = True
        # Add_Employees = True
        # Raise_Salaries = True
        # Promote_Employees = True
        # Fire_Employees = True
        # View_Messages = True
        return "1. Add Admins\n2. View Employees\n3. Add Employees\n4. Raise Salaries\n5. Promote employees\
\n6. Fire Employees\n7. View Messages\n8. Exit Program"

a = Admin("J", "V", 12000)
print(a)