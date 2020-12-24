
def get_input():
    with open('day22/input') as f:
        _ = f.readline()
        line = f.readline().strip()
        p1_deck = []
        while line:
            p1_deck.append(int(line))
            line = f.readline().strip()

        _ = f.readline()
        line = f.readline().strip()
        p2_deck = []
        while line:
            p2_deck.append(int(line))
            line = f.readline().strip()

    return p1_deck, p2_deck

def play_game(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card2 > card1:
            deck2.append(card2)
            deck2.append(card1)
        else:
            print('tied')

    return deck1, deck2

def play_recursive_game(deck1, deck2, depth=1):
    past_rounds = []
    while len(deck1) > 0 and len(deck2) > 0:
        rnd = (tuple(deck1), tuple(deck2))
        if depth == 1:
            print(rnd)
        if rnd in past_rounds:
            return [-1], []
        else:
            # Add past round
            past_rounds.append(rnd)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        # Check for recursive case
        if card1 <= len(deck1) and card2 <= len(deck2):
            d1, d2 = play_recursive_game(deck1[:card1], deck2[:card2], depth=depth+1)
            winner_1 = len(d1) > 0
        else:
            winner_1 = card1 > card2

        if winner_1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    return deck1, deck2

def part_1():
    p1_deck, p2_deck = get_input()
    p1_deck, p2_deck = play_game(p1_deck, p2_deck)

    if p1_deck:
        deck = p1_deck
    else:
        deck = p2_deck

    return sum([card * num for card, num in zip(reversed(deck), range(1, len(deck) + 1))])

def part_2():
    p1_deck, p2_deck = get_input()
    p1_deck, p2_deck = play_recursive_game(p1_deck, p2_deck)

    if p1_deck:
        deck = p1_deck
    else:
        deck = p2_deck

    return sum([card * num for card, num in zip(reversed(deck), range(1, len(deck) + 1))])

if __name__ == "__main__":
    #print(part_1())
    print(part_2())