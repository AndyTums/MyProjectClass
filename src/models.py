class Product:
    """Класс для прдставления продуктов"""

    name: str
    description: str
    price: float
    quantity: float

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса Product, задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Клас для предоставления категории"""

    name: str
    description: str
    products: list

    category_count = 0  # Счетчик количества категорий
    product_count = 0  # Счетчик количества продуктов

    def __init__(self, name: str, description: str, products: list):
        """Метод для инициализации класса Category, задаем значения атрибутам экземпляра"""
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
