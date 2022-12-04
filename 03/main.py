import string


def calc_prior(letter) -> int:
    return string.ascii_letters.find(letter) + 1


def main():
    i = 1
    priority = 0
    with open("input.txt") as h:
        group: list[set] = []
        for line in h.readlines():
            group.append(set(line.strip()))
            if i % 3 == 0:
                priority += calc_prior(list(set.intersection(*group))[0])
                group = []
            i += 1

    print(priority)


if __name__ == "__main__":
    main()
