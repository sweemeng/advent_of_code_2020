import pytest
import solution


@pytest.mark.parametrize("input_pair,direction,expected", [
        ((0, 127), "F", (0, 63)),
        ((0, 63), "B", (32, 63)),
        ((32, 63), "F", (32, 47)),
        ((44, 47), "F", (44, 45)),
        ((44, 45), "F", (44, 44)),
        ((0, 7), "R", (4, 7)),
        ((4, 7), "L", (4, 5)),
        ((4, 5), "R", (5, 5)),

])
def test_partition(input_pair, direction, expected):
    result = solution.partition(input_pair, solution.DIRECTION[direction])
    assert result == expected


def test_get_seat():
    seat = "FBFBBFFRLR"
    result = solution.get_seat(seat)
    assert result == (44, 5)


def test_get_id():
    seat = "FBFBBFFRLR"
    result = solution.get_id(seat)
    assert result == 357

@pytest.mark.parametrize("input_direction,actual_direction", [
        ("F", solution.LOWER),
        ("B", solution.UPPER),
        ("L", solution.LOWER),
        ("R", solution.UPPER),
])
def test_direction_const(input_direction, actual_direction):
    assert solution.DIRECTION[input_direction] == actual_direction
