# Jermaine Bentley
# The file name is "Vehicle Attribute Record"
# The purpose of this program is to print a record of the attributes of a car for which the user prints on the program. Basically just answer the questions
# the program asks and it prints a record of your answers.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def main():
    vehicle_type = "car"  # Assume the user input is "car"
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    car = Automobile(vehicle_type, year, make, model, doors, roof)
    car.display_info()

if __name__ == "__main__":
    main()