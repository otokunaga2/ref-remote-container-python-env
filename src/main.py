import sys


def hello(name: str, age: int) -> str:
    result1: str = "My name is " + name + ".\n"
    result2: str = "I am " + str(age) + " years old."
    return result1 + result2


print(sys.version_info)
