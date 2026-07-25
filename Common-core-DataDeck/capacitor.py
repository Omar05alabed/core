from ex1 import HealingCreatureFactory, TransformCreatureFactory


heal = HealingCreatureFactory()
heal1 = heal.create_base()
evolved = heal.create_evolved()
trans = TransformCreatureFactory()
trans1 = trans.create_base()
evolved1 = trans.create_evolved()


def first() -> None:
    print("Testing Creature with healing capability")
    print("base")
    print(heal1.describe())
    print(heal1.attack())
    print(heal1.heal())
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

    print("Testing Creature with transform capability")
    print("base")
    print(trans1.describe())
    print(trans1.attack())
    print(trans1.transform())
    print(trans1.attack())
    print(trans1.revert())
    print("evolved")
    print(evolved1.describe())
    print(evolved1.attack())
    print(evolved1.transform())
    print(evolved1.attack())
    print(evolved1.revert())


first()
