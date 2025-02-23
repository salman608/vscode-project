class animal:
    def __init__ (self, name, species):
        self.name=name
        self.species=species
    def sound(self):
        print(f"{self.name} is makes sound")

class dog(animal): 
         def __init__(self, name, species, breed, is_guard_dog, security):
          super().__init__(name, species)
          self.breed=breed
          self.is_guard_dog=is_guard_dog
          self.security=security
         def sound(self):
           print("Bark")
class cat(animal):
    def __init__(self, name, species, color, lovely):
        super().__init__(name, species)
        self.color=color
        self.lovely=lovely
        self.name:name
        def sound(self, sound):
            print("meow")   

dog = dog("bubby","Sporting", "Bulldog", "true", "guardgog", )
cat = cat("jery", "Abyssinian", "white", "kind")

dog.sound()
cat.sound()



