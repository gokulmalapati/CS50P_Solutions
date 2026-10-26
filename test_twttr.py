from twttr import shorten



def test_shorten_lowercase():
    assert shorten("aeiou") == ""
    assert shorten("cat") == "ct"
    assert shorten("rain") == "rn"
    assert shorten("cs50") == "cs50"

def test_shorten_uppercase():
    assert shorten("AEIOU") == ""
    assert shorten("cAt") == "ct"
    assert shorten("rAIn") == "rn"
    assert shorten("RAIN") == "RN"
    assert shorten("Ra..//in") == "R..//n"

