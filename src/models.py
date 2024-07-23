class Product:
    """Класс для прдставления продуктов"""

    name: str
    description: str
    price: float
    quantity: float

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса Product, задаем значения атрибутам экземпляра"""
        self.name = name  # Наименование продукта
        self.description = description  # Описание продукта
        self.price = price  # Цена продукта
        self.quantity = quantity  # Количество продукта


class Category:
    """Клас для предоставления категории"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации класса Category, задаем значения атрибутам экземпляра"""
        self.name = name  # Наименование продукта
        self.description = description  # Описание продукта
        self.products = products  # Список продуктов
        Category.category_count += 1
        Category.product_count += len(products)
