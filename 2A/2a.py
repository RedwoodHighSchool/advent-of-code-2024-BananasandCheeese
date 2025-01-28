def main():
    with open("./input2.txt") as file:
        reports = [line.split() for line in file]

    part1(reports)


def part1(reports):

    valid_reports = 0
    for report in reports:
        levels = list(map(int, report))

        if is_valid_report(levels):
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
