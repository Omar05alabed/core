def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature(temp: str) -> None:

    print(f"Input data is  ’{temp}’")
    try:
        input_temperature(temp)
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    print("All tests completed - program didn’t crash!")
