class Professor:
    """Professor class."""

    def __init__(self, firstname, lastname, title):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.email = (f"{self.title.lower()}{self.firstname.lower()}"+
        f"{'_'}{self.lastname.lower()}{'@school.edu'}")

    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    
class Professor:
    """Professor class."""

    def __init__(self, firstname, lastname, title):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
    
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    def email(self):
        return (f"{self.title}{self.firstname.lower()}"+
        f"{'_'}{self.lastname.lower()}{'@school.edu'}")
    
    
    prof_1 = Professor("Saad", "Laouadi", "Dr.")
prof_2 = Professor("Nassim", "Ali", "Pro.")
prof_3 = Professor("Muhammad", "Nadir", "Ass.")

print("*"*40)
print(prof_1.email())      # This is called referencing a function 
print(prof_2.email())
print(prof_3.email())

# To change 
prof_1.title = "Pr."
prof_3.title = "Dr."

print("*"*40)
print(prof_1.email())
print(prof_2.email())
print(prof_3.email())
