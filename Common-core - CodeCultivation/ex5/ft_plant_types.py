class Plant():

    def __init__(self, name: str, height: float, age: int) -> None:
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

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        return

    def set_age(self, age: int) -> None:
        return

    class State():
        def __init__(self) -> None:
            self.produced_shades = 0
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(
                f"Stats: {self.grow_calls} grow, {self.age_calls} age,"
                f"{self.show_calls} show"
                )

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += 0.2

    def age_up(self) -> None:
        self._age += 1


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):

    def __init__(
        self, name: str, height: float,
        age: int, trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade "
            f"of {self._height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def show_state(self) -> None:
        self._state.display()
        print(f"{self._state.produced_shades} shade")


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: float
    ):
        super().__init__(name, height, age)
        self.harvest_seson = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age_up(self) -> None:
        super().age_up()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_seson}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":

    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 15, 10, "red")

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    oak = Tree("Oak", 200, 365, 5)

    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    tomato = Vegetable("Tomato", 5, 10, "April", 5)

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age_up()
    tomato.show()
