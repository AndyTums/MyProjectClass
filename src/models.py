class Product:
    """Класс для предоставления продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса Product, задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int):
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер получает и выводит цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: int):
        """Сеттер изменяет цену продукта, если ниже требует потверждения"""
        if new_price < self.__price:
            confirmation_price = input(f"Новая цена: {new_price} ниже {self.__price}, "
                                       f"хотите изменить?(YES/NO)").lower()
            if "y" in confirmation_price:
                self.__price = new_price
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

    @property
    def views_product(self):
        """Метод возвращает описание товара типа: Имя, цена, остаток."""
        views_str = ""
        for i in self.__products:
            views_str += f"{i.name}, {i.price}. Остаток: {i.quantity}\n"

        return views_str

    @views_product.setter
    def views_product(self, product: Product):
        """Сеттер добавляет новый продукт в список продуктов категории"""
        self.__products.append(product)
        Category.product_count += 1
