from abc import ABC, abstractmethod


class Message(ABC):

    """Base class for all messages."""

    @abstractmethod
    def data(self) -> str:
        """Abstract method to return message data in string format."""
        pass

    @abstractmethod
    def exist(self) -> bool:
        """Abstract method to verify if message exist and return bool."""
        pass


class StrMessage(Message):

    """Class that stores a message in string format."""

    def __init__(self, message: str):
        """
        Initialize StrMessage object.

        :param message: data in string format
        """
        self._message = message

    def exist(self) -> bool:
        """
        Verify that message length is greater than 0.

        :return: True if message length is greater than 0
                 False in other cases
        """
        return len(self._message) > 0

    def data(self) -> str:
        """
        Get message data.

        :return: message data in string format
        """
        return self._message


class HtmlMessage(Message):

    """Class that stores a message in html format."""

    def __init__(self, base: Message):
        """
        Initialize HtmlMessage object.

        :param base: Message class object
        """
        self._message = base

    def data(self):
        """
        Reformat message data in HTML paragraph.

        :return: reformatted message data in string format
        """
        return "<p>{m}</p>".format(m=self._message.data())

    def exist(self):
        """
        Verify if message exists.

        :return: existence state of message as bool
        """
        return self._message.exist()


class FakeMessage(Message):

    """
    Class that stores a message and has field values by default.

    Field values will be set as default if not specified in constructor.
    """

    def __init__(self, message: str = "", exist: bool = False):
        """
        Initialize FakeMessage object.

        :param message: data in string format or "" by default
        :param exist: whether data exist or False by default
        """
        self._message = message
        self._exist = exist

    def exist(self) -> bool:
        """
        Get existence state of message.

        :return: existence state of message as bool
        """
        return self._exist

    def data(self) -> str:
        """
        Get message data.

        :return: message data in string format
        """
        return self._message
