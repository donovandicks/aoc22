from collections import defaultdict


def main():
    with open("input.txt", encoding="utf-8") as handler:
        batch = 0
        cals = defaultdict(int)
        for line in handler.readlines():
            if line == "\n":
                batch += 1
                continue

            cals[batch] += int(line.strip())

    top_cals = sorted(list(cals.values()), reverse=True)
    print(top_cals[:3], sum(top_cals[:3]))


if __name__ == "__main__":
    main()
