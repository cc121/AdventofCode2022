def convert_stack_ids(stack_ids):
    return [stack_id for stack_id in stack_ids.split(' ') if stack_id != '']


def convert_stacks(stacks, stack_ids):
    # Create a dictionary that has a list of containers per stack ids
    stack_data = {stack_id: [] for stack_id in stack_ids}

    # Parse the stack levels starting from the bottom and record the contains in the dictionary
    for stack in stacks[::-1]:
        i = 0
        count = 1
        variable = ''
        stack_id = 1
        while i < len(stack):
            if count <= 3:
                variable += stack[i]
                count += 1
            else:
                variable = variable[1:2]
                if variable != ' ':
                    stack_data[str(stack_id)].append(variable)

                variable = ''
                count = 1

                stack_id += 1
            i += 1

        # Handle the last stack/level
        variable = variable[1:2]
        if variable != ' ':
            stack_data[str(stack_id)].append(variable)

    return stack_data


def convert_instructions(instructions):
    data = []
    for instruction in instructions:
        data.append([val for i, val in enumerate(instruction.split(' ')) if i not in [0, 2, 4]])

    return data


def move_stacks(source, target, stacks):
    container = stacks[source].pop()
    stacks[target].append(container)

    return stacks


def move_stacks_9001(source, target, quantity, stacks):
    containers = []
    while quantity > 0:
        containers.append(stacks[source].pop())
        quantity -= 1
    stacks[target].extend(containers[::-1])

    return stacks



def calculate_result(stacks, stack_ids):
    result = ''
    for stack_id in stack_ids:
        result += stacks[stack_id][-1]

    return result


def part1(input_list):
    input_list = input_list.split('\n')
    i = 0
    n = len(input_list)

    # Get stacks
    stacks = []
    while '[' in input_list[i]:
        stacks.append(input_list[i])
        i += 1

    # Get total number of stacks
    stack_ids = input_list[i]
    i += 2

    stack_ids = convert_stack_ids(stack_ids)
    stacks = convert_stacks(stacks, stack_ids)

    # get instuctions
    instructions = []
    while i < n:
        instructions.append(input_list[i])
        i += 1

    instructions = convert_instructions(instructions)
    for quantity, source_stack, target_stack in instructions:
        quantity = int(quantity)
        while quantity > 0:
            stacks = move_stacks(source_stack, target_stack, stacks)
            quantity -= 1

    return calculate_result(stacks, stack_ids)


def part2(input_list):
    input_list = input_list.split('\n')
    i = 0
    n = len(input_list)

    # Get stacks
    stacks = []
    while '[' in input_list[i]:
        stacks.append(input_list[i])
        i += 1

    # Get total number of stacks
    stack_ids = input_list[i]
    i += 2

    stack_ids = convert_stack_ids(stack_ids)
    stacks = convert_stacks(stacks, stack_ids)

    # get instuctions
    instructions = []
    while i < n:
        instructions.append(input_list[i])
        i += 1

    instructions = convert_instructions(instructions)
    for quantity, source_stack, target_stack in instructions:
        quantity = int(quantity)
        stacks = move_stacks_9001(source_stack, target_stack, quantity, stacks)

    return calculate_result(stacks, stack_ids)
