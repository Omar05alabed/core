class Plant():

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 0.8

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


rose = Plant("rose", 25, 30)

print("=== Garden Plant Growth ===")
rose.show()

initial_height = rose.height

for day in range(1, 8):
    print(f"=== Day {day} ===")
    rose.grow()
    rose.age_up()
    rose.show()

growth = rose.height - initial_height
print(f"Growth this week: {round(growth, 2)}cm")
