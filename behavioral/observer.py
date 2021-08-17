"""
Observer is a behavioral design pattern that creates a subscription
mechanism that allows one object to watch and respond to events occurring in other objects.
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The publisher interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attaches an observer to a publisher.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detaches the observer from the publisher.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifies all observers of the event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The publisher owns some important state and notifies observers about it
    changes.
    """

    _state: int = None
    """
    For convenience, this variable stores the Publisher's state that everyone needs
    subscribers.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the subscriber list can be stored in
    in more detail (classified by type of event, etc.)
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Subscription management methods.
    """

    def notify(self) -> None:
        """
        Launching an update in every subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Typically, the subscription logic is only part of what the Publisher does.
        Publishers often contain some important business logic that
        fires a notification method whenever something is about to happen
        important (or after that).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares a notification method that publishers
    are used to notify their subscribers.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        ...


"""
Specific Observers respond to updates released by the Publisher to which
they are attached.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
