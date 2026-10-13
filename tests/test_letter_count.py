import pytest
from src.Ass1.letter_count import count


def test_count():
    assert count("hello") == 5
    assert count("world") == 5
    assert count("") == 0