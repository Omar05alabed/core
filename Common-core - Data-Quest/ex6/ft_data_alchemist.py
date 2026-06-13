import random


print("=== Game Data Alchemist ===")
players = [
    "Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john",
    "kevin", "Liam"
]
print(f"Initial list of players: {players}")
players_cap = [player.capitalize() for player in players]

print(f"New list with all names capitalized: {players_cap}")

init_cap = [p for p in players if p[0].isupper()]

print(f"New list of capitalized names only: {init_cap}")

scores = {d: random.randint(0, 1000) for d in players_cap}

print(f"Score dict: {scores}")
avg = sum(scores.values()) / len(scores)
print(f"Score average is {round(avg, 2)}")

high_scores = {name: score for name, score in scores.items() if score > avg}
print(f"High scores: {high_scores}")
