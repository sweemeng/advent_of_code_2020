import solution
import pytest


test_rules = [
    (
     "light red bags contain 1 bright white bag, 2 muted yellow bags.", 
     {"light red": {"bright white": 1, "muted yellow": 2}},
    ),
    (
     "bright white bags contain 1 shiny gold bag.",
     {"bright white": {"shiny gold": 1}},
    ),
    (
     "faded blue bags contain no other bags.",
     {"faded blue": {}},
    )
]


test_rule_trees = {
    "bright white": {"shiny gold": 1},
    "muted yellow": {"shiny gold": 2, "faded blue": 9},
    "dark orange": {"bright white": 3, "muted yellow": 4},
    "light red": {"bright white": 1, "muted yellow": 2},
}


full_rule_trees = {
    'light red': {'bright white': 1, 'muted yellow': 2},
    'dark orange': {'bright white': 3, 'muted yellow': 4},
    'bright white': {'shiny gold': 1},
    'muted yellow': {'shiny gold': 2, 'faded blue': 9},
    'shiny gold': {'dark olive': 1, 'vibrant plum': 2},
    'dark olive': {'faded blue': 3, 'dotted black': 4},
    'vibrant plum': {'faded blue': 5, 'dotted black': 6},
    'faded blue': {},
    'dotted black': {}
}


rules_str_1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


rules_str_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


@pytest.mark.parametrize("rule,expected",test_rules)
def test_parse_sentence(rule, expected):
    result = solution.parse_rule(rule)
    assert result == expected


def test_make_rule_tree():
    rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."""
    result = solution.make_rule_tree(rules.split("\n"))
    assert result == test_rule_trees


@pytest.mark.parametrize("color,rules,expected", [
        ("bright white", full_rule_trees, True),
        ("muted yellow", full_rule_trees, True),
        ("dark orange", full_rule_trees, True),
        ("light red", full_rule_trees, True),
        ("dark olive", full_rule_trees, False),
])
def test_check_gold(color, rules, expected):
    result = solution.check_bag(color, rules)
    exist = result != 0
    assert exist == expected
    

@pytest.mark.parametrize("rules,expected", [
        (rules_str_1, 32),
        (rules_str_2, 126),
])
def test_total_child_bag(rules, expected):
    rule_tree = solution.make_rule_tree(rules.split("\n"))

    total_child = solution.count_child("shiny gold", rule_tree)
    assert total_child == expected

