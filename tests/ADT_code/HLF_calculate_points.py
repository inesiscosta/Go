def calculate_points(board):
    white_points, black_points = get_player_stones(board)
    
    for territory in get_territories(board):
        limits = get_different_adjacents(board, territory)
        if limits:
            if all(is_white_stone(get_stone(board,i)) for i in limits):
                white_points += len(territory)
            elif all(is_black_stone(get_stone(board,i)) for i in limits):
                black_points += len(territory)
    return white_points, black_points