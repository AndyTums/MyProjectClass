import pytest

from src.models import Product, Category


# ТЕСТЫ НА ДЛЯ КЛАССА PRODUCT

def test_product(one_product):
    assert one_product.name == "Iphone 15"
    assert one_product.description == "512GB, Gray space"
    assert one_product.price == 210000.0
    assert one_product.quantity == 8


def test_add_product(one_category, one_product):
    assert one_category.product_count == 1
    one_category.add_product(one_product)
    assert one_category.product_count == 2


def test_new_product():
    product = Product("Nokia", "120GB, Gray space", 15000.0, 4)
    assert product.name == "Nokia"


def test_price_getter(one_product):
    assert one_product.price == 210000


def test_str_product(one_product):
    assert str(one_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_summ_product(one_product, second_product):
    assert (one_product + second_product) == 2580000.0


# ТЕСТЫ ДЛЯ КЛАССА CATEGORY

def test_category(one_category):
    assert one_category.name == "Смартфоны"
    assert one_category.description == ("Смартфоны, как средство не только коммуникации, "
                                        "но и получения дополнительных функций для удобства жизни")
    assert one_category.category_count == 1
    assert one_category.product_count == 1


def test_views_product(one_category):
    assert one_category.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_str_category(one_category):
    assert str(one_category) == "Категория Смартфоны, количество продуктов: 8 шт."


def test_smartphone(one_smartphone):
    assert one_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert one_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert one_smartphone.price == 180000.0
    assert one_smartphone.quantity == 5
    assert one_smartphone.efficiency == 95.5
    assert one_smartphone.model == "S23 Ultra"
    assert one_smartphone.memory == 256
    assert one_smartphone.color == "Серый"


def test_sum_smartphone(one_smartphone, second_smartphone):
    assert one_smartphone + second_smartphone == 2580000.0


def test_sum_error(one_smartphone, one_lawngrass):
    with pytest.raises(TypeError):
        assert one_smartphone + one_lawngrass


def test_lawngrass(one_lawngrass):
    assert one_lawngrass.name == "Газонная трава"
    assert one_lawngrass.description == "Элитная трава для газона"
    assert one_lawngrass.price == 500.0
    assert one_lawngrass.quantity == 20
    assert one_lawngrass.country == "Россия"
    assert one_lawngrass.germination_period == "7 дней"
    assert one_lawngrass.color == "Зеленый"


def test_sum_lawngrass(one_lawngrass, second_lawngrass):
    assert one_lawngrass + second_lawngrass == 16750.0


def test_sum_error_grass(one_smartphone, one_lawngrass):
    with pytest.raises(TypeError):
        assert one_lawngrass + 1


def test_middle_price(one_product, third_product, category_without_product):
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, "
                        "но и получения дополнительных функций для удобства жизни",
                        [one_product, third_product])
    assert category.middle_price() == 120500.0
    assert category_without_product.middle_price() == 0


# def test_error_middle_price(one_product, fourth_product):
#     category = Category("Смартфоны",
#                         "Смартфоны, как средство не только коммуникации, "
#                         "но и получения дополнительных функций для удобства жизни",
#                         [])
#     with pytest.raises(ZeroDivisionError):
#         category.middle_price()

