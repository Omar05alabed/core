from abc import ABC, abstractmethod
from ex0.Creature import Creature
from ex1.Capabilities import HealCapability, TransformCapability
from typing import cast


class BattleStrategy(ABC):
    name: str

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    name = "Normal"

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError("NormalStrategy cannot be used with this"
                             " creature")
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    name = "Aggressive"

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError("AggressiveStrategy requires a creature with "
                             "transform capability")
        transformed = cast(TransformCapability, creature)
        print(transformed.transform())
        print(creature.attack())
        print(transformed.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    name = "Defensive"

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError("DefensiveStrategy requires a creature with "
                             "healing capability")

        y = cast(HealCapability, creature)
        print(creature.attack())
        print(y.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
