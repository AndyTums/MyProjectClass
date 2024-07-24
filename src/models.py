class Product:
    """Класс для прдставления продуктов"""

    name: str  # Наименование продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: float  # Количество продукта

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса Product, задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Клас для предоставления категории"""

    name: str  # Наименование продукта
    description: str  # Описание продукта
    products: list  # Список продуктов

    category_count = 0  # Счетчик количества категорий
    product_count = 0  # Счетчик количества продуктов

    def __init__(self, name, description, products):
        """Метод для инициализации класса Category, задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
