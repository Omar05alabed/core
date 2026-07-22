from abc import ABC, abstractmethod
from ex0 import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, tareget=None):
        ...


class TransformCapability(ABC):
    def __init__(self):
        self.is_transformed = False

    @abstractmethod
    def transform(self):
        ...

    @abstractmethod
    def revert(self):
        ...


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self):
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return "Bloomelle uses Petal Dance!"

    def heal(self):
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self):
        if self.is_transformed is True:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self):
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self):
        self.is_transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self):
        if self.is_transformed is True:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self):
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self):
        self.is_transformed = False
        return "Morphagon stabilizes its form."


class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()

    def create_evolved(self):
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def creat_evolved(self):
        return Morphagon()
