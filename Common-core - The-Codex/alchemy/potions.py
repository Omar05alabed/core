import alchemy.elements
import elements


def healing_potion() -> str:
    return (f"Healing potion brewed with {alchemy.elements.create_earth()} and"
            f" {alchemy.elements.create_air()}")


def strength_potion() -> str:
    return (f"Strength potion brewed with {elements.create_fire()} and"
            f" {elements.create_water()}")
