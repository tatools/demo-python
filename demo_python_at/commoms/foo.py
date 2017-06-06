from abc import ABC, abstractmethod

from demo_python_at.commoms.message import Message
from demo_python_at.commoms.printer import Printer


class Foo(ABC):
    @abstractmethod
    def print(self):
        pass


class SimpleFoo(Foo):
    def __init__(self, printer: Printer, message: Message):
        self._printer = printer
        self._message = message

    def print(self):
        self._printer.print(self._message)
