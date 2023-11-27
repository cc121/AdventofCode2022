def get_score(o, m):
    if m == "ROCK":
        my_score = 1
        if o == "ROCK":
            outcome_score = 3
        elif o == "PAPER":
            outcome_score = 0
        elif o == "SCISSORS":
            outcome_score = 6
    elif m == "PAPER":
        my_score = 2
        if o == "ROCK":
            outcome_score = 6
        elif o == "PAPER":
            outcome_score = 3
        elif o == "SCISSORS":
            outcome_score = 0
    elif m == "SCISSORS":
        my_score = 3
        if o == "ROCK":
            outcome_score = 0
        elif o == "PAPER":
            outcome_score = 6
        elif o == "SCISSORS":
            outcome_score = 3

    return my_score + outcome_score


def calculate_score(strategy_guide):
    opponent_hand_translation = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS"
    }

    my_hand_translation = {
        "X": "ROCK",
        "Y": "PAPER",
        "Z": "SCISSORS"
    }

    total_score = 0
    for game_round in strategy_guide.split('\n'):
        opponent_hand, my_hand = game_round.split(' ')

        total_score += get_score(opponent_hand_translation[opponent_hand], my_hand_translation[my_hand])

    return total_score


def calculate_hand_and_score(strategy_guide):
    opponent_hand_translation = {
        "A": "ROCK",
        "B": "PAPER",
        "C": "SCISSORS"
    }

    goal_translation = {
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN"
    }

    total_score = 0
    for game_round in strategy_guide.split('\n'):
        opponent_hand, goal = game_round.split(' ')
        translated_opponent_hand = opponent_hand_translation[opponent_hand]

        translated_goal = goal_translation[goal]
        if translated_goal == "DRAW":
            my_hand = translated_opponent_hand
        elif translated_goal == "LOSE":
            if translated_opponent_hand == "ROCK":
                my_hand = "SCISSORS"
            elif translated_opponent_hand == "PAPER":
                my_hand = "ROCK"
            elif translated_opponent_hand == "SCISSORS":
                my_hand = "PAPER"
        else:
            if translated_opponent_hand == "ROCK":
                my_hand = "PAPER"
            elif translated_opponent_hand == "PAPER":
                my_hand = "SCISSORS"
            elif translated_opponent_hand == "SCISSORS":
                my_hand = "ROCK"

        total_score += get_score(translated_opponent_hand, my_hand)

    return total_score