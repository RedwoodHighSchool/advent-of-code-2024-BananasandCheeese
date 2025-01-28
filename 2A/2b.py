def main():
    with open("./input2.txt") as file:
        reports = [line.split() for line in file]

    part2(reports)


def part2(reports):
    valid_reports = 0

    for report in reports:
        ints = list(map(int, report))

        if is_valid_report(ints):
            valid_reports += 1
            continue

        valid_with_dampener = False

        for i in range(len(ints)):
            modified_report = [x for j, x in enumerate(ints) if j != i]

            if is_valid_report(modified_report):
                valid_with_dampener = True
                break

        if valid_with_dampener:
            valid_reports += 1

    print(valid_reports)


def is_valid_report(levels):
    is_increasing = is_increasing_sequence(levels)
    is_decreasing = is_decreasing_sequence(levels)

    if not is_increasing and not is_decreasing:
        return False

    for i in range(len(levels) - 1):
        diff = abs(levels[i + 1] - levels[i])
        if diff < 1 or diff > 3:
            return False

    return True


def is_increasing_sequence(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True


def is_decreasing_sequence(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            return False
    return True


if __name__ == "__main__":
    main()
