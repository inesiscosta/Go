def is_legal_play(board, pos, pedra, last_board):
    if is_valid_intersection(board, pos) and \
        not is_player_stone(obtain_stone(board, pos)):
            novo_board = create_copy_goban(board)
            play(novo_board, pos, pedra)
            if len(obtain_different_adjacents(novo_board, obtain_chain(novo_board, pos))) == 0:
                return False
            elif equal_gobans(novo_board, last_board):
                return False
            else:
                return True
    return False
