class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name.")
        self.name = name
    
    def Eat(self):
        print("Bread")

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def Eat(self):
        print("Rice")

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...

class Staff(Wizard):
    def Eat(self):
        print("Wheat")
    ...


wizard = Wizard("John")
student = Student("Harry", "Gryffindor")
professor = Professor("Snake", "Defense")
staff = Staff("Nuel")
student.Eat()
professor.Eat()
staff.Eat()
