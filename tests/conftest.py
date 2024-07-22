import pytest
from src.main import Category, Product


@pytest.fixture
def one_product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def one_category():
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [Product("Iphone 15", "512GB, Gray space", 210000.0, 8)])
