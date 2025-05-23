
class Car:
    def __init__(self, brand, model, year, doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.doors = doors
    
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class MotorCycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start_bike(self):
        print("Motorcycle is starting")

    def stop_bike(self):
        print("Motorcycle is stopping")


vehicles = [
    Car("Ford", "Focus", 2008, 5),
    MotorCycle("Honda", "Scoopy", 2018)
]

# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, MotorCycle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not a valid vehicle")

