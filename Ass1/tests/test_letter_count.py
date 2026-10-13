import pytest
from Ass1.letter_count import count
import string
import numpy as np


def test_count():
    abc=string.ascii_lowercase
    l=len(abc)
    assert count(abc) == l*[1]
    assert count("") == l*[0]