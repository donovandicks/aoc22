def main():
    with open("input.txt", encoding="utf-8") as handler:
        batches = handler.read().split("\n\n")

    highest = 0
    for batch in batches:
        batch_cals = sum(int(cal) for cal in batch.split("\n") if cal)
        if batch_cals > highest:
            highest = batch_cals

    print(highest)


if __name__ == "__main__":
    main()
