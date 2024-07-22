def test_product(one_product):
    assert one_product.name == "Iphone 15"
    assert one_product.description == "512GB, Gray space"
    assert one_product.price == 210000.0
    assert one_product.quantity == 8


def test_category(one_category):
    assert one_category.name == "Смартфоны"
    assert one_category.description == ("Смартфоны, как средство не только коммуникации, "
                                        "но и получения дополнительных функций для удобства жизни")
    assert len(one_category.products) == 1
    assert one_category.category_count == 1
    assert one_category.product_count == 1
