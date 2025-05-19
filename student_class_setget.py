class Student:
    def __init__(self, name, house):
        #This self.name go to the setter method, whenever Student.name is assigned it will directly go to the setter.
        self.name = name
        self.house = house

    def __str__(self):
        return f"<obj>Student(name:{self.name}, house:{self.house})"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        #To differentiate between function house and variable house use self._house
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Mandalay", "Yangon", "Taunggyi"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    # student.house = "Aung Ban" will go to the setter method and coditions will be placed
    # student._house = "Aung Ban" will directly assign to the house attribute, don't use _ outside class
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
