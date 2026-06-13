import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    player = ["bob", "alice", "dylan", "charlie"]
    action = [
        "run", "eat", "sleep", "grab", "move", "climb", "swim", "release"
    ]

    while True:
        yield (random.choice(player), random.choice(action))


def consume_event(
    event_list: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        choice = random.choice(event_list)
        event_list.remove(choice)
        yield choice


gen = gen_event()
for i in range(1000):
    player, action = next(gen)
    print(f"Event {i}: Player {player} did action {action}")

gen2 = gen_event()
event_list = []
print("Built list of 10 events: ", end="")
for p in range(10):
    player, action = next(gen2)
    print(f"({player, action}) ", end=" ")

    event_list.append((player, action))
for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")
