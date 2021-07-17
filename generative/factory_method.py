from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares a factory method that should return an object
    class Product. Creator subclasses usually provide an implementation of this
    method.
    """

    @abstractmethod
    def factory_method(self):
        """
        The creator can also provide an implementation
        the default factory method.
        """
        # Some default logic
        pass

    def some_operation(self) -> str:
        """
        Primary responsibility The creator is not about creating products. It usually contains
        some basic business logic that is based on Product objects, returned by the factory method.
        Subclasses can indirectly modify this business logic by overriding the factory method and returning
        another type of product.
        """

        # We call the factory method to get the product object.
        product = self.factory_method()

        # Next, we are working with this product.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


"""
Concrete Creators override the factory method in order to change the type
the resulting product.
"""


class ConcreteCreator1(Creator):
    """
    The method signature still uses the type
    abstract product, although in fact a concrete one is returned from the method
    product. Thus, the Creator can remain independent of specific product classes.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    The Product interface declares the operations that must be performed by all specific products.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Specific Products provide different implementations of the Product interface.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a specific creator, albeit through
    its basic interface. While the client continues to work with the creator through
    base interface, you can pass any creator subclass to it.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
