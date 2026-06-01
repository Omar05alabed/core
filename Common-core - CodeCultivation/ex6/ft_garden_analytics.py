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

    @staticmethod
    def is_years_old(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    class State():
        def __init__(self) -> None:
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.produced_shades = 0

        def display(self) -> None:
            print(
                f"Stats: {self.grow_calls} grow, {self.age_calls} age,"
                f"{self.show_calls} show"
                )

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")
        self._state.show_calls += 1

    def grow(self) -> None:
        self._height += 0.2
        self._state.grow_calls += 1

    def age_up(self) -> None:
        self._age += 1
        self._state.age_calls += 1


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False
        self.show_calls = 0

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
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
                ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade "
            f"of {self._height}cm long and "
            f"{self.trunk_diameter}cm wide."
        )
        self._state.produced_shades += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

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
            ) -> None:
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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_stats(plant: "Plant") -> None:
    plant._state.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? {Plant.is_years_old(30)}")
    print(f"Is 400 days more than a year? {Plant.is_years_old(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    rose._state.display()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose._state.display()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)

    oak.show()

    print("[statistics for Oak]")
    oak.show_state()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.show_state()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 54, "yellow")

    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower._state.display()

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    display_stats(unknown)
