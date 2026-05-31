import sys

print("=== Inventory System Analysis ===")
inventory: dict[str, int] = {}

for token in sys.argv[1:]:
    if token.count(":") != 1:
        print(f"Error - invalid parameter '{token}'")
        continue

    item, qty = token.split(":")

    if item in inventory:
        print(f"Redundant item '{item}' - discarding")
        continue

    try:
        qty_int = int(qty)
    except ValueError:
        print(
            f"Quantity error for '{item}': "
            f"invalid literal for int() with base 10: '{qty}'"
        )
        continue

    inventory[item] = qty_int

total = sum(inventory.values())
print(f"Got inventory: {inventory}")
print(f"Item list: {list(inventory.keys())}")
print(
    f"Total quantity of the {len(inventory)} items: "
    f"{sum(inventory.values())}"
)
for item, value in inventory.items():
    print(f"Item {item} represents {round(value/total*100, 1)}%")
most = max(inventory.values())
for item, value in inventory.items():
    if value == most:
        print(f"Item most abundant: {item} with quantity {value}")
        break
least = min(inventory.values())
for item, value in inventory.items():
    if value == least:
        print(f"Item least abundant: {item} with quantity {value}")
        break

inventory.update({"magic_item": 2})
print(f"Updated inventory: {inventory}")
