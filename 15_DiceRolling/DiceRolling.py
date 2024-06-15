import random

one = """ 
            ("===========")
            ("|         |")
            ("|    O    |")
            ("|         |")
            ("===========")\n  

        """

two = """ 
            ("===========")
            ("|         |")
            ("| O     O |")
            ("|         |")
            ("===========")\n  

        """

three = """ 
            ("===========")
            ("|    O    |")
            ("|    O    |")
            ("|    O    |")
            ("===========")\n  

        """

four = """ 
            ("===========")
            ("|  O    O |")
            ("|         |")
            ("|  O    O |")
            ("===========")\n  

        """

five = """ 
            ("===========")
            ("| O     O |")
            ("|    0    |")
            ("| O     O |")
            ("===========")\n  

        """

six = """
            ("===========") 
            ("| O     O |")
            ("| O     O |")
            ("| O     O |")
            ("===========") \n      
        """

outcomes_list = [one, two, three, four, five, six]

print("Zar atma oyunu")

choice = "y"
while choice == "y":
    random_outcome = random.choice(outcomes_list)
    print(random_outcome)

    x = input("Bidaha zar atmak için (y) basın ")
