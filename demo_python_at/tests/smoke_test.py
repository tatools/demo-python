from demo_python_at.commoms.application import SimpleApplication
from demo_python_at.commoms.message import HtmlMessage, StrMessage
from demo_python_at.commoms.printer import StdoutPrinter


def test_foo():
    SimpleApplication(StdoutPrinter(),
                      HtmlMessage(StrMessage("Hello"))).print()
