from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.abstract import BattleStrategy
from ex0.Creature import CreatureFactory


aqua = AquaFactory()
flame = FlameFactory()
healing = HealingCreatureFactory()
transform = TransformCreatureFactory()

normal = NormalStrategy()
aggressive = AggressiveStrategy()
defensive = DefensiveStrategy()

tournament0 = [
    (flame, normal),
    (healing, defensive),
]

tournament1 = [
    (flame, aggressive),
    (healing, defensive),
]

tournament2 = [
    (aqua, normal),
    (healing, defensive),
    (transform, aggressive),
]


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("* Battle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()
            print(creature1.describe())
            print("vs")
            print(creature2.describe())
            print("now fight!")
            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


battle(tournament0)
battle(tournament1)
battle(tournament2)
