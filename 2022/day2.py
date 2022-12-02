def convert_move(move):
    converted_move = ""
    if (move == "X" or move == "A"):
        converted_move = "Rock"
    elif (move == "Y" or move == "B"):
        converted_move = "Paper"
    elif (move == "Z" or move == "C"):
        converted_move = "Scissors"
    return converted_move

def assert_move(move):
    play_to_make = ""
    if (move == "X"):
        play_to_make = "Lose"
    if (move == "Y"):
        play_to_make = "Draw"
    if (move == "Z"):
        play_to_make = "Win"

    return play_to_make

def score_for_choice(my_move):
    choice_score = 0

    if my_move == "Rock":
        choice_score = 1
    if my_move == "Paper":
        choice_score = 2
    if my_move == "Scissors":
        choice_score = 3

    return choice_score

def score_for_game(opponents_move, my_move):
    game_score = 0

    if (my_move == "Rock" and opponents_move == "Scissors") or (my_move == "Paper" and opponents_move == "Rock") or (my_move == "Scissors" and opponents_move == "Paper"):
        game_score = 6
    elif (my_move == opponents_move):
        game_score = 3
    else:
        game_score = 0

    return game_score

def determine_actual_move(result_to_follow, opponents_move):
    if (result_to_follow == "Win"):
        if (opponents_move == "Rock"):
            my_move = "Paper"
        if (opponents_move == "Paper"):
            my_move = "Scissors"
        if (opponents_move == "Scissors"):
            my_move = "Rock"
    
    if (result_to_follow == "Draw"):
            my_move = opponents_move
    
    if (result_to_follow == "Lose"):
        if (opponents_move == "Rock"):
            my_move = "Scissors"
        if (opponents_move == "Paper"):
            my_move = "Rock"
        if (opponents_move == "Scissors"):
            my_move = "Paper"

    return my_move

def calculate_score():
    score_for_choices = 0
    score_for_results = 0

    with open("C:/Users/NBURNESS/source/repos/side/AdventOfCode/2022/data/day2.txt") as file:
        for line in file:
                opponents_move = convert_move(line[0])
                my_move = convert_move(line[2])

                score_for_choices += score_for_choice(my_move)
                score_for_results += score_for_game(opponents_move, my_move)

    return score_for_choices + score_for_results

def calculate_score_part2():
    score_for_choices = 0
    score_for_results = 0

    with open("C:/Users/NBURNESS/source/repos/side/AdventOfCode/2022/data/day2.txt") as file:
        for line in file:
                opponents_move = convert_move(line[0])
                result_to_follow = assert_move(line[2])
                my_move = determine_actual_move(result_to_follow, opponents_move)

                score_for_choices += score_for_choice(my_move)
                score_for_results += score_for_game(opponents_move, my_move)
    return score_for_choices + score_for_results
    


if __name__ == "__main__":
    print("part1 score is: ", calculate_score())
    print("part2 score is: ", calculate_score_part2())