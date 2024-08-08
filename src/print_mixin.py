class PrintMixin:
    """ Класс для логирование вызова классовых методов """

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__repr__}({self.name}, {self.description}, {self.price}, {self.quantity})"
