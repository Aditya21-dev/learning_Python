# Vehicle Management System (Single File OOPS Program)

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed      # Encapsulation (Private Variable)

    def start(self):
        print(f"{self.brand} vehicle is starting...")

    def stop(self):
        print(f"{self.brand} vehicle is stopping...")

    def display_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.__speed)

    def get_speed(self):
        return self.__speed


# Child Class 1
class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def start(self):   # Method Overriding
        print(f"{self.brand} car is starting with {self.fuel_type} engine.")


# Child Class 2
class Bike(Vehicle):
    def __init__(self, brand, speed, helmet_required):
        super().__init__(brand, speed)
        self.helmet_required = helmet_required

    def start(self):   # Method Overriding
        if self.helmet_required:
            print(f"{self.brand} bike is starting. Wear helmet!")
        else:
            print(f"{self.brand} bike is starting.")


# -------- Main Program --------

v1 = Car("Toyota", 180, "Petrol")
v2 = Bike("Yamaha", 120, True)

print("\n--- Car Details ---")
v1.display_info()
v1.start()
v1.stop()

print("\n--- Bike Details ---")
v2.display_info()
v2.start()
v2.stop()