from abc import ABC, abstractmethod

from demo_python_at.commons.message import Message
from demo_python_at.commons.printer import Printer


class Application(ABC):

    """Base class for all applications."""

    @abstractmethod
    def print(self):
        pass


class SimpleApplication(Application):

    """
    Class that simply prints out text.

    It aggregates the Printer and Message class instances and
    performs printing the content of Message instance.
    """

    def __init__(self, printer: Printer, message: Message):
        self._printer = printer
        self._message = message

    def print(self):
        self._printer.print(self._message)
