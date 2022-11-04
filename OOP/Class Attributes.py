# Class attribues
class Employee:
    def __init__(self, name, salary):
        self.name = name
        # self.salary = salary
        if salary < 1000:
            raise ValueError(f"The salary cannot be less than {1000}" \
            " Please provide a reasonable salary")
        if salary >= 1000:
             self.salary = salary
    def give_raise(self, raise_pct):
        self.salary = int(self.salary * raise_pct)
                
# Practice 

class Employee:
    BASE_SALARY = 1000 # <---- This is called Class Attribute
    def __init__(self, name, salary):
        self.name = name      # <--- Instance attribute

        if salary >= Employee.BASE_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.BASE_SALARY
