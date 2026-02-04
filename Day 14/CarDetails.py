# creating a Car service
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make : {self.make}")
        print(f"Model: {self.model}")
        print(f"Year : {self.year}")


# child class of Car
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        Car.__init__(self,make, model, year)
        self.battery_size = battery_size

    def display(self):
        Car.display(self)
        print(f"Battery Size: {self.battery_size} kWh")


# object creation (outside class)
car1 = Car("BMW", "W4", 2024)
car1.display()

print("\n----------\n")

electric_car = ElectricCar("Tata", "Nexon EV", 2023, 296)
electric_car.display()

print("\n----------\n")

ev = ElectricCar("BYD", "BYD Atto 3", 2025, 455)
ev.display()