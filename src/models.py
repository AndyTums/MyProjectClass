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
        if isinstance(other, type(self)):
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError("Товары разных категорий не могут быть сложены!")

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


class Smartphone(Product):
    """ Дочерний класс для работы со смартфонами """

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """ Дочерний класс для работы с газонной травой """

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
    def products(self):
        """Метод возвращает описание товара типа: Имя, цена, остаток."""
        for i in self.__products:
            return f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт.\n"

    def add_product(self, product: Product):
        """Класс метод добавляет новый продукт в список продуктов категории"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        raise TypeError


if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
