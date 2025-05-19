class Student:
    def __init__(self, name, house):
        #This self.name go to the setter method, whenever Student.name is assigned it will directly go to the setter.
        self.name = name
        self.house = house

    def __str__(self):
        return f"<obj>Student(name:{self.name}, house:{self.house})"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
    
def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
