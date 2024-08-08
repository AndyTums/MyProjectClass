from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Определение абстрактных методов """

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
