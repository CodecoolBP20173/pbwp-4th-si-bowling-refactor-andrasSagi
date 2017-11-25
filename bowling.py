def score(game):
    result = 0
    frame = 1
    in_first_half = True
    last_turn = 0
    for turn in range(len(game)):
        this_turn = game[turn]
        if this_turn == '/':
            result += 10 - last_turn
        else:
            result += get_value(this_turn)
        if frame < 10 and get_value(this_turn) == 10:
            next_turn = game[turn+1]
            result += get_value(next_turn)
            if this_turn.upper() == 'X':
                if game[turn+2] == '/':
                    result += 10 - get_value(next_turn)
                else:
                    result += get_value(game[turn+2])
        last_turn = get_value(this_turn)
        if not in_first_half:
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
        if this_turn.upper() == 'X':
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
