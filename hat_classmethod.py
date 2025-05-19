# when we don't need multiple objects of a class, we can call the class itself

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuf", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")

Hat.sort("Harry")

