from generative.builder_with_director import PizzaSauceType, PizzaBase, PizzaDoughDepth, PizzaDoughType, \
    PizzaTopLevelType


"""
Composable product class
"""


class Pizza:
    def __init__(self, _builder):
        self.name = _builder.name
        self.dough = _builder.dough
        self.sauce = _builder.sauce
        self.topping = _builder.topping
        self.cooking_time = _builder.cooking_time  # in minute

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
Implementation of a builder (chefs) for assembling pizzas
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
    # Cooking pizza Margarita
    pizza_base = PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT)
    builder = Pizza.getBuilder()
    builder.set_name("Margarita")
    builder.set_dough(pizza_base)
    builder.set_sauce(PizzaSauceType.TOMATO)
    builder.set_topping(
        [item for item in (PizzaTopLevelType.MOZZARELLA, PizzaTopLevelType.MOZZARELLA, PizzaTopLevelType.BACON)]
    )
    builder.set_cooking_time(10)
    pizza = builder.build()
    print(pizza)
