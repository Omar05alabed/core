from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingredients_lower = ingredients.lower()

    for ingredient in dark_spell_allowed_ingredients():
        if ingredient in ingredients_lower:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
