def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()
    if unit == "packets":
        print( seed,"seeds:",quantity,unit,"available")
    elif unit == "grams":
        print(seed,"seeds:",quantity,unit,"total")
    elif unit == "area":
        print(seed,"seeds:","covers",quantity,"square meters")




ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")