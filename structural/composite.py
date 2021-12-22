"""
A compositor is a structural design pattern that allows you to group multiple objects
into a tree structure and then work with it as if it were a single object.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
    The base class Component declares common operations for both simple and
    complex objects of structure.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        If necessary, the underlying Component can declare an interface for
        setting and getting the parent of a component in a tree structure. He
        may also provide some default implementation for these
        methods.
        """
        self._parent = parent

    """
    In some cases, it is advisable to define operations for managing descendants
    right in the base class Component. This way you will not need to
    provide concrete component classes to client code, even during
    assemblies of the object tree. The disadvantage of this approach is that these methods
    will be empty for sheet level components.
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """
        You can provide a method that allows the client code to understand
        whether the component can have nested objects.
        """
        return False

    @abstractmethod
    def operation(self) -> str:
        """
        The underlying Component can itself implement some default behavior
        or delegate this to specific classes by declaring a method containing the behavior
        abstract.
        """
        pass


class Leaf(Component):
    """
    The Leaf class represents the final objects of the structure. Leaf cannot
    have nested components.

    Typically, Leaf objects do the actual work, while Leaf objects do the actual work.
    Containers only delegate work to their subcomponents.
    """

    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
    The Container class contains complex components that can be nested
    Components. Typically, Container objects delegate the actual work to their
    children, and then "summarize" the result.
    """

    def __init__(self) -> None:
        self._children: List[Component] = []

    """
    The container object can both add components to its nested list
    components and remove them, both simple and complex.
    """

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        The container executes its main logic in a special way. It passes
        recursively through all of its children, collecting and summarizing their results.
        Since the descendants of the container pass these calls to their descendants and so
        further, as a result, the entire tree of objects is traversed.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


def client_code(component: Component) -> None:
    """
    The client code works with all components through the base interface.
    """
    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:
    """
    Due to the fact that the operations for managing descendants are declared in the base class
    Component, client code can work with both simple and complex
    components, regardless of their specific classes.
    """

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


if __name__ == "__main__":
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print("\n")

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
