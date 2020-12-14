import solution
import pytest


@pytest.mark.parametrize("value,mask,expected",[
        (11, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X","000000000000000000000000000001001001"),
        (0, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", "000000000000000000000000000001000000"),
        (101, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", "000000000000000000000000000001100101"),
])
def test_mask_value(value, mask, expected):
    result = solution.mask_value(value, mask)
    assert result == expected


@pytest.mark.parametrize("value,mask,expected",[
        (42, "000000000000000000000000000000X1001X", "000000000000000000000000000000X1101X"),
        (26, "00000000000000000000000000000000X0XX", "00000000000000000000000000000001X0XX"),
])
def test_mask_value_keep_all(value, mask, expected):
    result = solution.mask_value(value, mask,keep_all=True)
    assert result == expected


expected_addresses = [
    [
        "000000000000000000000000000000011010",
        "000000000000000000000000000000011011",
        "000000000000000000000000000000111010",
        "000000000000000000000000000000111011",
    ],
    [
        "000000000000000000000000000000010000",
        "000000000000000000000000000000010001",
        "000000000000000000000000000000010010",
        "000000000000000000000000000000010011",
        "000000000000000000000000000000011000",
        "000000000000000000000000000000011001",
        "000000000000000000000000000000011010",
        "000000000000000000000000000000011011",
    ]
]


@pytest.mark.parametrize("template,expected",[
        ("000000000000000000000000000000X1101X", expected_addresses[0]),
        ("00000000000000000000000000000001X0XX", expected_addresses[1]),
])
def test_generate_address(template,expected):
    result = solution.generate_addresses(template)
    
    assert expected == result

def test_populate_mems():
    test_values = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0",
    ]
    expected = {
        7: 101,
        8: 64,
    }
    result = solution.populate_mems(test_values)
    assert result == expected 


def test_populate_mems_version_2():
    test_values = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1",
    ]
    expected = {
        16: 1,
        17: 1,
        18: 1,
        19: 1,
        24: 1,
        25: 1,
        26: 1,
        27: 1,
        58: 100,
        59: 100,
    }
    result = solution.populate_mems(test_values,version=2)
    assert result == expected 

