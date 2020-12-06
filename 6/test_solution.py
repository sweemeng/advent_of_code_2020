from solution import solution

import pytest

@pytest.mark.parametrize("answers,expected", [
        (['abc\n'], [{'a','b','c'}]),
        (['a\n','b\n','c\n'], [{'a','b','c'}]),
        (['abc', '', 'a', 'b', 'c'], [{'a','b','c'}, {'a','b','c'}]),
        (['a','b','c','','a','a','a','a'], [{'a','b','c'}, {'a'}])
])
def test_all_answers(answers, expected):
    result = solution(answers)
    assert result == expected


@pytest.mark.parametrize("answers,expected", [
        (['abc\n'], [{'a','b','c'}]),
        (['a\n','b\n','c\n'], [set()]),
        (['abc', '', 'a', 'b', 'c'], [{'a','b','c'}, set()]),
        (['a','b','c','','a','a','a','a'], [set(), {'a'}]),
        (['ab', 'ac'], [{'a'}]),
])
def test_common_answers(answers, expected):
    result = solution(answers, operation='intersection')
    assert result == expected
