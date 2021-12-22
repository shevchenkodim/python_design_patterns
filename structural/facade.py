"""
A facade is a structural design pattern that provides a simple interface
to a complex class system, library, or framework.
"""

from __future__ import annotations


class Facade:
    """
    The Facade class provides a simple interface to complex logic of one or
    multiple subsystems. The facade delegates client requests to the appropriate
    objects inside the subsystem. The façade is also responsible for managing their life
    cycle. All this protects the client from the unwanted complexity of the subsystem.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Depending on the needs of your application, you can provide
        Facade existing subsystem objects or force Facade to create them
        on one's own.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        """
        Facade methods are handy for quick access to complex functionality
        subsystems. However, clients receive only a fraction of the capabilities of the subsystem.
        """

        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    """
    The subsystem can accept requests either from the facade or from the client directly.
    In any case, for the Subsystem, Facade is another client, and it is not
    part of the Subsystem.
    """

    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    """
    Some facades can work with different subsystems at the same time.
    """

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    """
    The client code works with complex subsystems through a simple interface,
    provided by the Facade. When a facade manages the lifecycle of a subsystem,
    the client may not even be aware of the subsystem's existence. This approach
    allows you to keep the complexity under control.
    """

    print(facade.operation(), end="")


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
