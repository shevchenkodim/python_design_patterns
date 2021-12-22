"""
A bridge is a structural design pattern that separates one or more classes
into two separate hierarchies — abstraction and implementation — so you can change them independently.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    """
    Abstraction sets up an interface for the "governing" part of two hierarchies
    classes. It contains a reference to an object from the Implementation hierarchy and delegates
    all real work for him.
    """

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    """
    It is possible to extend the Abstraction without changing the Implementation classes.
    """

    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    """
    An implementation sets up an interface for all implementation classes. He shouldn't
    conform to the interface of the Abstraction. In practice, both interfaces can be
    completely different. Typically, the Implementation interface only provides
    primitive operations, while Abstraction defines operations more
    high level based on these primitives.
    """

    @abstractmethod
    def operation_implementation(self) -> str:
        pass


"""
Each Concrete Implementation corresponds to a specific platform and implements
interface Implementations using the API of this platform.
"""


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    """
    Except for the initialization phase, when the Abstraction object is associated with
    specific Implementation object, the client code should only depend on
    class of Abstraction. Thus, the client code can support any
    a combination of abstraction and implementation.
    """

    # ...

    print(abstraction.operation(), end="")

    # ...


if __name__ == "__main__":
    """
    The client code should work with any preconfigured
    a combination of abstraction and implementation.
    """

    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)
