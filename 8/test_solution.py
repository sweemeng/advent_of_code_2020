import solution
import pytest


data = [
    ("nop", 0),
    ("acc", 1),
    ("jmp", 4),
    ("acc", 3),
    ("jmp", -3),
    ("acc", -99),
    ("acc", 1),
    ("jmp", -4),
    ("acc", 6),
]


@pytest.mark.parametrize("initial,amount,expected", [
        (0, 100, 100),
        (10, 100, 110),
        (10, -10, 0),
])
def test_machine_acc(initial, amount, expected):
    machine = solution.Machine()
    machine.accumulator = initial
    machine.acc(amount)
    assert machine.accumulator == expected


@pytest.mark.parametrize("initial,amount,expected", [
        (0, 4, 4),
        (5, 4, 9),
        (5, -4, 1),
])
def test_machine_jmp(initial, amount, expected):
    machine = solution.Machine()
    machine.ptr = initial
    machine.jmp(amount)
    assert machine.ptr == expected


@pytest.mark.parametrize("ops,amount,initial,expected", [
        ("jmp", 2, 0, 2),
        ("acc", 1, 0, 1),
        ("nop", 0, 0, 1),
])
def test_machine_ops(ops, amount, initial, expected):
    machine = solution.Machine()
    machine.ptr = initial
    getattr(machine, ops)(amount)
    assert machine.ptr == expected


@pytest.mark.parametrize("ops,amount,curr_ptr,expected", [
        ("jmp", 4, 2, ("acc", 1)),
        ("nop", 0, 0, ("acc", 1)),
        ("acc", 1, 1, ("jmp", 4)),
        ("jmp", -4, 7, ("acc", 3)),
])
def test_machine_ops_register(ops, amount, curr_ptr, expected): 
    machine = solution.Machine(data=data)
    machine.ptr = curr_ptr
    getattr(machine, ops)(amount)
    assert machine.data[machine.ptr] == expected


def test_load_data():
    codes = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    machine = solution.Machine()
    machine.load_code(codes.split("\n"))
    assert machine.data == data
