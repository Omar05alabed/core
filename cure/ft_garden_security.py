import ft_garden_data

print("=== Garden Security System ===")

rose = ft_garden_data.Plant("Rose", 15, 10)
print("Plant created: ", end="")
rose.show()

rose.set_height(25)
rose.set_age(30)

rose.set_height(-5)
rose.set_age(-10)


print(f"Current state: ", end="")
rose.show()