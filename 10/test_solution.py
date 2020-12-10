import solution

from collections import Counter
import pytest


test_data = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4,]
test_data_big = [
    28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 
    49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3,
]


@pytest.mark.parametrize("data,expected", [
        (test_data, Counter({1:7, 3:5})),
        (test_data_big, Counter({1:22, 3:10})),
])
def test_jolts_diff_distribution(data, expected):
    result,_ = solution.jolt_diff_dist(data)
    assert result == expected


@pytest.mark.parametrize("data,expected", [
        (test_data, 8),
        (test_data_big, 19208),
])
def test_count_arrangement(data, expected):
    result = solution.count_arrangement(data)
    assert result == expected
