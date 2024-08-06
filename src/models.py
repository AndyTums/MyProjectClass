class Product:
    """Класс для предоставления продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса Product, задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Метод возвращает описание товара типа: Имя, цена, остаток."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        """Метод складывает количество продуктов и их общую стоимость с другим продуктом"""
        return self.quantity * self.price + other.quantity * other.price

    @classmethod
    def new_product(cls, work_dict):
        """Метод возвращает класс Продукта из списка словарей"""
        name = work_dict["name"]
        description = work_dict["description"]
        price = work_dict["price"]
        quantity = work_dict["quantity"]

        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер получает и выводит цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: int):
        """Сеттер изменяет цену продукта, если ниже требует потверждения"""
        if new_price <= 0:
            print("Цена должна быть положительной или не равно 0")
        else:
            confirmation_price = input(f"Новая цена: {new_price} ниже {self.__price}, "
                                       f"хотите изменить?(YES/NO)").lower()
            if "y" in confirmation_price:
                self.__price = new_price


class Category:
    """Клас для предоставления категории"""

    category_count = 0  # Счетчик количества категорий
    product_count = 0  # Счетчик количества продуктов

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации класса Category, задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Метод выводит строковое значение наименование категории и общее количество товара на складе"""
        value = 0
        for i in self.__products:
            value += i.quantity
        return f"Категория {self.name}, количество продуктов: {value} шт."

    @property
    def views_product(self):
        """Метод возвращает описание товара типа: Имя, цена, остаток."""
        for i in self.__products:
            return f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n"

    def add_product(self, product: Product):
        """Класс метод добавляет новый продукт в список продуктов категории"""
        self.__products.append(product)
        Category.product_count += 1
