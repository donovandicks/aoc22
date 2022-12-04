KEY = {
    "A": 1,  # rock
    "X": 1,
    "B": 2,  # paper
    "Y": 2,
    "C": 3,  # scissors
    "Z": 3,
}

WINNING_MOVES = {
    1: 2,
    2: 3,
    3: 1,
}


def calc_score(x: str, y: str) -> int:
    if y == "Y":
        return 3 + KEY[x]

    if y == "Z":
        return 6 + WINNING_MOVES[KEY[x]]

    if y == "X":
        return 0 + WINNING_MOVES[KEY[x] % 3 + 1]

    # unreachable
    raise NotImplementedError()


def main():
    score = 0
    with open("input.txt", encoding="utf-8") as h:
        for line in h.readlines():
            opp, goal = line.strip().split()
            score += calc_score(opp, goal)

    print(score)


if __name__ == "__main__":
    main()
