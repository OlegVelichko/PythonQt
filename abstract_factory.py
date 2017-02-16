import random


class PetShop:
    def _init__(self, animal_factory=None):
        """pet_factory is abstract factory"""
        self.pet_factory = animal_factory

    def show_pet(self):

        pet = self.pet_factory.get_pet()
        print("This is a lovely", pet)
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())


class DogFactory():
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"


class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

if __name__ == "__main__":
    def get_factory():
        return random.choice([DogFactory, CatFactory])()

    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("=" * 20)
