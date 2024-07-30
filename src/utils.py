import json
import os

from src.models import Category, Product


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
