import ft_garden_data

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print(f"Is 30 days more than a year? {ft_garden_data.Plant.is_years_old(30)}")
    print(f"Is 400 days more than a year? {ft_garden_data.Plant.is_years_old(400)}")

    print("=== Flower")
    rose = ft_garden_data.Flower("Rose", 15, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    rose._state.display()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose._state.display()

    print("=== Tree")
    oak = ft_garden_data.Tree("Oak", 200, 365, 5)

    oak.show()

    print("[statistics for Oak]")
    oak.show_state()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    oak.show_state()

    
    print("=== Seed")
    sunflower = ft_garden_data.Seed("Sunflower", 80, 54, "yellow")

    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    sunflower._state.display()

    print("=== Anonymous")
    unknown = ft_garden_data.Plant.anonymous()
    unknown.show()
    print("[statistics for Unknown plant]")
    ft_garden_data.display_stats(unknown)
