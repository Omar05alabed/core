from .light_validator import validate_ingredients


def light_spell_allowed_ingredients():
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str):
    validation = validate_ingredients(
        ingredients, light_spell_allowed_ingredients()
    )

    return f"Spell recorded: {spell_name} ({ingredients} - {validation})"
