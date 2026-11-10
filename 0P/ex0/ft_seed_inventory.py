def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    cap: str = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{cap} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{cap} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{cap} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
