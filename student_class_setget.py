class Student:
    def __init__(self, name, house):
        #This self.name go to the setter method, whenever Student.name is assigned it will directly go to the setter.
        self.__name = name
        self._house = house

    def __str__(self):
        return f"<obj>Student(name:{self.name}, house:{self.house})"
    
    def eat(self):
        print("Eating")
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self.__name = name

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
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    # student.house = "Aung Ban" will go to the setter method and coditions will be placed
    # student._house = "Aung Ban" will directly assign to the house attribute, don't use _ outside class
    
    print(student.name)
    print(student.house)
    student.house = "New York"
    print(student.house)

if __name__ == "__main__":
    main()
