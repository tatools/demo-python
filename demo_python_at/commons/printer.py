from abc import ABC, abstractmethod

from demo_python_at.commons.message import Message


class Printer(ABC):

    """Base class for all printers."""

    @abstractmethod
    def print(self, message: Message):
        pass


class StdoutPrinter(Printer):

    """Class that prints a message to console."""

    def print(self, message: Message):
        print(message.data())
