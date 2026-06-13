import random


def gen_player_achievements() -> set[str]:
    achievements = [
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Boss Slayer',
        'Strategist',
        'Unstoppable',
        'Speed Runner',
        'Survivor',
        'Treasure Hunter',
        'First Steps',
        'Sharp Mind'
    ]

    size = random.randint(1, len(achievements))
    result = set()

    for o in range(size):
        result.add(random.choice(achievements))

    return result


def main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("=== Achievement Tracker System ===")
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"All distinct achievements: {alice.union(bob, charlie, dylan)}")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")
    print(f"Alice is missing: {bob.union(charlie, dylan).difference(alice)}")
    print(f"Bob is missing: {alice.union(charlie, dylan).difference(bob)}")
    print(f"Charlie is missing: {alice.union(bob, dylan).difference(charlie)}")
    print(f"Dylan is missing:  {alice.union(bob, charlie).difference(dylan)}")


main()
