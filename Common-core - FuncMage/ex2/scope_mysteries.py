from typing import Callable


def mage_counter() -> Callable[[], int]:
    x: int = 0

    def counter() -> int:
        nonlocal x
        x += 1
        return x

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power: int = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def enchant(item_name: str) -> str:
        return enchantment_type + " " + item_name

    return enchant


def memory_vault() -> dict[str, Callable[..., object]]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


counter = mage_counter()
print(counter())
