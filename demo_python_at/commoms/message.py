from abc import ABC, abstractmethod


class Message(ABC):
    @abstractmethod
    def data(self) -> str:
        pass

    @abstractmethod
    def exist(self) -> bool:
        pass


class StrMessage(Message):
    def __init__(self, message: str):
        self._message = message

    def exist(self) -> bool:
        return len(self._message) > 0

    def data(self) -> str:
        return self._message


class HtmlMessage(Message):
    def __init__(self, base: Message):
        self._message = base

    def data(self):
        return "<p>{m}</p>".format(m=self._message.data())

    def exist(self):
        return self._message.exist()


class FakeMessage(Message):
    def __init__(self, message: str = "", exist: bool = False):
        self._message = message
        self._exist = exist

    def exist(self) -> bool:
        return self._exist

    def data(self) -> str:
        return self._message
