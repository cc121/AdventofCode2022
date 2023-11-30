from collections import Counter

def part1(input_list):
    i = 0
    n = len(input_list)
    window = []
    while i < n:
        letter = input_list[i]
        if i < 4:
            window.append(letter)
        else:
            c = Counter(window)
            for key, val in c.items():
                if val > 1:
                    break
            else:
                return i
            window = window[1:]
            window.append(letter)
        i += 1


def part2(input_list):
    i = 0
    n = len(input_list)
    window = []
    while i < n:
        letter = input_list[i]
        if i < 14:
            window.append(letter)
        else:
            c = Counter(window)
            for key, val in c.items():
                if val > 1:
                    break
            else:
                return i
            window = window[1:]
            window.append(letter)
        i += 1
