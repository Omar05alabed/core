def validate_ingredients(ingredients: str, allowed_ingre: list[str]) -> str:

    ingredients_lower = ingredients.lower()

    for ingredient in allowed_ingre:
        if ingredient in ingredients_lower:
            return "VALID"

    return "INVALID"
