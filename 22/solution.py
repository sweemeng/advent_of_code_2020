from copy import deepcopy


PLAYER_1 = 1
PLAYER_2 = 2

def load_deck(f):
    player_1 = []
    player_2 = []
    deck = None
    for i in f:
        i = i.strip()
        if not i:
            continue
        if "Player 1" in i:
            deck = player_1
        elif "Player 2" in i:
            deck = player_2
        else:
            deck.append(int(i))
    return player_1, player_2


def play_card(player_1, player_2):
    winner = None
    cards = None
    if player_1 > player_2:
        winner = 1
        cards = [player_1, player_2]
    else:
        winner = 2
        cards = [player_2, player_1]
    return winner, cards


def play_game(f):
    player_1 = 1
    player_2 = 2
    deck_1, deck_2 = load_deck(f)
    decks = {player_1: deck_1, player_2: deck_2}

    done = False

    while not done:
        winner = None
        card_1 = decks[player_1].pop(0)
        card_2 = decks[player_2].pop(0)
        
        winner, cards = play_card(card_1, card_2)
        print(f"card 1: {card_1}")
        print(f"card 2: {card_2}")
        print(f"Winner: {winner}")
        print(f"Cards: {cards}")

        decks[winner] = decks[winner] + cards
        print(f"Player 1: {decks[player_1]}")
        print(f"Player 2: {decks[player_2]}")
        done = not all((len(decks[player_1]), len(decks[player_2])))

    if decks[player_1]:
        deck = decks[player_1]
    else:
        deck = decks[player_2]

    scores = zip(deck, range(len(deck), 0, -1))
    score = sum([x*y for x,y in scores])
    print(score)


def play_recursion(deck_1, deck_2):
    winner = None

    done = False
    decks = {PLAYER_1: deepcopy(deck_1), PLAYER_2: deepcopy(deck_2)}
    seen = {PLAYER_1: set(), PLAYER_2: set()}

    while not done:
        recurse_game = False
        print(f"Current decks 1: {decks[PLAYER_1]}")
        print(f"Old Decks 1: {len(seen[PLAYER_1])}")

        print(f"Current decks 2: {decks[PLAYER_2]}")
        print(f"Old Decks 2: {len(seen[PLAYER_2])}")
        if tuple(decks[PLAYER_1]) in seen[PLAYER_1]:
            winner = PLAYER_1
            break
        else:
            seen[PLAYER_1].add(tuple(decks[PLAYER_1]))

        if tuple(decks[PLAYER_2]) in seen[PLAYER_2]:
            winner = PLAYER_1
            break
        else:
            seen[PLAYER_2].add(tuple(decks[PLAYER_2]))


        card_1 = decks[PLAYER_1].pop(0)
        card_2 = decks[PLAYER_2].pop(0)
        print(f"Card 1: {card_1}")
        print(f"Card 2: {card_2}")
        recurse_game = all([
            card_1 <= len(decks[PLAYER_1]),
            card_2 <= len(decks[PLAYER_2]),
        ])
        winning = {PLAYER_1: [card_1, card_2], PLAYER_2: [card_2, card_1]}
        if recurse_game:
            winner, _ = play_recursion(
                    decks[PLAYER_1][:card_1], 
                    decks[PLAYER_2][:card_2],
                )
            decks[winner] += winning[winner]
        else:
            winner, _ = play_card(card_1, card_2)
            decks[winner] += winning[winner]
        done = not all([len(decks[PLAYER_1]), len(decks[PLAYER_2])])

    return winner, (decks[PLAYER_1], decks[PLAYER_2])
        

def play_game_2(f):
    deck_1, deck_2 = load_deck(f)
    winner, decks = play_recursion(deck_1, deck_2)
    print(winner, decks)
    if winner == PLAYER_1:
        deck = decks[0]
    else:
        deck = decks[1]
    scores = zip(deck, range(len(deck), 0, -1))
    score = sum([x*y for x,y in scores])
    print(score)



def sample_main():
    from io import StringIO
    f = StringIO("""Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""")
    play_game(f)
    f = StringIO("""Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""")

    play_game_2(f)


def main():
    f = open("input")
    play_game(f)
    f = open("input")
    play_game_2(f)
    
def infinite_main():
    from io import StringIO
    f = StringIO("""Player 1:
43
19

Player 2:
2
29
14""")
    play_game_2(f)


if __name__ == "__main__":
    main()
