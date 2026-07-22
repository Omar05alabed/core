from ex1 import HealingCreatureFactory, TransformCreatureFactory


heal = HealingCreatureFactory()
heal1 = heal.create_base()


def first():
    print(heal.create_base())
    print(heal.create_evolved())
    print(heal1.attack)


first()
