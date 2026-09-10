def artifact_sorter(artifacts: list[dict[str, int]]) -> list[dict[str, int]]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(
    mages: list[dict[str, int]],
    min_power: int
) -> list[dict[str, int]]:
    return list(
        filter(lambda mage: mage["power"] >= min_power, mages)
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict[str, int]]) -> dict[str, object]:
    x = max(mages, key=lambda mage: mage["power"])
    n = min(mages, key=lambda mage: mage["power"])

    power = list(map(lambda mage: mage["power"], mages))
    avg = round(sum(power) / len(power), 2)

    return {
        "max_power": x["power"],
        "min_power": n["power"],
        "avg_power": avg
    }
