def recursive_count(days: int):
    if (days == 0):
        return
    else:
        recursive_count(days - 1)
        print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))
    recursive_count(days)
    print("Harvest time!")
