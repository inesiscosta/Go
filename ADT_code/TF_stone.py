from random import randint

def create_white_stone():
    return ['stone', '.O.', 'more', (3.14, randint(0, 10**6))]

def create_black_stone():
    return ['stone', '.X.', 'more', (3.14, randint(0, 10**6))]

def create_neutral_stone():
    return ['stone', '...', 'more', (3.14, randint(0, 10**6))]

def is_stone(arg):
    return isinstance(arg, list) and len(arg) == 4 and arg[0] == 'stone' and arg[2] == 'more' and \
        isinstance(arg[3], tuple) and arg[3][0] == 3.14 and isinstance(arg[3][1], int) and \
        (arg[1] == '.O.' or arg[1] == '.X.' or arg[1] == '...')
        
def is_white_stone(arg):
    return is_stone(arg) and arg[1] == '.O.'

def is_black_stone(arg):
    return is_stone(arg) and arg[1] == '.X.'

def equal_stones(s1, s2):
    return is_stone(s1) and is_stone(s2) and s1[1] == s2[1]

def stone_to_str(s):
    return s[1][1]

def is_player_stone(stone):
    return is_white_stone(stone) or is_black_stone(stone)

