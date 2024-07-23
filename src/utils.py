import json
import os

from src.models import Product, Category


def read_json(filename: str) -> dict:
    """Функция считывает информацию с JSON файла"""
    full_path = os.path.abspath(filename)
    with open(full_path, "r", encoding="utf-8") as file:
        info = json.load(file)
    return info


def load_info_from_json(info):
    """Функция создает список из класса Category в которых лежат продукты класса Product"""
    list_info = []
    for value in info:
        product = []
        for i in value["products"]:
            product.append(Product(**i))
        value["products"] = product
        list_info.append(Category(**value))

    return list_info


# reding_file = read_json("../data/products.json")
# raw = load_info_from_json(reding_file)
# print(raw[0].name)
# print(raw[0].products)
