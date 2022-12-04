from typing import Tuple


def load_input() -> str:
    with open("input.txt") as h:
        return h.read()


def parse_line(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    range_1, range_2 = line.split(",")
    range_1_b, range_1_e = range_1.split("-")
    range_2_b, range_2_e = range_2.split("-")
    return (
        (int(range_1_b), int(range_1_e)),
        (int(range_2_b), int(range_2_e)),
    )


def solve_1(data: str) -> int:
    count = 0
    for line in data.split("\n"):
        ((range_1_b, range_1_e), (range_2_b, range_2_e)) = parse_line(line)
        if range_1_b <= range_2_b and range_1_e >= range_2_e:
            count += 1
            continue

        if range_2_b <= range_1_b and range_2_e >= range_1_e:
            count += 1
            continue

    return count


def solve_2(data: str) -> int:
    count = 0
    for line in data.split("\n"):
        ((range_1_b, range_1_e), (range_2_b, range_2_e)) = parse_line(line)
        if range_1_b in (range_2_b, range_2_e) or range_1_e in (range_2_b, range_2_e):
            count += 1
            continue

        if range_2_b < range_1_b < range_2_e:
            count += 1
            continue

        if range_2_b < range_1_e < range_2_e:
            count += 1
            continue

        if range_1_b < range_2_b < range_1_e:
            count += 1
            continue

        if range_1_b < range_2_e < range_1_e:
            count += 1
            continue

    return count


if __name__ == "__main__":
    input_data = load_input().strip()
    print(f"Solution 1: {solve_1(input_data)}")
    print(f"Solution 2: {solve_2(input_data)}")
