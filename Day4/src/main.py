def part1(input_list):
    input_list = input_list.split('\n')

    count = 0
    for pair in input_list:
        first, second = pair.split(',')

        first = [int(val) for val in first.split('-')]
        second = [int(val) for val in second.split('-')]

        case_1 = first[0] <= second[0] and first[1] >= second[1]
        case_2 = first[0] >= second[0] and first[1] <= second[1]
        if case_1 or case_2:
            count += 1

    return count


def part2(input_list):
    input_list = input_list.split('\n')

    count = 0
    for pair in input_list:
        first, second = pair.split(',')

        first = [int(val) for val in first.split('-')]
        second = [int(val) for val in second.split('-')]

        case_1 = first[0] <= second[0] and first[1] >= second[0]
        case_2 = first[0] >= second[0] and first[0] <= second[1]
        if case_1 or case_2:
            count += 1

    return count
