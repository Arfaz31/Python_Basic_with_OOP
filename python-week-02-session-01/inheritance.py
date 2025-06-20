class Vehicle:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, color):
        super().__init__(brand, model)
        self.color = color

class ElectricCar(Car):
    def __init__(self, brand, model, color, battery_capacity):
        super().__init__(brand, model, color)
        self.battery_capacity = battery_capacity


tesla = ElectricCar("Tesla", "Model S", "Red", 100)
print(tesla.brand)
print(tesla.model)
print(tesla.color)
print(tesla.battery_capacity)