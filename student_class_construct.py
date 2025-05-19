class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Mandalay", "Yangon", "Taunggyi"]:
            raise ValueError("Invalid location")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"<obj>Student(name:{self.name}, house:{self.house})"

    def charm(self):
        match self.patronus:
            case "horse":
                return "🐴"
            case "elephant":
                return "🐘"
            case "dog":
                return "🐕"
            case _:
                return "..."

def main():
    student = get_student()
    print("Expetro Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()
