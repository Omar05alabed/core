import ft_garden_data

if __name__ == "__main__":

    print("=== Garden Plant Types ===")

    rose = ft_garden_data.Flower("Rose", 15, 10, "red")

    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()


    oak = ft_garden_data.Tree("Oak", 200, 365, 5)
    
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    tomato = ft_garden_data.Vegetable("Tomato", 5, 10 ,"April", 5)

    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age_up()
    tomato.show()