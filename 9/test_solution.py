from solution import process

import pytest


test_data = [
    35, 
    20, 
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


@pytest.mark.parametrize("pos,window_size,expected",[
        (14, 5, False),
        (5, 5, True),
        (6, 5, True),
])
def test_valid(pos, window_size, expected):
    result = process(test_data, pos, window_size)
    assert expected == result
