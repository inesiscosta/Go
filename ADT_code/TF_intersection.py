LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def create_intersection(col, lin):
    if type(col) == str and len(col) == 1 and 'A' <= col <= 'S' \
        and type(lin) == int and  1 <= lin <= 19:
            return 'blabla', ('nothing',lin), (col,)
        
    raise ValueError("create_intersection: invalid arguments") 

def obtain_col(pos):
    return pos[2][0]

def obtain_row(pos):
    return pos[1][1]

def is_intersection(arg):
    return type(arg) == tuple and len(arg) == 3 and arg[0] == 'blabla' \
        and type(arg[1]) == tuple and len(arg[1]) == 2 and arg[1][0] == 'nothing' \
            and type(arg[1][1]) == int and  1 <= arg[1][1] <= 19 \
                and type(arg[2]) == tuple and len(arg[2]) == 1 and type(arg[2][0]) == str and len(arg[2][0]) == 1 and  'A' <= arg[2][0] <= 'S'
                
def equal_intersections(pos1, pos2):
    return is_intersection(pos1) and is_intersection(pos2) and obtain_col(pos1) == obtain_col(pos2) and obtain_row(pos1) == obtain_row(pos2)

def intersection_to_str(pos):
    return f'{obtain_col(pos)}{obtain_row(pos)}'

def str_to_intersection(s):
    return create_intersection(s[0], int(s[1:]))

def obtain_adjacent_intersections(pos, last_pos):
    move = {
        'U': lambda x: 0 if obtain_row(x) == obtain_row(last_pos) else create_intersection(obtain_col(x), obtain_row(x)+1),
        'D': lambda x: 0 if obtain_row(x) == 1 else create_intersection(obtain_col(x), obtain_row(x)-1),
        'L': lambda x: '' if obtain_col(x) == 'A' else create_intersection(LETTERS[LETTERS.index(obtain_col(x))-1], obtain_row(x)),
        'R': lambda x: '' if obtain_col(x) == obtain_col(last_pos) else create_intersection(LETTERS[LETTERS.index(obtain_col(x))+1], obtain_row(x))
    }
    return tuple(move[d](pos) for d in ('D', 'L', 'R', 'U') if move[d](pos))
    
def sort_intersections(tup):
    return tuple(sorted(tup, key=lambda x:(obtain_row(x), obtain_col(x))))
