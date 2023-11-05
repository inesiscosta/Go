
def turno_jogador(current, stone, last_board):
    def eh_cadeia_intercecao_ok(cad):
        return isinstance(cad,str) and ((len(cad) == 2 and 'A' <= cad[0] <= 'S' and cad[1] in '0123456789' and 1<= int(cad[1]) <= 9) \
            or (len(cad) == 3 and 'A' <= cad[0] <= 'S' and cad[1] == '1' \
                and cad[2] in '0123456789' and 1<= int(cad[1:]) <= 19)) 

    legal_play = False
    while not legal_play:
        pos = input(f"Write down an intersection or 'P' to pass the turn [{stone_to_str(stone)}]:")
        if pos == 'P':
            return False
        elif eh_cadeia_intercecao_ok(pos):
            pos = str_to_intersection(pos)
            legal_play = is_legal_play(current, pos, stone, last_board)
            
    play(current, pos, stone)
    return True