from plates import is_valid


def test_valid():
    assert is_valid("CS50")
    assert is_valid("HELLO")


def test_length():
    assert not is_valid("A")
    assert not is_valid("TOOLONG")


def test_starting_numbers():
    assert not is_valid("50CS")
    assert not is_valid("123")


def test_zero():
    assert not is_valid("CS05")
    assert is_valid("CS50")


def test_numbers_middle():
    assert not is_valid("CS50P")


def test_punctuation():
    assert not is_valid("PI3.14")


