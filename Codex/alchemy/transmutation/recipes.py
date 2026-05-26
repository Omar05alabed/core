from ..elements import create_air
import alchemy.potions
from elements import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew {create_air()} and "
            f"{alchemy.potions.strength_potion()} mixed with {create_fire()}"
            )
