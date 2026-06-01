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


rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 365)
cactus = Plant("Cactus", 80, 45)
sunflower = Plant("Sunflower", 80, 45)
fern = Plant("Fern", 15, 120)

plants = [rose, oak, cactus, sunflower, fern]

print("=== Plant Factory Output ===")
for plant in plants:
    print("Created:", end=" ")
    plant.show()
