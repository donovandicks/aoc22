KEY = {
    "A": 1,  # rock
    "X": 1,
    "B": 2,  # paper
    "Y": 2,
    "C": 3,  # scissors
    "Z": 3,
}


def get_result(x: str, y: str) -> int:
    opp, me = KEY[x], KEY[y]
    if opp == me:
        return 3

    match (opp, me):
        case (1, 2) | (2, 3) | (3, 1):
            return 6
        case _:
            return 0


def main():
    score = 0
    with open("input.txt", encoding="utf-8") as h:
        for line in h.readlines():
            opp, me = line.strip().split()
            score += KEY[me] + get_result(opp, me)

    print(score)


if __name__ == "__main__":
    main()
