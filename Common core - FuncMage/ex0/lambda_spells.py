def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifacts: artifacts["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    x = max(mages, key=lambda mage: mage["power"])
    n = min(mages, key=lambda mage: mage["power"])

    power = list(map(lambda mage: mage["power"], mages))
    avg = round(sum(power) / len(power), 2)

    return {
        "max_power": x,
        "min_power": n,
        "avg_power": avg
    }
