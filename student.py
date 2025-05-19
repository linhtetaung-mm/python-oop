#once assigned tuple, you can't change its assigned value.
#student value can't be change

def main():
    student = get_student()
    print(f"{student[0]} is from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) # returning the tuple type
    #return [name, house] #value can be changed

if __name__ == "__main__":
    main()
