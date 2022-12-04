import string


def calc_prior(letter) -> int:
    return string.ascii_letters.find(letter) + 1


def main():
    priority = 0
    with open("input.txt") as h:
        for line in h.readlines():
            c1, c2 = line[: (len(line) // 2)], line[(len(line) // 2) :]
            priority += calc_prior(list(set(c1).intersection(c2))[0])

    print(priority)


if __name__ == "__main__":
    main()
