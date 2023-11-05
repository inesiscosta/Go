def calculate_points(board):
    white_points, black_points = obtain_player_stones(board)
    
    for territory in obtain_territories(board):
        limits = obtain_different_adjacents(board, territory)
        if limits:
            if all(is_white_stone(obtain_stone(board,i)) for i in limits):
                white_points += len(territory)
            elif all(is_black_stone(obtain_stone(board,i)) for i in limits):
                black_points += len(territory)
    return white_points, black_points