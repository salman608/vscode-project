import math

class Shape:
    def __init__(self, color):
        self.color = color  
    def color(self):
        print(f"{self.color}")

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)  
        self.radius = radius
      
    
    def area(self):
         return math.pi * self.radius**2 # Area of a circle
    
  
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)  
        self.width = width  
        self.height = height  

    def area(self):
        return self.width * self.height  # Area of a rectangle       
    

circle = Circle("red", 5)
rectangle = Rectangle("blue", 4, 6)

print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")