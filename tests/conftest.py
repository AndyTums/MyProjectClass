import pytest
from src.models import Category, Product


@pytest.fixture
def one_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def second_product():
    return Product("Samsung", "256GB, White", 40000.0, 2)


@pytest.fixture
def one_category(one_product):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [one_product])
