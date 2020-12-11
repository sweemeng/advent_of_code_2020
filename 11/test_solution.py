import solution
import pytest


test_state = [
    [
        ['#','.',],
        ['#','.',],
    ],
    [

        ['#','#',],
        ['#','#',],
    ],
    [
        ['#','#','.'],
        ['#','#','#'],
    ],
    [
        ['#','#','#'],
        ['.','.','#'],
    ],
    [
        ['.','.','.'],
        ['.','#','.'],
        ['#','#','#'],
    ],
    [
        ['#','#','#'],
        ['#','#','#'],
        ['#','#','#'],
    ],
    [
        ['L','L','.'],
        ['L','L','L'],
        ['L','L','L'],
    ],
    [
        ['#','L','.'],
        ['L','L','L'],
        ['L','L','L'],
    ],
]


world_state = [
    """#.##.##.##
       #######.##
       #.#.#..#..
       ####.##.##
       #.##.##.##
       #.#####.##
       ..#.#.....
       ##########
       #.######.#
       #.#####.##""",
    """#.LL.L#.##
       #LLLLLL.L#
       L.L.L..L..
       #LLL.LL.L#
       #.LL.LL.LL
       #.LLLL#.##
       ..L.L.....
       #LLLLLLLL#
       #.LLLLLL.L
       #.#LLLL.##""",
]


@pytest.mark.parametrize("initial,pos,expected",[
    (test_state[0], (0,0), '#'),
    (test_state[1], (0,0), '#'),
    (test_state[2], (0,1), 'L'),
    (test_state[2], (1,1), 'L'),
    (test_state[3], (0,1), '#'),
    (test_state[4], (1,1), '#'),
    (test_state[5], (1,1), 'L'),
    (test_state[6], (1,1), '#'),
    (test_state[7], (1,1), 'L'),
])
def test_get_next_state(initial, pos, expected):
    x, y = pos
    result = solution.get_next_state(initial, x, y)
    assert result == expected


def test_move_world():
    start_world_state = [list(i.strip()) for i in world_state[0].split("\n")]
    end_world_state = [list(i.strip()) for i in world_state[1].split("\n")]
    result = solution.move_world(start_world_state)
    assert result == end_world_state


test_state_long = [
    """.......#.
       ...#.....
       .#.......
       .........
       ..#L....#
       ....#....
       .........
       #........
       ...#.....""",
    """.............
       .L.L.#.#.#.#.
       .............""",
    """.##.##.
       #.#.#.#
       ##...##
       ...L...
       ##...##
       #.#.#.#
       .##.##."""
]


@pytest.mark.parametrize("state,pos,expected",[
        (test_state_long[0],(4,3),['#','#','#','#','#','#','#','#']),
        (test_state_long[1],(1,1),['.','.','.','.','L','.','.','.']),
        (test_state_long[2],(3,3),['.','.','.','.','.','.','.','.']),
])
def test_get_next_adjecent_long(state, pos, expected):
    start_state = [list(i.strip()) for i in state.split("\n")]
    x, y = pos
    adjecents = solution.get_adjecent_long(start_state, x, y)
    assert adjecents == expected
