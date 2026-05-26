import alchemy.elements
import elements

def healing_potion():
    return (f"Healing potion brewed with {alchemy.elements.create_earth()} and {alchemy.elements.create_air()}")

def strength_potion():
    return (f"Strength potion brewed with {elements.create_fire()} and {elements.create_water()}")