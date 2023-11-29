priorities = {letter: val+1 for val, letter in enumerate('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')}


def part1(input_list):
    priority_sum = 0
    for sack in input_list.split('\n'):
        mid = len(sack)//2
        left = sack[:mid]
        right = sack[mid:]
        for letter in left:
            if letter in right:
                priority_sum += priorities[letter]
                break
    return priority_sum


def part2(input_list):
    priority_sum = 0
    input_list = input_list.split('\n')
    for i in range(0, len(input_list), 3):
        first = input_list[i]
        second = input_list[i+1]
        third = input_list[i+2]

        for letter in first:
            if letter in second and letter in third:
                priority_sum += priorities[letter]
                break
    return priority_sum
