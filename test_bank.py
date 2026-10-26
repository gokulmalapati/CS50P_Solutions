from bank import value

def test_value_0():
    assert value("hello you  ") == 0
    assert value("hello you dumb sir") == 0
    assert value("Hello you  ") == 0

def test_value_20():
    assert value("h you  ") == 20
    assert value("hi you dumb sir") == 20

def test_value_100():
    assert value("ello you  ") == 100
    assert value(" you dumb sir") == 100
