LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def create_intersection(col, lin):
    if type(col) == str and len(col) == 1 and 'A' <= col <= 'S' \
        and type(lin) == int and  1 <= lin <= 19:
            return 'blabla', ('nothing',lin), (col,)
        
    raise ValueError("create_intersection: invalid arguments") 

def get_col(pos):
    return pos[2][0]

def get_row(pos):
    return pos[1][1]

def is_intersection(arg):
    return type(arg) == tuple and len(arg) == 3 and arg[0] == 'blabla' \
        and type(arg[1]) == tuple and len(arg[1]) == 2 and arg[1][0] == 'nothing' \
            and type(arg[1][1]) == int and  1 <= arg[1][1] <= 19 \
                and type(arg[2]) == tuple and len(arg[2]) == 1 and type(arg[2][0]) == str and len(arg[2][0]) == 1 and 'A' <= arg[2][0] <= 'S'
                
def equal_intersections(pos1, pos2):
    return is_intersection(pos1) and is_intersection(pos2) and get_col(pos1) == get_col(pos2) and get_row(pos1) == get_row(pos2)

def intersection_to_str(pos):
    return f'{get_col(pos)}{get_row(pos)}'

def str_to_intersection(s):
    return create_intersection(s[0], int(s[1:]))

def get_adjacent_intersections(pos, last_pos):
    move = {
        'U': lambda x: 0 if get_row(x) == get_row(last_pos) else create_intersection(get_col(x), get_row(x)+1),
        'D': lambda x: 0 if get_row(x) == 1 else create_intersection(get_col(x), get_row(x)-1),
        'L': lambda x: '' if get_col(x) == 'A' else create_intersection(LETTERS[LETTERS.index(get_col(x))-1], get_row(x)),
        'R': lambda x: '' if get_col(x) == get_col(last_pos) else create_intersection(LETTERS[LETTERS.index(get_col(x))+1], get_row(x))
    }
    return tuple(move[d](pos) for d in ('D', 'L', 'R', 'U') if move[d](pos))
    
def sort_intersections(tup):
    return tuple(sorted(tup, key=lambda x:(get_row(x), get_col(x))))
