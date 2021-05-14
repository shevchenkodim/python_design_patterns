"""
A singleton is a generative design pattern that ensures that a
class has only one instance and provides a global access point to it.
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def __init__(self, some_var):
        self.some_var = some_var

    def some_business_logic(self):
        print(self.some_var)
        return True


if __name__ == "__main__":
    s1 = Singleton('Test 1')
    s2 = Singleton('Test 2')

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

    s1.some_business_logic()
    s2.some_business_logic()
