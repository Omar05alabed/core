from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    ingredients_lower = ingredients.lower()

    for ingredient in dark_spell_allowed_ingredients():
        if ingredient == ingredients_lower:
            return "VALID"

    return "INVALID"
