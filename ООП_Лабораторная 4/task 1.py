class Pets:
    """
    Base class for all pets.
    """

    def __init__(self, name: str, age: int):
        """
        Constructor for the Pets class.

        :param name: Name of the pet.
        :param age: Age of the pet in years.
        """
        self.__name = name
        self.__age = age

    def __str__(self) -> str:
        """
        Returns a string representation of the pet.

        :return: String with information about the pet.
        """
        return f"Pet: {self.__name}, Age: {self.__age} years"

    def __repr__(self) -> str:
        """
        Returns a formal string representation of the pet.

        :return: Formal string with information about the pet.
        """
        return f"Pets(name='{self.__name}', age={self.__age})"

    def make_sound(self) -> str:
        """
        Method that should be overridden in derived classes.

        :return: Sound that the pet makes.
        """
        raise NotImplementedError("This method should be overridden in the derived class.")


class Cat(Pets):
    """
    Class for cats, inheriting from the Pets class.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Constructor for the Cat class.

        :param name: Name of the cat.
        :param age: Age of the cat in years.
        :param breed: Breed of the cat.
        """
        super().__init__(name, age)
        self.__breed = breed

    def __str__(self) -> str:
        """
        Returns a string representation of the cat.

        :return: String with information about the cat.
        """
        return f"Cat: {self._Pets__name}, Age: {self._Pets__age} years, Breed: {self.__breed}"

    def make_sound(self) -> str:
        """
        Overridden method that returns the sound made by the cat.

        :return: Sound that the cat makes.
        """
        return "Meow"


class Dog(Pets):
    """
    Class for dogs, inheriting from the Pets class.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Constructor for the Dog class.

        :param name: Name of the dog.
        :param age: Age of the dog in years.
        :param breed: Breed of the dog.
        """
        super().__init__(name, age)
        self.__breed = breed

    def __str__(self) -> str:
        """
        Returns a string representation of the dog.

        :return: String with information about the dog.
        """
        return f"Dog: {self._Pets__name}, Age: {self._Pets__age} years, Breed: {self.__breed}"

    def make_sound(self) -> str:
        """
        Overridden method that returns the sound made by the dog.

        :return: Sound that the dog makes.
        """
        return "Woof"


if __name__ == "__main__":
    cat = Cat("Bashmak", 2, "British")
    dog = Dog("Demon", 4, "Сhihuahua")

    print(cat)  # Вывод информации о коте
    print(cat.make_sound())  # Вывод звука, который издает кот

    print(dog)  # Вывод информации о собаке
    print(dog.make_sound())  # Вывод звука, который издает собака