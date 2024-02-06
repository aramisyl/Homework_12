class Vehicle:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print("The vehicle is starting.")

class Car(Vehicle):

    def __init__(self, brand, model, color, doors):
        super.__init__(brand, model, color)
        self.doors = doors

    def honk(self):
        print("The car is honking.")

class Bike(Vehicle):

    def __init__(self, brand, model, color, gears):
        super.__init__(brand, model, color)
        self.gears = gears

    def pedal(self):
        print("The bike is pedaling.")

class Plane(Vehicle):

    def __init__(self, brand, model, color, wingspan):
        super.__init__(brand, model, color)
        self.wingspan = wingspan

    def fly(self):
        print("The plane is flying.")