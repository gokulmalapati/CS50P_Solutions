from um import count
import pytest

def test_work():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Album is good") == 0
    assert count(" um , thanks for the um.") == 2

