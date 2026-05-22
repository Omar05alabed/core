import ft_garden_data

rose = ft_garden_data.Plant("rose", 2, 30)

print("=== Garden Plant Growth ===")
rose.show()

initial_height = rose._height

for day in range(1, 8):
    print(f"=== Day {day} ===")
    rose.grow()
    rose.age_up()
    rose.show()

growth = rose._height - initial_height
print(f"Growth this week: {round(growth, 2)}cm")