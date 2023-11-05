def calcula_pontos(board):
    white_points, black_points = obtain_player_stones(board)
    
    for territorio in obtain_territories(board):
        limites = obtain_different_adjacents(board, territorio)
        if limites:
            if all(is_white_stone(obtem_pedra(board,i)) for i in limites):
                white_points += len(territorio)
            elif all(is_black_stone(obtem_pedra(board,i)) for i in limites):
                black_points += len(territorio)
    return white_points, black_points