import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        self.__name = name

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def string_to_number(score):
        return int(float(score))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        Item.all.clear()
        with open("../src/items.csv", newline='', encoding="cp1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row["name"]
                price = row["price"]
                quantity = row["quantity"]
                product = cls(name, price, quantity)
        return product

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]


class MixinLog:
    Language = "EN"
    def __init__(self):
        self.__language = MixinLog.Language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language == "EN"
        return self


class KeyBoard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
