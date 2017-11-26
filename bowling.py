def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for turn in range(len(game)):
        this_turn = game[turn]
        if is_spare(this_turn):
            result += 10 - last_turn
            if frame < 10:
                next_turn = game[turn+1]
                result += get_value(next_turn)
        else:
            result += get_value(this_turn)
        if is_strike(this_turn):
            if frame < 10:
                next_turn = game[turn+1]
                result += get_value(next_turn)
                second_next_turn = game[turn+2]
                if is_spare(second_next_turn):
                    result += 10 - get_value(next_turn)
                else:
                    result += get_value(second_next_turn)
            in_first_half = True
            frame += 1
            continue
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        last_turn = get_value(this_turn)
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
