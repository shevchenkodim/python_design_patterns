"""
An abstract factory is an ancestral design pattern that
allows you to create families of related objects without
being tied to the specific classes of objects that you create.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    various abstract products. Products from the same family can usually
    interact with each other. A product family can have multiple variations,
    but products of one variation are incompatible with products of another.
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    A specific Factory produces a family of products of one variation. Factory
    guarantees the compatibility of the products received. note that
    Concrete Factory method signatures return an abstract product, while
    while inside the method an instance of a specific product is created.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variation.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Each individual product in a product family must have a base interface.
    All product variations must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self) -> None:
        pass


"""
Concrete products are created by the corresponding Concrete Factories.
"""


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    The basic interface of another product. All products can interact
    with each other, but correct interaction is only possible between products
    the same specific variation.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is capable of working on its own ...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ... and also interact with Products A of the same variation.

        The Abstract Factory ensures that all the products it creates are
        have the same variation and are therefore compatible.
        """
        pass


"""
Concrete products are created by the corresponding Concrete Factories.
"""


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    Product B1 can only work correctly with Product A1. However, he
    takes any instance of Abstract Product A as an argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        Product B2 can only work correctly with Product A2. However,
        it accepts any instance of Abstract Product A as argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: Abstract Factory and Abstract Product. This allows you to transfer
    any factory or product subclass to client code without breaking it.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    Client code can work with any specific factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteFactory2())
