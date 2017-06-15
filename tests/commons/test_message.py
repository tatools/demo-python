from demo_python_at.commons.message import FakeMessage, HtmlMessage


def test_html_message():
    assert HtmlMessage(FakeMessage(message="a")).data() == "<p>a</p>"
