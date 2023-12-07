from enum import Enum

players = open("input.txt", "r", encoding="utf-8").read().strip().splitlines()


class HandType(Enum):
    FIVE = 7
    FOUR = 6
    FULL = 5
    THREE = 4
    TWO = 3
    ONE = 2
    HIGH = 1

    def __lt__(self, obj):
        return self.value < obj.value


def evaluate(hand: list[int]):
    hand = sorted(hand)
    hand_set = set(hand)
    if len(hand_set) == 1:
        return HandType.FIVE
    elif hand.count(hand[0]) == 4 or hand.count(hand[-1]) == 4:
        return HandType.FOUR
    elif (hand.count(hand[0]) == 3 and hand.count(hand[-1]) == 2) or (
        hand.count(hand[0]) == 2 and hand.count(hand[-1]) == 3
    ):
        return HandType.FULL
    elif [hand.count(c) for c in hand_set].count(3) == 1:
        return HandType.THREE
    elif [hand.count(c) for c in hand_set].count(2) == 2:
        return HandType.TWO
    elif [hand.count(c) for c in hand_set].count(2) == 1:
        return HandType.ONE
    else:
        return HandType.HIGH


def process_joker(hand: list[int]):
    original = evaluate(hand)
    if 0 not in hand:
        return original

    hand_sorted = sorted(hand)
    if hand.count(0) >= 4:
        return HandType.FIVE
    elif hand.count(0) == 3:
        if len(set(hand)) == 2:
            return HandType.FIVE
        return HandType.FOUR
    elif hand.count(0) == 2:
        common = max(set(hand_sorted[2:]), key=hand.count)
        hand_sorted[0] = common
        hand_sorted[1] = common
        return evaluate(hand_sorted)
    elif hand.count(0) == 1:
        common = max(set(hand_sorted[1:]), key=hand.count)
        hand_sorted[0] = common
        return evaluate(hand_sorted)


class Hand:
    def __init__(self, hand, bid):
        self.bid = bid
        self.type = process_joker(hand)
        self.hand = hand

    def __lt__(self, obj):
        if self.type < obj.type:
            return True
        elif self.type > obj.type:
            return False

        if self.hand[0] < obj.hand[0]:
            return True
        elif self.hand[0] > obj.hand[0]:
            return False
        if self.hand[1] < obj.hand[1]:
            return True
        elif self.hand[1] > obj.hand[1]:
            return False
        if self.hand[2] < obj.hand[2]:
            return True
        elif self.hand[2] > obj.hand[2]:
            return False
        if self.hand[3] < obj.hand[3]:
            return True
        elif self.hand[3] > obj.hand[3]:
            return False
        return self.hand[4] < obj.hand[4]


hands: list[Hand] = []
for player in players:
    raw_hand, raw_bid = player.split()
    bid = int(raw_bid)
    hand = [
        int(
            n.replace("A", "14")
            .replace("K", "13")
            .replace("Q", "12")
            .replace("J", "11")
            .replace("T", "10")
        )
        for n in raw_hand
    ]

    hands.append(Hand(hand, bid))
hands.sort()

total = 0
for i, h in enumerate(hands):
    total += (i + 1) * h.bid
print(total)

hands = []
for player in players:
    raw_hand, raw_bid = player.split()
    bid = int(raw_bid)
    hand = [
        int(
            n.replace("A", "13")
            .replace("K", "12")
            .replace("Q", "11")
            .replace("T", "10")
            .replace("J", "0")
        )
        for n in raw_hand
    ]

    hands.append(Hand(hand, bid))
hands.sort()

total = 0
for i, h in enumerate(hands):
    total += (i + 1) * h.bid
print(total)
