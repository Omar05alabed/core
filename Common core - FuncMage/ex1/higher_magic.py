def spell(target: str, power: int) -> str:
    return f"spell shoot {target} with {power}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"



def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    ...