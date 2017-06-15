from abc import ABC, abstractmethod

from demo_python_at.commons.message import Message


class Printer(ABC):
    @abstractmethod
    def print(self, message: Message):
        pass


class StdoutPrinter(Printer):
    def print(self, message: Message):
        print(message.data())
