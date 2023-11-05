# pylint: skip-file
import pytest 
project_filename = 'Go.py'
import sys

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code that will run before your test, for example:
    exec(open(project_filename, encoding="utf-8").read(), globals())

    # A test function will be run at this point
    yield

class TestPublicIntersection:

    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            intersection1 = create_intersection('a', 12)
        assert "create_intersection: invalid arguments" == str(excinfo.value)
    
    def test_2(self):
        assert not equal_intersections(create_intersection('A', 2), create_intersection('B', 13))

    def test_3(self):
        assert equal_intersections(create_intersection('A', 2), str_to_intersection('A2'))

    def test_4(self):
        assert intersection_to_str(create_intersection('B', 13)) == 'B13'

    def test_5(self):
        intersection1 = create_intersection('A', 2)
        assert ('A1', 'B2', 'A3') == tuple(intersection_to_str(i) for i in obtain_adjacent_intersections(intersection1, create_intersection('S',19)))
        
    def test_6(self):
        tup = (create_intersection('A',1), create_intersection('A',3), create_intersection('B',1), create_intersection('B',2))
        assert ('A1', 'B1', 'B2', 'A3') == tuple(intersection_to_str(i) for i in sort_intersections(tup))
        
class TestPublicStone:

    def test_1(self):
        assert  is_stone(create_white_stone())

    def test_2(self):
        assert not equal_stones(create_white_stone(), create_black_stone())

    def test_3(self):
        white, black = create_white_stone(), create_black_stone()
        assert stone_to_str(white), stone_to_str(black) == ('O', 'X')
        
    def test_4(self):
        assert not is_player_stone(create_neutral_stone())
        
class TestPublicGoban:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            goban = create_empty_goban(10)
            assert "create_initial_goban: invalid argument" == str(excinfo.value)

    def test_2(self):
        assert is_goban(create_empty_goban(9))
        
    def test_3(self):
        goban = create_empty_goban(9)
        intersection1 = create_intersection('C',8)
        assert stone_to_str(obtain_stone(goban,intersection1)) == '.'
        
    def test_4(self):
        goban = create_empty_goban(9)
        white, black = create_white_stone(), create_black_stone()
        white_intersections1 = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        black_intersections1 = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in white_intersections1: place_stone(goban, str_to_intersection(i), white)
        for i in black_intersections1: place_stone(goban, str_to_intersection(i), black)
        hyp = \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 . . O O . . . . .  2
 1 . . O . . . . . .  1
   A B C D E F G H I"""
        assert  goban_to_str(goban) == hyp
        
    def test_5(self):
        goban = create_empty_goban(9)
        white, black = create_white_stone(), create_black_stone()
        white_intersections1 = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        black_intersections1 = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in white_intersections1: place_stone(goban, str_to_intersection(i), white)
        for i in black_intersections1: place_stone(goban, str_to_intersection(i), black)
        cad = obtain_chain(goban, create_intersection('F',5))
        assert  tuple(intersection_to_str(i) for i in cad) == ('E4', 'F4', 'E5', 'F5')

    def test_6(self):
        goban = create_empty_goban(9)
        white, black = create_white_stone(), create_black_stone()
        white_intersections1 = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        black_intersections1 = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in white_intersections1: place_stone(goban, str_to_intersection(i), white)
        for i in black_intersections1: place_stone(goban, str_to_intersection(i), black)
        chain = obtain_chain(goban, create_intersection('F',5))
        liberties = obtain_different_adjacents(goban, chain)
        assert tuple(intersection_to_str(i) for i in liberties) == ('E3', 'F3', 'G4', 'D5', 'G5', 'E6', 'F6')
        
    def test_7(self):
        goban = create_empty_goban(9)
        white, black = create_white_stone(), create_black_stone()
        white_intersections1 = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        black_intersections1 = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in white_intersections1: place_stone(goban, str_to_intersection(i), white)
        for i in black_intersections1: place_stone(goban, str_to_intersection(i), black)
        terr = obtain_territories(goban)
        assert tuple(intersection_to_str(i) for i in terr[0]) == ('A1', 'B1', 'A2', 'B2')

    def test_8(self):
        goban = create_empty_goban(9)
        b, p = create_white_stone(), create_black_stone()
        white_intersections1 = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        black_intersections1 = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in white_intersections1: place_stone(goban, str_to_intersection(i), b)
        for i in black_intersections1: place_stone(goban, str_to_intersection(i), p)
        terr = obtain_territories(goban)
        border = obtain_different_adjacents(goban, terr[0])
        assert  tuple(intersection_to_str(i) for i in border) == ('C1', 'C2', 'A3', 'B3')

    def test_9(self):
        goban = create_empty_goban(9)
        b, p = create_white_stone(), create_black_stone()
        white_intersections1 = 'C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'
        black_intersections1 = 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'
        for i in white_intersections1: place_stone(goban, str_to_intersection(i), b)
        for i in black_intersections1: place_stone(goban, str_to_intersection(i), p)
        assert obtain_num_player_stones(goban) == (8, 6)
        
    def test_10(self):
        white_intersections1 = tuple(str_to_intersection(i) \
            for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        black_intersections1 = tuple(str_to_intersection(i) \
            for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        goban = create_goban(9, white_intersections1, black_intersections1)
        assert  goban_to_str(goban) == \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 X . O O . . . . .  2
 1 X X O . . . . . .  1
   A B C D E F G H I"""
   
    def test_11(self):
        white_intersections1 = tuple(str_to_intersection(i) \
            for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        black_intersections1 = tuple(str_to_intersection(i) \
            for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        goban = create_goban(9, white_intersections1, black_intersections1)
        white = create_white_stone()
        _ = play(goban, create_intersection('B', 2), white)
        assert  goban_to_str(goban) == \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 . O O O . . . . .  2
 1 . . O . . . . . .  1
   A B C D E F G H I"""
   
   
class TestPublicCalculatepoints:
    def test_1(self):
        white_intersections1 = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        black_intersections1 = tuple(str_to_intersection(i) for i in ('E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        goban = create_goban(9, white_intersections1, black_intersections1)
        assert calculate_points(goban) == (12, 6)
        
class TestPublicIsPlayLegal:
    def test_1(self):
        white_intersections1 = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        black_intersections1 = tuple(str_to_intersection(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        goban = create_goban(9, white_intersections1, black_intersections1)
        prev_goban = create_empty_goban(9)
        white, black = create_white_stone(), create_black_stone()
        assert not is_legal_play(goban, create_intersection('B', 2), black, prev_goban)
        
    def test_2(self):
        white_intersections1 = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        black_intersections1 = tuple(str_to_intersection(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        goban = create_goban(9, white_intersections1, black_intersections1)
        prev_goban = create_empty_goban(9)
        white, black = create_white_stone(), create_black_stone()
        assert is_legal_play(goban, create_intersection('B', 2), white, prev_goban)

    def test_3(self):
        white_intersections1 = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        black_intersections1 = tuple(str_to_intersection(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        goban = create_goban(9, white_intersections1, black_intersections1)
        prev_goban = create_empty_goban(9)
        white, black = create_white_stone(), create_black_stone()
        ref = \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X . . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 X . O O . . . . .  2
 1 X X O . . . . . .  1
   A B C D E F G H I"""
        assert (not is_legal_play(goban, create_intersection('B', 2), black, prev_goban)) \
            and is_legal_play(goban, create_intersection('B', 2), white, prev_goban) \
                and ref ==  goban_to_str(goban)

    def test_4(self):
        white_intersections1 = tuple(str_to_intersection(i) for i in ('A2','B1','B3','C2'))
        black_intersections1 = tuple(str_to_intersection(i) for i in ('C1','C3','D1','D2'))
        white, black = create_white_stone(), create_black_stone()
        goban = create_goban(9, white_intersections1, black_intersections1)
        g_ko = create_copy_goban(goban)
        assert is_legal_play(goban, create_intersection('B', 2), black, g_ko)

    def test_5(self):
        white_intersections1 = tuple(str_to_intersection(i) for i in ('A2','B1','B3','C2'))
        black_intersections1 = tuple(str_to_intersection(i) for i in ('C1','C3','D1','D2'))
        white, black = create_white_stone(), create_black_stone()
        goban = create_goban(9, white_intersections1, black_intersections1)
        g_ko = create_copy_goban(goban)
        play(goban, create_intersection('B', 2), black)   
        assert not is_legal_play(goban, create_intersection('B', 2), white, g_ko)
   
class TestPublicPlayerTurn:
    def test_1(self):
        white_intersections1 = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        black_intersections1 = tuple(str_to_intersection(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        goban = create_goban(9, white_intersections1, black_intersections1)
        ref = (True, "Write down an intersection or 'P' to pass the turn [X]:Write down an intersection or 'P' to pass the turn [X]:Write down an intersection or 'P' to pass the turn [X]:")
        assert offlime_player_turn(goban, create_black_stone(), create_empty_goban(9), 'B10\nB2\nG5\n') == ref

    def test_2(self):
        white_intersections1 = tuple(str_to_intersection(i) for i in ('C1', 'C2', 'C3', 'D2', 'D3', 'D4', 'A3', 'B3'))
        black_intersections1 = tuple(str_to_intersection(i) for i in ('A1', 'A2', 'B1', 'E4', 'E5', 'F4', 'F5', 'G6', 'G7'))
        goban = create_goban(9, white_intersections1, black_intersections1)
        offlime_player_turn(goban, create_black_stone(), create_empty_goban(9), 'B10\nB2\nG5\n')
        ref = \
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . X . .  7
 6 . . . . . . X . .  6
 5 . . . . X X X . .  5
 4 . . . O X X . . .  4
 3 O O O O . . . . .  3
 2 X . O O . . . . .  2
 1 X X O . . . . . .  1
   A B C D E F G H I"""
        assert  goban_to_str(goban) == ref
   
class TestGo:
    def test_1(self):
        input_str = 'A1\nB1\nB2\nA2\nA1\nA3\nA1\nC1\nE5\nP\nP\n'
        ref = \
"""White (O) has 0 points
Black (X) has 0 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [X]:White (O) has 0 points
Black (X) has 81 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 X . . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [O]:White (O) has 1 points
Black (X) has 1 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 X O . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [X]:White (O) has 1 points
Black (X) has 2 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . X . . . . . . .  2
 1 X O . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [O]:White (O) has 3 points
Black (X) has 1 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 O X . . . . . . .  2
 1 . O . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [X]:Write down an intersection or 'P' to pass the turn [X]:White (O) has 3 points
Black (X) has 2 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 O X . . . . . . .  2
 1 . O . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [O]:White (O) has 3 points
Black (X) has 2 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 O X . . . . . . .  2
 1 O O . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [X]:White (O) has 0 points
Black (X) has 81 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [O]:White (O) has 1 points
Black (X) has 6 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [X]:White (O) has 1 points
Black (X) has 6 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [O]:White (O) has 1 points
Black (X) has 6 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . O . . . .  5
 4 . . . . . . . . .  4
 3 X . . . . . . . .  3
 2 . X . . . . . . .  2
 1 . . X . . . . . .  1
   A B C D E F G H I
"""
        assert offline_go(9, (), (), input_str) == (False, ref)
        
    def test_2(self):
        ref = \
"""White (O) has 62 points
Black (X) has 17 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O . . O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [X]:White (O) has 60 points
Black (X) has 18 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O X . O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [O]:White (O) has 62 points
Black (X) has 17 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X O O O O X O  6
 5 . O X O . O O X O  5
 4 . O X O O O X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [X]:White (O) has 51 points
Black (X) has 28 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [O]:White (O) has 51 points
Black (X) has 28 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
Write down an intersection or 'P' to pass the turn [X]:White (O) has 51 points
Black (X) has 28 points
   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . O O O O O O O  8
 7 . . O X X X X X O  7
 6 . O X . . . . X O  6
 5 . O X . X . . X O  5
 4 . O X . . . X X .  4
 3 . O X X X X X . O  3
 2 . . O O O O O O .  2
 1 . . . . . . . . .  1
   A B C D E F G H I
"""

        white_intersections1 = 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'B3', 'I3', 'B4', 'D4', 'E4', 'F4', 'B5', 'D5', 'G5', 'I5', 'B6', 'D6', 'E6', 'F6', 'G6', 'I6', 'C7', 'I7', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'
        black_intersections1 = 'C3', 'D3', 'E3', 'F3', 'G3', 'C4', 'G4', 'H4', 'C5', 'H5', 'C6', 'H6', 'D7', 'E7', 'F7', 'G7', 'H7'

        assert offline_go(9, white_intersections1, black_intersections1, 'E5\nF5\nE5\nP\nP\n') == (True, ref)
        

# Auxiliary Code Necessary to Replace Standard Input 
class ReplaceStdIn:
    def __init__(self, input_handle):
        self.input = input_handle.split('\n')
        self.line = 0

    def readline(self):
        if len(self.input) == self.line:
            return ''
        result = self.input[self.line]
        self.line += 1
        return result

class ReplaceStdOut:
    def __init__(self):
        self.output = ''

    def write(self, s):
        self.output += s
        return len(s)

    def flush(self):
        return 


def offlime_player_turn(board, pedra, last, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = player_turn(board, pedra, last)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

def offline_go(n, white_intersections, black_intersections, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = go(n, white_intersections, black_intersections)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout


white_intersections_ = 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 'B3', 'J3', 'B4', 'D4', 'E4', 'F4', 'B5', 'D5', 'G5', 'J5', 'B6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'C7', 'J7', 'C8', 'D8', 'E8', 'F9', 'G9', 'H9', 'I9'
black_intersections_ = 'C3', 'D3', 'E3', 'F3', 'G3', 'C4', 'G4', 'H4', 'C5', 'H5', 'C6', 'H6', 'D7', 'E7', 'F7', 'G7', 'H7', 'I7'
