def secure_archive(
    file_name: str, action: str = "read", changes: str = ""
) -> tuple[bool, str]:
    print("=== Cyber Archives Security ===")
    try:
        if action == "read":
            with open(file_name) as file:
                content = file.read()
                print("Using ’secure_archive’ to read from a regular file:")
                return (True, content)
        elif action == "write":
            with open(file_name, "w+") as file:
                file.write(changes)
                print(
                    "Using ’secure_archive’ to write previous content to a new"
                    " file:"
                )
                return (True, "Content successfully written to file")
        return (False, "invalid action")

    except FileNotFoundError as e:
        print("Using ’secure_archive’ to read from a nonexistent file:")
        return (False, str(e))
    except PermissionError as e:
        print("Using ’secure_archive’ to read from an inaccessible file:")
        return (False, str(e))


print(secure_archive("ooo.txt"))
