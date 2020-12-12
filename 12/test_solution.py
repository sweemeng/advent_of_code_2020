import solution
import pytest


@pytest.mark.parametrize("command,pos,heading,expected",[
        ("F10", (0,0), (0,1), (0,10)),
        ("N3", (0,10), (0,1), (3,10)),
        ("F7", (3,10), (0,1), (3,17)),
        ("R90",(3,17), (0,1), (3,17)),
        ("F11", (3,17), (-1,0), (-8,17)),
])
def test_move_ship(command, pos, heading, expected):
    ship = solution.Ship()
    ship.heading = heading
    ship.pos = pos
    ship.move(command)
    assert ship.pos == expected


@pytest.mark.parametrize("command,heading,expected",[
    ("R90", (0,1), (-1,0)),
    ("L90", (0,1), (1,0)),
    ("R180", (0,1), (0,-1)),
    ("L180", (0,1), (0,-1)),
    ("R270", (0,1), (1,0)),
    ("L270", (0,1), (-1,0)),
])
def test_change_heading(command, heading, expected):
    ship = solution.Ship()
    ship.heading = heading
    ship.move(command)
    assert ship.heading == expected


def test_move_all():
    cmds = ["F10","N3","F7","R90","F11"]
    ship = solution.Ship()
    for cmd in cmds:
        ship.move(cmd)
    assert ship.pos == (-8,17)


@pytest.mark.parametrize("command,pos,waypoint,expected",[
        ("F10", (0,0), (1,10), (10,100)),
        ("N3", (10,100), (1,10), (10,100)),
        ("R90", (38,170), (4,10), (38, 170)),
])
def test_move_waypoint_mode(command, pos, waypoint, expected):
    ship = solution.Ship(waypoint_mode=True)
    ship.pos = pos
    ship.waypoint = waypoint
    ship.move(command)
    assert ship.pos == expected


@pytest.mark.parametrize("command,waypoint,expected", [
        ("N3", (1,10), (4,10)),
        ("S3", (1,10), (-2,10)),
        ("E3", (1,10), (1,13)),
        ("W3", (1,10), (1,7)),
])
def test_move_news_wayppoint_mode(command, waypoint, expected):
    ship = solution.Ship(waypoint_mode=True)
    ship.waypoint = waypoint
    ship.move(command)
    assert ship.waypoint == expected


@pytest.mark.parametrize("command,waypoint,expected",[
        ("R90",(4,10), (-10,4)),
        ("R180",(4,10), (-4,-10)),
        ("R270",(4,10), (10,-4)),
        ("L90", (4,10), (10,-4)),
        ("L180", (4,10), (-4,-10)),
        ("L270", (4,10), (-10,4)),

])
def test_move_rotate_waypoint_mode(command, waypoint, expected):
    ship = solution.Ship(waypoint_mode=True)
    ship.waypoint = waypoint
    ship.move(command)
    assert ship.waypoint == expected


def test_move_all_waypoint_mode():
    cmds = ["F10","N3","F7","R90","F11"]
    ship = solution.Ship(waypoint_mode=True)
    ship.waypoint = (1, 10)
    for cmd in cmds:
        ship.move(cmd)
    assert ship.pos == (-72,214)

