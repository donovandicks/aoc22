def main():
    with open("input.txt", encoding="utf-8") as handler:
        batches = handler.read().split("\n\n")

    cals = []
    for batch in batches:
        cals.append(sum(int(cal) for cal in batch.split("\n") if cal))

    cals.sort(reverse=True)
    print(cals[:3], sum(cals[:3]))


if __name__ == "__main__":
    main()
