def  garden_operations(operation_number : int):
    if operation_number == 0:
      int("abc")

    elif operation_number == 1:
        result = 10 / 0
        

    elif operation_number == 2:
        open("sa")
    
    elif operation_number == 3:
        result = "abc" + 3
    else:
        print("Operation completed successfully")


def test_error_types():
    print("=== Garden Error Types Demo ===")

    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")


        try:
            garden_operations(operation_number)

        except ValueError as e:
            print(f"Caught ValueError: {e}")

        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")

        except TypeError as e:
            print(f"Caught TypeError: {e}")

        print("All error types tested successfully!")



if __name__ == "__main__":
    test_error_types()
