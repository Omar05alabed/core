import ft_custom_errors



def water_plant(plant_name: str) -> None:
        if plant_name == plant_name.capitalize():
            print(f"Watering {plant_name}: [OK]")
        else:
            raise ft_custom_errors.PlantError(f"Invalid plant name to water: ’{plant_name}’")

   
def test_watering_system():
    print("=== Garden Watering System ===")
    print("Testing valid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")

    except ft_custom_errors.PlantError as error:
        print(f"Caught PlantError: {error}")

    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("lettuce")

    except ft_custom_errors.PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")
if __name__ == "__main__":
    test_watering_system()