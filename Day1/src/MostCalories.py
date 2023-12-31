def get_most_calories(calorie_list: str):
    output = []

    calorie_sum = 0
    for calorie in calorie_list.split('\n'):
        if calorie == '':
            output.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += int(calorie)
    
    return max(output)


def get_top_three_calories(calorie_list: str):
    output = []

    calorie_sum = 0
    for calorie in calorie_list.split('\n'):
        if calorie == '':
            output.append(calorie_sum)
            calorie_sum = 0
        else:
            calorie_sum += int(calorie)
    output.append(calorie_sum)

    output.sort(reverse=True)

    return sum(output[:3])
