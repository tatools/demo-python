from demo_python_at.commons.application import SimpleApplication
from demo_python_at.commons.message import HtmlMessage, StrMessage
from demo_python_at.commons.printer import StdoutPrinter


def test_foo():
    SimpleApplication(StdoutPrinter(), HtmlMessage(StrMessage("Hello"))).print()
