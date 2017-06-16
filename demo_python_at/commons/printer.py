from abc import ABC, abstractmethod

from demo_python_at.commons.message import Message


class Printer(ABC):

    """Base class for all printers."""

    @abstractmethod
    def print(self, message: Message):
        """Abstract method for printing."""
        pass


class StdoutPrinter(Printer):

    """Class that prints a message to console."""

    def print(self, message: Message):
        """
        Print given message in stdout.

        :param message: Message class object
        """
        print(message.data())
