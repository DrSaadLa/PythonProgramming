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


# ========================
class Professor:
    """Professor class."""

    def __init__(self, firstname, lastname, title):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
    
    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    @property
    def email(self):
        return (f"{self.title}{self.firstname.lower()}"+
        f"{'_'}{self.lastname.lower()}{'@school.edu'}")
    
prof_1 = Professor("Saad", "Laouadi", "Dr.")
prof_2 = Professor("Nassim", "Ali", "Pro.")
prof_3 = Professor("Muhammad", "Nadir", "Ass.")

print("*"*40)
print(prof_1.email)      # This is called referencing a function 
print(prof_2.email)
print(prof_3.email)
print("*"*40)

print(prof_1.fullname)      
print(prof_2.fullname)
print(prof_3.fullname)


# ====================
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
       
    # Getter method
    @property
    def get_hour(self):
        return self.hour
    @property
    def get_minute(self):
        return self.minute
    @property
    def get_second(self):
        return self.second
    @property
    def get_time(self):
        return f"{self.hour}{':'}{self.minute}{':'}{self.second}"
    
t = Time(10, 23, 45)
print(t.get_hour)
print(t.get_minute)
print(t.get_second)
print(t.get_time)
# ========================
