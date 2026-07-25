from ex0 import FlameFactory, AquaFactory
from ex0.Creature import CreatureFactory


def create(factory: CreatureFactory) -> None:
    print("Testing factory")
    print(factory.create_base().describe())
    print(factory.create_base().attack())

    print(factory.create_evolved().describe())
    print(factory.create_evolved().attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    print(factory1.create_base().describe())
    print("vs.")
    print(factory2.create_base().describe())
    print("fight!")
    print(factory1.create_base().attack())
    print(factory2.create_base().attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    create(flame)
    create(aqua)
    battle(flame, aqua)
