from demo_python_at.commoms.foo import SimpleFoo
from demo_python_at.commoms.message import HtmlMessage, StrMessage
from demo_python_at.commoms.printer import StdoutPrinter


def test_foo():
    SimpleFoo(StdoutPrinter(), HtmlMessage(StrMessage("Hello"))).print()
