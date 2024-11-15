from random import randint

def create_empty_goban(n):
    if type(n) == int and n in (9, 13, 19):
        return [randint(0, 10**6), (n, {})]
    raise ValueError('create_empty_goban: invalid argument')    

def create_goban(n, white_intersections, black_intersections):
    if type(n) == int and n in (9, 13, 19):
        goban = create_empty_goban(n)
        if type(n) == int and n in (9, 13, 19) and \
            type(white_intersections) == tuple and all(is_intersection(i) and is_valid_intersection(goban, i) for i in white_intersections) and \
                type(black_intersections) == tuple and all(is_intersection(i) and is_valid_intersection(goban, i) for i in black_intersections):
                    for i in white_intersections: 
                        if is_player_stone(get_stone(goban, i)):
                            raise ValueError('create_goban: invalid arguments')   
                        place_stone(goban, i, create_white_stone())
                    
                    for i in black_intersections: 
                        if is_player_stone(get_stone(goban, i)):
                            raise ValueError('create_goban: invalid arguments')  
                        place_stone(goban, i, create_black_stone())
                    return goban
    
    raise ValueError('create_goban: invalid arguments')   

def create_copy_goban(board):
    return [board[0], (board[1][0], board[1][1].copy())]

def get_last_intersection(board):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return create_intersection(LETTERS[board[1][0]-1], board[1][0])

def get_stone(board, pos):
    if pos in board[1][1]:
        return board[1][1][pos]
    else:
        return create_neutral_stone()

def get_chain(board, pos):
    
    state = get_stone(board, pos)
    last = get_last_intersection(board)
    
    chain, to_check = [], [pos]
    
    while to_check:
        pos = to_check.pop()
        chain.append(pos)
        for new_pos in get_adjacent_intersections(pos, last):
            if equal_stones(get_stone(board, new_pos), state) and new_pos not in chain + to_check:
                to_check.append(new_pos)
                
    return sort_intersections(tuple(chain))

def place_stone(board, pos, stone):
    board[1][1][pos] = stone
    return board

def remove_stone(board, pos):
    if pos in board[1][1]:
        del board[1][1][pos]
    return board

def remove_chain(board, tuplo):
    for pos in tuplo:
        remove_stone(board, pos)
    return board

def is_goban(arg):
    def intersection_within_limits(i1, i2):
        return 'A' <= get_col(i1) <= get_col(i2) and 1 <= get_row(i1) <= get_row(i2)
    return isinstance(arg,list) and len(arg) == 2 and type(arg[0]) == int and \
        type(arg[1]) == tuple and len(arg[1]) == 2 and type(arg[1][0]) == int and arg[1][0] in (9, 13, 19) \
        and type(arg[1][1]) == dict and  all(is_intersection(k) for k in arg[1][1]) and \
            all(intersection_within_limits(k, get_last_intersection(arg)) for k in arg[1][1]) and \
                all(is_stone(arg[1][1][k]) for k in arg[1][1])
      
def is_valid_intersection(board, pos):
    def intersection_within_limits(i1, i2):
        return 'A' <= get_col(i1) <= get_col(i2) and 1 <= get_row(i1) <= get_row(i2)
    return intersection_within_limits(pos, get_last_intersection(board))

def equal_gobans(g1, g2):
    if is_goban(g1) and is_goban(g2) and g1[1][0] == g2[1][0]: 
        if sorted(g1[1][1].keys()) == sorted(g2[1][1].keys()):
            return all(equal_stones(g1[1][1][k], g2[1][1][k]) for k in g1[1][1])
    return False

def goban_to_str(board):    
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    n_v, n_h = board[1][0], board[1][0]
    res = '   ' + ''.join(f'{l} ' for l in LETTERS[:n_v]).rstrip() + '\n' 
    for i in range(n_h):
        res += '{:>2} '.format(n_h-i)
        for j in LETTERS[:n_v]:
            res += stone_to_str(get_stone(board, create_intersection(j, n_h-i))) + ' '
        res += '{:>2}'.format(n_h-i) + '\n'
    res += '   ' + ''.join(f'{l} ' for l in LETTERS[:n_v]).rstrip()
    return res
   
def get_different_adjacents(board, stone_chain):
  
    if stone_chain:
        state = get_stone(board, stone_chain[0])
        eh_diferente = (lambda x:not is_player_stone(x)) if is_player_stone(state) else is_player_stone
        
        liberties = []
        
        for pos in stone_chain:
            for new_pos in get_adjacent_intersections(pos, get_last_intersection(board)):
                if eh_diferente(get_stone(board, new_pos)) and new_pos not in liberties:
                    liberties.append(new_pos)
                    
        return sort_intersections(tuple(liberties))
    return ()

def play(board, pos, stone):
    place_stone(board, pos, stone)
    for new_pos in get_adjacent_intersections(pos, get_last_intersection(board)):
        other_stone = get_stone(board, new_pos)
        if is_player_stone(other_stone) and not equal_stones(stone, other_stone):
            chain = get_chain(board, new_pos)
            if len(get_different_adjacents(board, chain)) == 0:
                remove_chain(board, chain)
    return board
                    
def get_player_stones(board):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    num_w, num_b = 0, 0
    white, black = create_white_stone(), create_black_stone()
    
    last_pos = get_last_intersection(board)
    last_h, last_v = LETTERS.index(get_col(last_pos)), get_row(last_pos)
    
    for h in LETTERS[:last_h+1]:
        for v in range(1, last_v+1):
            pos = create_intersection(h, v)
            if equal_stones(white, get_stone(board, pos)):
                num_w+=1
            elif equal_stones(black, get_stone(board, pos)):
                num_b += 1
    return num_w, num_b

def get_territories(board):
    LETTERS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    all_chains, seen_chains = [], ()
    
    last_pos = get_last_intersection(board)
    last_h, last_v = LETTERS.index(get_col(last_pos)), get_row(last_pos)
    
    for h in LETTERS[:last_h+1]:
        for v in range(1, last_v+1):
            pos = create_intersection(h, v)
            if equal_stones(get_stone(board, pos), create_neutral_stone()) and pos not in seen_chains:
                this_chain = get_chain(board, pos)
                all_chains.append(this_chain)
                seen_chains += this_chain
          
    return tuple(sorted(all_chains, key=lambda x:(get_row(x[0]), get_col(x[0]))))
