
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand  
        self.wheels = wheels  
    
    def show_wheels(self):
       
        print(f"This vehicle has {self.wheels} wheels.")

class Car(Vehicle):
    def __init__(self, brand, color, model):
      super().__init__(brand, 4)
      self.color=color
      self.model=model
      
    def show_wheels(self):
       
        print(f"This vehicle has {self.wheels} wheels.")
class Bike(Vehicle):
    def __init__(self, brand, speed, color):
        super().__init__(brand, 4)
        self.speed=speed
        self.color=color
    def show_wheels(self):
       
        print(f"This vehicle has {self.wheels} wheels.")

car = Car("Toyota", "red","2024")
bike = Bike("Honda", "50k/h","black")

car.show_wheels()  
bike.show_wheels() 



