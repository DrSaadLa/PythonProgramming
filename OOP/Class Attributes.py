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
