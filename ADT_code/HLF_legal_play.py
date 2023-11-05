def is_legal_play(board, pos, stone, last_board):
    if is_valid_intersection(board, pos) and \
        not is_player_stone(obtain_stone(board, pos)):
            new_board = create_copy_goban(board)
            play(new_board, pos, stone)
            if len(obtain_different_adjacents(new_board, obtain_chain(new_board, pos))) == 0:
                return False
            elif equal_gobans(new_board, last_board):
                return False
            else:
                return True
    return False
