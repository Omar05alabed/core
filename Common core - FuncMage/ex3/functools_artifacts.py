import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError("Unknown operation")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, power=50, element="fire")
    ice = functools.partial(base_enchantment, power=50, element="ice")

    lightning = functools.partial(
        base_enchantment,
        power=50,
        element="lightning",
            )

    return {"fire": fire, "ice": ice, "lightning": lightning}


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n

    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def spell(spell_value: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(spell_value: int) -> str:
        return f"{spell_value} damage"

    @spell.register(str)
    def _(spell_value: str) -> str:
        return spell_value

    @spell.register(list)
    def _(spell_value: list) -> str:
        return f"{len(spell_value)} spells"

    return spell
