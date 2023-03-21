from enum import Enum, auto #(ля себя)используется для возврата членов по значению, представляет собой набор символических имен (членов), привязанных к уникальным значениям
from collections import namedtuple

# 1 задание вместе со 2 заданием, самому было сложно это сделать, так что использовались шаблоны и решения других людей - данного паттерна Builder
# можно сегодня по подробнее это пройдти
PizzaBase = namedtuple('PizzaBase', ['DoughDepth', 'DoughType'])
class PizzaDoughDepth(Enum):
    THIN = auto()
    THICK = auto()


class PizzaDoughType(Enum):
    WHEAT = auto()
    CORN = auto()
    RYE = auto()


class PizzaSauceType(Enum):
    PESTO = auto()
    WHITE_GARLIC = auto()
    BARBEQUE = auto()
    TOMATO = auto()


class PizzaTopLevelType(Enum):
    MOZZARELLA = auto()
    SALAMI = auto()
    BACON = auto()
    MUSHROOMS = auto()
    SHRIMPS = auto()

"""
Класс компонуемого продукта
"""


class Pizza:
    def __init__(self, builder):
        self.name = builder.name
        self.dough = builder.dough
        self.sauce = builder.sauce
        self.topping = builder.topping
        self.cooking_time = builder.cooking_time  # in minute

    def __str__(self):
        info: str = f"Pizza name: {self.name} \n" \
                    f"dough type: {self.dough.DoughDepth.name} & " \
                    f"{self.dough.DoughType.name}\n" \
                    f"sauce type: {self.sauce} \n" \
                    f"topping: {[it.name for it in self.topping]} \n" \
                    f"cooking time: {self.cooking_time} minutes"
        return info

    @staticmethod
    def getBuilder():
        return _Builder()


"""
Реализация строителя (шеф-поваров) для сборки пицц
"""


class _Builder:
    def set_name(self, name: str):
        self.name = name

    def set_dough(self, pizza_base: PizzaBase):
        self.dough = pizza_base

    def set_sauce(self, sauce: PizzaSauceType):
        self.sauce = sauce

    def set_topping(self, topping: list):
        self.topping = topping

    def set_cooking_time(self, time: int):
        self.cooking_time = time

    def build(self):
        return Pizza(self)


if __name__ == "__main__":
    # Готовим пиццу Маргарита
    pizza_base = PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT)
    builder = Pizza.getBuilder()
    builder.set_name("Margarita")
    builder.set_dough(pizza_base)
    builder.set_sauce(PizzaSauceType.TOMATO)
    builder.set_topping(
        [
            it for it in (PizzaTopLevelType.MOZZARELLA,
                          PizzaTopLevelType.MOZZARELLA,
                          PizzaTopLevelType.BACON,
                          )
        ]
    )
    builder.set_cooking_time(10)
    pizza = builder.build()
    print(pizza)
