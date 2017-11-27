def score(game):
    '''
    Calculate the score of a player in a game of bowling

    Arguments:
        game: bowling roll points input as a string

    Returns:
        resulting points as integer
    '''
    result = 0
    frame = 1
    in_first_half = True
    for turn in range(len(game)):
        this_turn = game[turn]
        result += points_if_spare(turn, game, frame)
        if is_strike(this_turn):
            if frame < 10:
                result += get_value(game[turn+1])
                if is_spare(game[turn+2]):
                    result += 10 - get_value(game[turn+1])
                else:
                    result += get_value(game[turn+2])
            in_first_half = True
            frame += 1
            continue
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    '''
    Get the value of character as points

    Arguments:
        char: individual character from each turn of bowling, as string

    Returns:
        character's value as integer
    '''
    if char.upper() == 'X' or char == '/':
        return 10
    elif char == '-':
        return 0
    elif 0 < int(char) < 10:
        return int(char)
    else:
        raise ValueError()


def is_strike(turn):
    ''' Decide if turn is a strike '''
    if turn.upper() == 'X':
        return True


def is_spare(turn):
    ''' Decide if turn is a spare '''
    if turn == '/':
        return True


def points_if_spare(roll, game, frame):
    '''
    Calculate points of a roll based on if it is a spare

    Arguments:
        roll: current roll, as integer
        game: the results of the bowling game as a string
        frame: current frame as integer

    Returns:
        points as integer
    '''
    this_turn = game[roll]
    points = 0
    if is_spare(this_turn):
        points += 10 - get_value(game[roll-1])
        if frame < 10:
            points += get_value(game[roll+1])
    else:
        points += get_value(this_turn)
    return points
