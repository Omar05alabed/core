import ft_garden_data

rose = ft_garden_data.Plant("Rose", 25, 30)
oak = ft_garden_data.Plant("Oak", 200, 365)
cactus = ft_garden_data.Plant("Cactus", 80, 45)
sunflower = ft_garden_data.Plant("Sunflower", 80, 45)
fern = ft_garden_data.Plant("Fern", 15, 120)

plants = [rose, oak, cactus, sunflower, fern]

print("=== Plant Factory Output ===")
for plant in plants:
    print("Created:", end=" ")
    plant.show()
