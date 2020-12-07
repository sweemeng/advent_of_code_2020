import re


def parse_rule(rule):
    parent_pattern = r'(?P<parent>^[a-z]+\s[a-z]+)'
    match = re.match(parent_pattern, rule)
    parent = match.group("parent")
    data = {parent: {}}
    child_pattern = r"(?P<amount>\d+)\s(?P<color>[a-z]+\s[a-z]+)"
    matches = re.findall(child_pattern, rule)
    if matches:
        for amount, child in re.findall(child_pattern, rule):
            data[parent][child] = int(amount)
    return data


def make_rule_tree(rules):
    data = {}
    for rule in rules:
        temp = parse_rule(rule)
        data.update(temp)
    return data


def check_bag(color, rule, goal="shiny gold"):
    current = rule.get(color)
    if not current:
        return 0
    goal_count = current.get(goal)
    if goal_count:
        return goal_count
    else:
        total_goal = 0
        for child in current:
            total_goal = total_goal + check_bag(child, rule)
        return total_goal


def count_child(color, rules):
    child = rules.get(color)
    if not child:
        return 0
    total = 0
    for key in child:
        total = total + child[key] + child[key] * count_child(key, rules)
    return total


def main():
    f = open("input")
    data = f.readlines()
    rules = make_rule_tree(data)

    count = 0
    for rule in rules:
        amount = check_bag(rule, rules)
        if amount:
            count = count + 1

    print(f"total is {count}")

    total = count_child("shiny gold", rules)
    print(f"solution two is {total}")

if __name__ == "__main__":
    main()
