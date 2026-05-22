class Plant():
  
    def __init__(self, name, height, age):
        self._name = name
        self._height = 0.0
        self._age = 0
        self._state = Plant.State()
        if height < 0:
            print(f"{name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
        else:
            self._age = age

    def get_height(self):
        return self._height
    
    def get_age(self):
        return self._age
    
    def set_height(self, height):
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm")
          
        else:
            print(f"{self._name}: Error, height can’t be negative")
            print("Height update rejected")
            return

    def set_age(self, age):
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days")            

        else:
            print(f"{self._name}: Error, age can’t be negative")
            print("Age update rejected")
            return
        
    @staticmethod
    def is_years_old(days):
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0)


    class State():
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.produced_shades = 0

        def display(self):
            print(f"Stats: {self.grow_calls} grow, {self.age_calls} age, {self.show_calls} show")
    
    def show(self):
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._state.show_calls += 1
        
    def grow(self):
        self._height += 0.2
        self._state.grow_calls += 1
        
    def age_up(self):
        self._age += 1
        self._state.age_calls += 1
        


class Flower(Plant):
    
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True
    
    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

class Tree(Plant):

    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self._name} now produces a shade "
            f"of {self._height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )
        self._state.produced_shades += 1


    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def show_state(self):
        self._state.display()
        print(f"{self._state.produced_shades} shade")

class Vegetable(Plant):
    
    def __init__(self, name, height, age,  harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_seson = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age_up(self):
        super().age_up()

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_seson}")
        print(f"Nutritional value: {self.nutritional_value}")

class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds = 0
    
    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")

def display_stats(plant):
    plant._state.display()

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)

    sunflower = Plant("Sunflower", 80, 45)

    cactus = Plant("Cactus", 15, 120)


    print("=== Garden Plant Registry ===")

    rose.show()
    sunflower.show()
    cactus.show()