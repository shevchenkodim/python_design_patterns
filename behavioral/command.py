"""
A command is a behavioral pattern that allows
you to wrap queries or simple operations in separate objects.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Commands interface declares a method for executing commands.
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Some commands are capable of performing simple operations on their own.
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing ({self._payload})")


class ComplexCommand(Command):
    """
    But there are also teams that delegate more complex operations to others.
    objects called "recipients".
    """

    def __init__(self, _receiver: Receiver, a: str, b: str) -> None:
        """
        Complex commands can accept one or more recipient objects
        along with any context data via the constructor.
        """

        self._receiver = _receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands can delegate execution to any receiver method.
        """

        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    The Recipient classes contain some important business logic. They know how to do
    all kinds of operations related to the execution of a request. In fact, any class
    can act as the Recipient.
    """

    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    """
    The sender is associated with one or more commands.
    He sends a request team.
    """

    _on_start = None
    _on_finish = None

    """
    Initialization of commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        The sender is independent of the specific command and recipient classes.
        The sender passes the request to the receiver indirectly by executing the command.
        """

        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    The client code can parameterize the sender with any commands.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Print this message!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))
    invoker.do_something_important()
