"""
An iterator is a behavioral pattern that allows you to consistently
traverse a complex collection without revealing the details of its implementation.
"""

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


"""
To create an iterator in Python, there are two abstract classes from the built-in
of the collections module - Iterable, Iterator. You need to implement the __iter __ () method in
the iterable object (list), and the __next __ () method in the iterator.
"""


class AlphabeticalOrderIterator(Iterator):
    """
    Concrete Iterators implement various traversal algorithms. These classes
    permanently store the current bypass position.
    """

    _position: int = None
    _reverse: bool = False

    def __init__(self, _collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = _collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable):
    """
    Concrete Collections provide one or more methods to get
    new iterator instances compatible with the collection class.
    """

    def __init__(self, _collection: List[Any] = []) -> None:
        self._collection = _collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        """
        The __iter __ () method returns an iterator object, by default we return
        an ascending iterator.
        """
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("1. ----------------")
    print("\n".join(collection))
    print("")

    print("2. ----------------")
    print("\n".join(collection.get_reverse_iterator()), end="")
