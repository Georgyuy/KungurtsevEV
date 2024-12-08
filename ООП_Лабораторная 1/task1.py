import doctest

class Car:
    def __init__(self, brand: str, max_speed: float, fuel_capacity: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param max_speed: Максимальная скорость автомобиля
        :param fuel_capacity: Объем топливного бака

        Примеры:
        >>> car = Car("Toyota", 200.0, 50.0)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Объем топливного бака должен быть положительным числом")

        self.brand = brand
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity

    def start_engine(self) -> None:
        """
        Запуск двигателя автомобиля.

        Примеры:
        >>> car = Car("Toyota", 200.0, 50.0)
        >>> car.start_engine()
        """
        ...

    def drive(self, distance: float) -> None:
        """
        Управление автомобилем на определенную дистанцию.

        :param distance: Расстояние в километрах
        :raise ValueError: Если расстояние отрицательное

        Примеры:
        >>> car = Car("Toyota", 200.0, 50.0)
        >>> car.drive(100)
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        ...


class Cat:
    def __init__(self, name: str, age: int, color: str):
        """
        Создание и подготовка к работе объекта "Кот"

        :param name: Имя кота
        :param age: Возраст кота
        :param color: Цвет шерсти кота

        Примеры:
        >>> cat = Cat("Барсик", 3, "рыжий")
        """
        if not isinstance(name, str):
            raise TypeError("Имя кота должно быть строкой")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст кота должен быть положительным числом")
        if not isinstance(color, str):
            raise TypeError("Цвет шерсти должен быть строкой")

        self.name = name
        self.age = age
        self.color = color

    def meow(self) -> str:
        """
        Кот издает звук "мяу".

        :return: Строка "мяу"

        Примеры:
        >>> cat = Cat("Барсик", 3, "рыжий")
        >>> cat.meow()
        'мяу'
        """
        return "мяу"

    def eat(self, food: str) -> None:
        """
        Кот ест определенную пищу.

        :param food: Тип пищи
        :raise ValueError: Если пища пустая строка

        Примеры:
        >>> cat = Cat("Барсик", 3, "рыжий")
        >>> cat.eat("рыба")
        """
        if not food:
            raise ValueError("Пища не может быть пустой строкой")
        ...


class House:
    def __init__(self, address: str, area: float, floors: int):
        """
        Создание и подготовка к работе объекта "Дом"

        :param address: Адрес дома
        :param area: Площадь дома в квадратных метрах
        :param floors: Количество этажей

        Примеры:
        >>> house = House("ул. Ленина, 10", 120.0, 2)
        """
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть строкой")
        if not isinstance(area, (int, float)) or area <= 0:
            raise ValueError("Площадь дома должна быть положительным числом")
        if not isinstance(floors, int) or floors <= 0:
            raise ValueError("Количество этажей должно быть положительным числом")

        self.address = address
        self.area = area
        self.floors = floors

    def open_door(self) -> None:
        """
        Открытие двери дома.

        Примеры:
        >>> house = House("ул. Ленина, 10", 120.0, 2)
        >>> house.open_door()
        """
        ...

    def clean(self) -> None:
        """
        Уборка дома.

        Примеры:
        >>> house = House("ул. Ленина, 10", 120.0, 2)
        >>> house.clean()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
