from ex0 import FlameFactory, AquaFactory

flame = FlameFactory()
aqua = AquaFactory()
abase = aqua.create_base()
aevolved = aqua.create_evolved()
fbase = flame.create_base()
fevolved = flame.create_evolved()


def create():
    print("Testing factory")
    print(fbase.describe())
    print(fbase.attack())
    print(fevolved.describe())
    print(fevolved.attack())

    print("Testing factory")
    print(abase.describe())
    print(abase.attack())
    print(aevolved.describe())
    print(aevolved.attack())


def battle():
    print("Testing battle")
    print(fbase.describe())
    print("vs.")
    print(abase.describe())
    print("fight!")
    print(fbase.attack())
    print(abase.attack())


create()
battle()
