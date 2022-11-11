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
