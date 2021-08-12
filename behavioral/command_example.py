from abc import ABC, abstractmethod
from typing import List


class ICommand(ABC):
    """
    Interface class for performed operations
    """
    @abstractmethod
    def execute(self) -> None:
        ...


class ChiefAssistant:
    def prepare_pizza_dough(self):
        print("The assistant prepares the pizza dough")

    def prepare_topping(self):
        print("The assistant cuts the pizza toppings")

    def prepare_sauce(self):
        print("The assistant prepares the sauce")


class Stove:
    def prepare_stove(self):
        print("The oven is heating up")

    def cooking_pizza(self):
        print("Pizza is cooked in the oven")


class ChiefCooker:
    def make_pizza_base(self):
        print("Chef rolls out a pizza base")

    def applied_sauce(self):
        print("The chef applies the sauce to the base of the pizza")

    def add_topping_to_pizza(self):
        print("Chef adds toppings to pizza")

    def bon_appetit(self):
        print("The chef wishes the client a bon appetit!")


class PrepareStoveCommand(ICommand):
    """
    Command class for heating the furnace
    """
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_stove()


class PrepareDoughCommand(ICommand):
    """
    Team class for preparing pizza dough
    """
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_pizza_dough()


class PrepareToppingCommand(ICommand):
    """
    Team class for slicing pizza toppings
    """
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_topping()


class PrepareSauceCommand(ICommand):
    """
    Sauce team class
    """
    def __init__(self, executor: ChiefAssistant):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.prepare_sauce()


class CookingPizzaCommand(ICommand):
    """
    Team class for cooking pizza in the oven
    """
    def __init__(self, executor: Stove):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.cooking_pizza()


class MakePizzaBaseCommand(ICommand):
    """
    Team class for making pizza base
    """
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.make_pizza_base()


class AppliedSauceCommand(ICommand):
    """
    Pizza Sauce Team Class
    """
    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.applied_sauce()


class AddToppingCommand(ICommand):
    """
    Command class for adding toppings to pizza
    """

    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.add_topping_to_pizza()


class BonAppetitCommand(ICommand):
    """
    Team class for the client's wishes Bon Appetit
    """

    def __init__(self, executor: ChiefCooker):
        self.__executor = executor

    def execute(self) -> None:
        self.__executor.bon_appetit()


class Pizzeria:
    """
    Aggregation class of all cooking commands pizza
    """
    def __init__(self):
        self.history: List[ICommand] = []

    def addCommand(self, command: ICommand) -> None:
        self.history.append(command)

    def cook(self) -> None:
        if not self.history:
            print("Execution order not specified"
                  " pizza making teams")
        else:
            for executor in self.history:
                executor.execute()
        self.history.clear()


if __name__ == "__main__":
    chief = ChiefCooker()
    assistant = ChiefAssistant()
    stove = Stove()
    pizzeria = Pizzeria()
    # we form a sequence of commands for cooking pizza
    pizzeria.addCommand(PrepareDoughCommand(assistant))
    pizzeria.addCommand(MakePizzaBaseCommand(chief))
    pizzeria.addCommand(PrepareSauceCommand(assistant))
    pizzeria.addCommand(AppliedSauceCommand(chief))
    pizzeria.addCommand(PrepareStoveCommand(stove))
    pizzeria.addCommand(PrepareToppingCommand(assistant))
    pizzeria.addCommand(AddToppingCommand(chief))
    pizzeria.addCommand(CookingPizzaCommand(stove))
    pizzeria.addCommand(BonAppetitCommand(chief))
    # we start the process of making pizza
    pizzeria.cook()
