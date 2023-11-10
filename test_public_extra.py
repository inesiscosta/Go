# pylint: skip-file
import pytest
from Go import *
import sys

class TestExtraCreateIntersection:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            create_intersection(1,1)
        assert str(excinfo.value) == "create_intersection: invalid arguments"
        
    def test_2(self):
        with pytest.raises(ValueError) as excinfo:
            create_intersection("AA",1)
        assert str(excinfo.value) == "create_intersection: invalid arguments"

    def test_3(self):
        with pytest.raises(ValueError) as excinfo:
            create_intersection("a",1)
        assert str(excinfo.value) == "create_intersection: invalid arguments"

    def test_4(self):
        with pytest.raises(ValueError) as excinfo:
            create_intersection("A","a")
        assert str(excinfo.value) == "create_intersection: invalid arguments"

    def test_5(self):
        with pytest.raises(ValueError) as excinfo:
            create_intersection((),())
        assert str(excinfo.value) == "create_intersection: invalid arguments"

    def test_6(self):
        with pytest.raises(ValueError) as excinfo:
            create_intersection(None,None)
        assert str(excinfo.value) == "create_intersection: invalid arguments"
    
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            create_intersection("A",True)
        assert str(excinfo.value) == "create_intersection: invalid arguments"
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            create_intersection("A",float(1))
        assert str(excinfo.value) == "create_intersection: invalid arguments"
    
    def test_9(self):
        intersecao = create_intersection("A",1)
        hashable = {intersecao:1}
        assert hashable[intersecao] == 1

class TestExtraObtainColRow:
    def test_1(self):
        intersection1 = create_intersection("A",1)
        assert obtain_col(intersection1) == "A"

    def test_2(self):
        intersection1 = create_intersection("A",1)
        assert obtain_row(intersection1) == 1

    def test_3(self):
        intersection1 = create_intersection("S",19)
        assert obtain_col(intersection1) == "S"

    def test_4(self):
        intersection1 = create_intersection("S",19)
        assert obtain_row(intersection1) == 19

class TestExtraIsIntersection:
    
    def test_1(self):
        intersection1 = 1
        assert not is_intersection(1)
    
    def test_2(self):
        intersection1 = "A1"
        assert not is_intersection(1)
    
    def test_3(self):
        intersection1 = ["A",2,3]
        assert not is_intersection(1)
        
    def test_4(self):
        intersection1 = [1,1]
        assert not is_intersection(1)
    
    def test_5(self):
        intersection1 = ["A","A"]
        assert not is_intersection(1)
    
    def test_6(self):
        intersection1 = ["AA",1]
        assert not is_intersection(1)

    def test_7(self):
        intersection1 = ["a",1]
        assert not is_intersection(1)

    def test_8(self):
        intersection1 = ["A",0]
        assert not is_intersection(1)
    
    def test_9(self):
        intersection1 = create_intersection("A",1)
        assert is_intersection(intersection1)

class TestExtraEqualIntersections:
    def test_1(self):
        intersection1 = create_intersection("A",1)
        intersection2 = create_intersection("A",1)
        assert equal_intersections(intersection1,intersection2)
    
    def test_2(self):
        intersection1 = create_intersection("A",1)
        intersection2 = create_intersection("B",1)
        assert not equal_intersections(intersection1,intersection2)

    def test_3(self):
        intersection1 = create_intersection("A",1)
        intersection2 = create_intersection("A",2)
        assert not equal_intersections(intersection1,intersection2)
    
    def test_4(self):
        intersection1 = create_intersection("A",1)
        intersection2 = create_intersection("B",2)
        assert not equal_intersections(intersection1,intersection2)

class TestExtraIntersectionToStr:
    def test_1(self):
        intersection1 = create_intersection("A",1)
        assert intersection_to_str(intersection1) == "A1"

    def test_2(self):
        intersection1 = create_intersection("S",19)
        assert intersection_to_str(intersection1) == "S19"
    
class TestExtraStrToIntersection:
    def test_1(self):
        intersection1 = "A1"
        assert str_to_intersection(intersection1) == create_intersection("A",1)
    
    def test_2(self):
        intersection1 = "S19"
        assert str_to_intersection(intersection1) == create_intersection("S",19)

class TestExtraAdjacentIntersections:
    def test_1(self):
        intersection1 = create_intersection("A",1)
        intersection2 = create_intersection("S",19)
        answer = ["B1","A2"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)

    def test_2(self): 
        intersection1 = create_intersection("S",1)
        intersection2 = create_intersection("S",19)
        answer = ["R1","S2"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)

    def test_3(self): 
        intersection1 = create_intersection("A",19)
        intersection2 = create_intersection("S",19)
        answer = ["A18","B19"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)
    
    def test_4(self):
        intersection1 = create_intersection("S",19)
        intersection2 = create_intersection("S",19)
        answer = ["S18","R19"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)
    
    def test_5(self):
        intersection1 = create_intersection("A",2)
        intersection2 = create_intersection("S",19)
        answer = ["A1","B2","A3"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)

    def test_6(self):
        intersection1 = create_intersection("S",2)
        intersection2 = create_intersection("S",19)
        answer = ["S1", "R2", "S3"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)

    def test_7(self):
        intersection1 = create_intersection("R",19)
        intersection2 = create_intersection("S",19)
        answer = ["R18","Q19","S19"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)
    
    def test_8(self): 
        intersection1 = create_intersection("R",1)
        intersection2 = create_intersection("S",19)
        answer = ["Q1","S1","R2"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)

    def test_9(self):
        intersection1 = create_intersection("B",2)
        intersection2 = create_intersection("S",19)
        answer = ["B1","A2","C2","B3"]
        assert obtain_adjacent_intersections(intersection1,intersection2) == tuple(str_to_intersection(x) for x in answer)
        
class TestExtraSortIntersections:
    def test_1(self): 
        intersection1 = ("A18","A10","A1","A2","A3","A4","A5","A6","A7","A8","A9")
        intersection1 = tuple(str_to_intersection(x) for x in intersection1)
        answer = ("A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A18")
        assert sort_intersections(intersection1) == tuple(str_to_intersection(x) for x in answer)

    def test_2(self): 
        intersection1 = ("G1","A1","K1","B1","C1","E1","F1","H1","D1","I1","J1")
        intersection1 = tuple(str_to_intersection(x) for x in intersection1)
        answer = ("A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1")
        assert sort_intersections(intersection1) == tuple(str_to_intersection(x) for x in answer)

    def test_3(self): 
        intersection1 = ("G1","A1","K1","B1","C1","E1","F1","H1","D1","I1","J1","A18","A10","A1","A2","A3","A4","A5","A6","A7","A8","A9")
        intersection1 = tuple(str_to_intersection(x) for x in intersection1)
        answer = ("A1","A1","B1","C1","D1","E1","F1","G1","H1","I1","J1","K1","A2","A3", "A4","A5","A6","A7","A8","A9","A10","A18")
        assert sort_intersections(intersection1) == tuple(str_to_intersection(x) for x in answer)

class TestExtraIsStone:
    def test_1(self):
        assert is_stone(create_white_stone())
    
    def test_2(self):
        assert is_stone(create_neutral_stone())
    
    def test_3(self):
        assert is_stone(create_black_stone())
        
    def test_4(self):
        assert is_black_stone((create_black_stone()))
        
    def test_5(self):
        assert is_white_stone((create_white_stone()))
        
    def test_6(self):
        assert not is_player_stone((create_neutral_stone()))
        
    def test_7(self):
        assert is_player_stone((create_black_stone()))
        
    def test_8(self):
        assert is_player_stone((create_white_stone()))

class TestMarcosstoneParaStr:
    def test_1(self):
        assert stone_to_str(create_white_stone()) == "O"
    
    def test_2(self):
        assert stone_to_str(create_black_stone()) == "X"
    
    def test_3(self):
        assert stone_to_str(create_neutral_stone()) == "."

class TestMarcosstonesIguais:
    def test_1(self):
        assert equal_stones(create_white_stone(),create_white_stone())
    
    def test_2(self):
        assert equal_stones(create_black_stone(),create_black_stone())
    
    def test_3(self):
        assert equal_stones(create_neutral_stone(),create_neutral_stone())
    
    def test_4(self):
        assert not equal_stones(create_white_stone(),create_black_stone())
    
    def test_5(self):
        assert not equal_stones(create_white_stone(),create_neutral_stone())
    
    def test_6(self):
        assert not equal_stones(create_black_stone(),create_neutral_stone())
    
class TestExtraCreateGoban:
    def test_1(self):
        black_intersections = 'A'
        white_intersections = ()
        with pytest.raises(ValueError) as excinfo:
            create_goban(9,white_intersections,black_intersections)
        assert str(excinfo.value) == "create_goban: invalid arguments"

    def test_2(self):
        black_intersections = ()
        white_intersections = "A"
        with pytest.raises(ValueError) as excinfo:
            create_goban(9,white_intersections,black_intersections)
        assert str(excinfo.value) == "create_goban: invalid arguments" 

    def test_3(self):
        black_intersections = ()
        white_intersections = ()
        with pytest.raises(ValueError) as excinfo:
            create_goban(10,white_intersections,black_intersections)
        assert str(excinfo.value) == "create_goban: invalid argument"
        
    def test_4(self):
        white_intersections = ("A2",)
        black_intersections = ("A2",)
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        with pytest.raises(ValueError) as excinfo:
            create_goban(9,white_intersections,black_intersections)
        assert str(excinfo.value) == "create_goban: invalid arguments"
        
    def test_5(self):
        white_intersections = ("A3",)
        black_intersections = ("A2", "A2")
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        with pytest.raises(ValueError) as excinfo:
            create_goban(9,white_intersections,black_intersections)
        assert str(excinfo.value) == "create_goban: invalid arguments"
    
    def test_6(self):
        white_intersections = ("A2", "A2")
        black_intersections = ("A3",)
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        with pytest.raises(ValueError) as excinfo:
            create_goban(9,white_intersections,black_intersections)
        assert str(excinfo.value) == "create_goban: invalid arguments"
    
    def test_7(self):
        with pytest.raises(ValueError) as excinfo:
            create_empty_goban(None)
        assert str(excinfo.value) == "create_empty_goban: invalid arguments"
    
    def test_8(self):
        with pytest.raises(ValueError) as excinfo:
            create_empty_goban("A")
        assert str(excinfo.value) == "create_empty_goban: invalid arguments"
    
    def test_9(self):
        with pytest.raises(ValueError) as excinfo:
            create_empty_goban(3)
        assert str(excinfo.value) == "create_empty_goban: invalid arguments"

    def test_10(self):
        white_intersections = ("A13",)
        black_intersections = tuple()
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        with pytest.raises(ValueError) as excinfo:
            create_goban(9,white_intersections,black_intersections)
        assert str(excinfo.value) == "create_goban: invalid arguments"
    
    def test_11(self):
        white_intersections = ("A2",)
        black_intersections = ("A13",)
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        with pytest.raises(ValueError) as excinfo:
            create_goban(9,white_intersections,black_intersections)
        assert str(excinfo.value) == "create_goban: invalid arguments"
    
class TestExtraObtainStone:
    def test_1(self):
        white_intersections = ("A2",)
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        goban = create_goban(9,white_intersections,())
        assert is_white_stone(obtain_stone(goban,create_intersection("A",2)))

    def test_2(self):
        black_intersections = ("B9",)
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        goban = create_goban(9,(),black_intersections)
        assert is_black_stone(obtain_stone(goban,create_intersection("B",9)))
    
    def test_3(self):
        white_intersections = ("A2",)
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        goban = create_goban(9,white_intersections,())
        assert not is_player_stone(obtain_stone(goban,create_intersection("A",1)))

class TestExtraObtainChain:
    def test_1(self):
        white_intersections = ("A2","A3","A4")
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        goban = create_goban(9,white_intersections,())
        assert obtain_chain(goban,create_intersection("A",4)) == white_intersections

    def test_2(self):
        black_intersections = ("A2","A3","A4")
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        goban = create_goban(9,(),black_intersections)
        assert obtain_chain(goban,create_intersection("A",2)) == black_intersections 

    def test_3(self):
        black_intersections = ("A1","A2","A3","B3","B4","C4","D4","D3","D2","C2","C1","B1") 
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        goban = create_goban(9,(),black_intersections)
        answer = ("A1","B1","C1","A2","C2","D2","A3","B3","D3","B4","C4","D4")
        answer = tuple(str_to_intersection(x) for x in answer)
        assert obtain_chain(goban,create_intersection("C",4)) == answer
        
class TestExtraPlaceStone:
    def test_1(self):
        goban = create_empty_goban(9)
        place_stone(goban,create_intersection("A",1),create_white_stone())
        assert is_white_stone(obtain_stone(goban,create_intersection("A",1)))

    def test_2(self):
        goban = create_empty_goban(9)
        place_stone(goban,create_intersection("A",1),create_black_stone())
        assert is_black_stone(obtain_stone(goban,create_intersection("A",1)))

    def test_3(self):
        goban = create_empty_goban(9)
        place_stone(goban,create_intersection("A",1),create_black_stone())
        assert not is_player_stone(obtain_stone(goban,create_intersection("A",2)))

    def test_4(self):
        goban = create_empty_goban(9)
        place_stone(goban,create_intersection("A",1),create_white_stone())
        place_stone(goban,create_intersection("A",1),create_black_stone())
        assert is_black_stone(obtain_stone(goban,create_intersection("A",1)))

    def test_5(self):
        goban = create_empty_goban(9)
        place_stone(goban,create_intersection("A",1),create_white_stone())
        remove_stone(goban,create_intersection("A",1))
        assert not is_player_stone(obtain_stone(goban,create_intersection("A",1)))

    def test_6(self):
        white_intersections = ("A1","A2","A3","B3","B4","C4","D4","D3","D2","C2","C1","B1")
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        goban = create_goban(9,white_intersections,())
        remove_chain(goban,white_intersections)
        answer = ()
        for i in white_intersections:
            answer += (obtain_stone(goban,i) if is_player_stone(obtain_stone(goban,i))else ())
        assert answer == ()

class TestExtraIsGoban:
    def test_1(self):
        assert is_goban(create_empty_goban(9))

    def test_2(self):
        assert is_goban(create_empty_goban(13))

    def test_3(self):
        assert is_goban(create_empty_goban(19))

    def test_4(self):
        white_intersections = ("A1","A2","A3","B3","B4","C4","D4","D3","D2","C2","C1","B1")
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        goban = create_goban(9,white_intersections,())
        assert is_goban(goban)

    def test_5(self):
        goban = [["" for _ in range(9)] for _ in range(9)]
        assert not is_goban(goban)
    
class TestExtraObtainLastIntersection:
    def test_1(self):
        goban = create_empty_goban(9)
        assert obtain_last_intersection(goban) == create_intersection("I",9)
    def test_1(self):
        goban = create_empty_goban(13)
        assert obtain_last_intersection(goban) == create_intersection("M",13)
    def test_1(self):
        goban = create_empty_goban(19)
        assert obtain_last_intersection(goban) == create_intersection("S",19)

class TestExtraCopyGobanEqualGobans:
    def test_1(self):
        goban = create_empty_goban(9)
        assert equal_gobans(goban,create_copy_goban(goban))

    def test_2(self):
        goban = create_empty_goban(9)
        goban1 = create_copy_goban(goban)
        place_stone(goban,create_intersection("A",1),create_white_stone())
        assert not equal_gobans(goban,goban1)
    
    def test_3(self):
        goban = create_empty_goban(9)
        goban1 = create_copy_goban(goban)
        place_stone(goban,create_intersection("A",1),create_white_stone())
        remove_stone(goban,create_intersection("A",1))
        assert equal_gobans(goban,goban1)

class TestExtraGobanToStr:
    def test_1(self):
        goban = create_empty_goban(9)
        assert goban_to_str(goban) == REF_TEST_GOBAN["1"]
    
    def test_2(self):
        white_intersections = "C1,G1,C2,G2,C3,G3,A4,B4,C4,G4,H4,I4,A6,B6,C6,D6,E6,E7,F7,G7,H7,I7".split(",")
        black_intersections = "D1,F1,D2,E2,F2,D3,E3,F3,F4,D4,E4,A5,B5,C5,D5,F5,G5,H5,I5,I6,H6,G6,F6".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        black_intersections = tuple(str_to_intersection(i) for i in black_intersections)
        goban = create_goban(13,white_intersections,black_intersections)
        assert goban_to_str(goban) == REF_TEST_GOBAN["2"]

class TestExtraObtainTerritories:
    def test_1(self):
        white_intersections = ("B1","A2","B2","A4","B4","C4","D4","D3","D2","D1","F1","F2","F3","F4","F5","F6","E6","D6","C6","B6","A6","A8","B8","C8","D8","E8","F8","G8","H8","H7","H6","H5","H4","H3","H2","H1","I9","G7","E5","C3")
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        goban = create_goban(9,white_intersections,())
        answer = (('A1',), ('C1', 'C2'), ('E1', 'E2', 'E3', 'E4'), ('G1', 'G2', 'G3', 'G4', 'G5', 'G6'), ('I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8'), ('A3', 'B3'), ('A5', 'B5', 'C5', 'D5'), ('A7', 'B7', 'C7', 'D7', 'E7', 'F7'), ('A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9'))
        answer = tuple(tuple(str_to_intersection(j) for j in i) for i in answer)
        assert obtain_territories(goban) == answer
    
    def test_2(self):
        black_intersections = ("B1","A2","B2","A4","B4","C4","D4","D3","D2","D1","F1")
        white_intersections = ("F2","F3","F4","F5","F6","E6","D6","C6","B6","A6","A8","B8","C8","D8","E8","F8","G8","H8","H7","H6","H5","H4","H3","H2","H1","I9","G7","E5","C3")
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        answer = (('A1',), ('C1', 'C2'), ('E1', 'E2', 'E3', 'E4'), ('G1', 'G2', 'G3', 'G4', 'G5', 'G6'), ('I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8'), ('A3', 'B3'), ('A5', 'B5', 'C5', 'D5'), ('A7', 'B7', 'C7', 'D7', 'E7', 'F7'), ('A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9'))
        answer = tuple(tuple(str_to_intersection(j) for j in i) for i in answer)
        assert obtain_territories(goban) == answer

class TestExtraObtainDifferentAdjacents:
    def test_1(self):
        white_intersections = ("B1","A2","B2","A4","B4","C4","D4","D3","D2","D1","F1","F2","F3","F4","F5","F6","E6","D6","C6","B6","A6","A8","B8","C8","D8","E8","F8","G8","H8","H7","H6","H5","H4","H3","H2","H1","I9","G7","E5","C3")
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        goban = create_goban(9,white_intersections,())
        cadeia = obtain_chain(goban,create_intersection("F",1))
        answer = ('E1', 'G1', 'E2', 'G2', 'E3', 'G3', 'E4', 'G4', 'A5', 'B5', 'C5', 'D5', 'G5', 'G6', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7')
        answer = tuple(str_to_intersection(x) for x in answer)
        assert obtain_different_adjacents(goban,cadeia) == answer
    
class TestExtraPlay:
    def test_1(self):
        white_intersections = "E2,E3,E4,E5".split(",")
        white_intersections = tuple(str_to_intersection(x) for x in white_intersections)
        black_intersections = "F1,F2,F3,F4,F5,E6,D5,D4,D3,D2,D1".split(",")
        black_intersections = tuple(str_to_intersection(x) for x in black_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        p = create_black_stone()
        _ = play(goban,create_intersection("E",1),p)
        assert goban_to_str(goban) == REF_TEST_PLAY["1"]

    def test_2(self):
        white_intersections = "C1,G1,C2,G2,C3,G3,A4,B4,C4,G4,H4,I4,A6,B6,C6,D6,E6,E7,F7,G7,H7,I7".split(",")
        black_intersections = "D1,E1,F1,D2,E2,F2,D3,E3,F3,F4,D4,E4,A5,B5,C5,D5,F5,G5,H5,I5,I6,H6,G6,F6".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        black_intersections = tuple(str_to_intersection(i) for i in black_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        _ = play(goban,create_intersection('E',5),create_white_stone())
        assert goban_to_str(goban) == REF_TEST_PLAY["2"]
    
    def test_3(self): 
        white_intersections = "C1,G1,C2,G2,C3,G3,A4,B4,C4,G4,H4,I4,A6,B6,C6,D6,E6,E7,F7,G7,H7,I7".split(",")
        black_intersections = "D1,F1,D2,E2,F2,D3,E3,F3,F4,D4,E4,A5,B5,C5,D5,F5,G5,H5,I5,I6,H6,G6,F6".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        black_intersections = tuple(str_to_intersection(i) for i in black_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        _ = play(goban,create_intersection('E',5),create_white_stone())
        assert goban_to_str(goban) == REF_TEST_PLAY["3"]

class TestExtraCalculatePoints:
    def test_1(self):
        goban = create_empty_goban(9)
        assert calculate_points(goban) == (0,0)

    def test_2(self):
        white_intersections = "A1,I9".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        goban = create_goban(9,white_intersections,())
        assert calculate_points(goban) == (81,0)
    
    def test_3(self):
        white_intersections = "A1,I9".split(",")
        black_intersections = "A2,I8".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        black_intersections = tuple(str_to_intersection(i) for i in black_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        assert calculate_points(goban) == (2,2)

    def test_4(self):
        white_intersections = "C1,G1,C2,G2,C3,G3,A4,B4,C4,G4,H4,I4,A6,B6,C6,D6,E6,E7,F7,G7,H7,I7".split(",")
        black_intersections = "D1,F1,D2,E2,F2,D3,E3,F3,F4,D4,E4,A5,B5,C5,D5,F5,G5,H5,I5,I6,H6,G6,F6".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        black_intersections = tuple(str_to_intersection(i) for i in black_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        _ = play(goban,create_intersection('E',5),create_white_stone())
        answer = (57, 24)
        assert calculate_points(goban) == answer

class TestExtraIsLegalPlay:
    def test_1(self):
        goban = create_empty_goban(9)
        l = create_copy_goban(goban)
        assert not is_legal_play(goban,create_intersection("K",1),create_white_stone(),l)
    
    def test_2(self): 
        goban = create_empty_goban(9)
        place_stone(goban,create_intersection("A",1),create_white_stone())
        l = create_copy_goban(goban)
        assert not is_legal_play(goban,create_intersection("A",1),create_white_stone(),l)
    
    def test_3(self):
        goban = create_empty_goban(9)
        copy = create_copy_goban(goban)
        place_stone(copy,create_intersection("A",1),create_white_stone())
        assert not is_legal_play(goban,create_intersection("A",1),create_white_stone(),copy)

    def test_4(self):
        white_intersections = "A2,B1,B2".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        goban = create_goban(9,white_intersections,())
        l = create_copy_goban(goban)
        assert not is_legal_play(goban,create_intersection("A",1),create_black_stone(),l)

    def test_5(self):
        white_intersections = "A2,B1,B2".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        goban = create_goban(9,white_intersections,())
        l = create_copy_goban(goban)
        assert is_legal_play(goban,create_intersection("A",1),create_white_stone(),l)
    
    def test_6(self):
        white_intersections = "A3,B3,C3,C2,C1".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        black_intersections = "A2,B2,B1".split(",")
        black_intersections = tuple(str_to_intersection(i) for i in black_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        l = create_copy_goban(goban)
        assert is_legal_play(goban,create_intersection("A",1),create_white_stone(),l)

class TestExtraPlayerTurn:
    def test_1(self):
        white_intersections = "A2,B1,B2".split(",")
        black_intersections = "A3,B3,C3,C2,C1".split(",")
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        black_intersections = tuple(str_to_intersection(i) for i in black_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        l = create_copy_goban(goban)
        offline_turn_player(goban,create_white_stone(),l,"A1\nA2\nB2\nA3\nA4\n")
        assert goban_to_str(goban) == REF_TEST_TURN["1"]

    def test_2(self):
        white_intersections = tuple("E5,E3,D4,F4".split(","))
        black_intersections = tuple("D3,F3,E2".split(","))
        white_intersections = tuple(str_to_intersection(i) for i in white_intersections)
        black_intersections = tuple(str_to_intersection(i) for i in black_intersections)
        goban = create_goban(9,white_intersections,black_intersections)
        l = create_copy_goban(goban)
        play(goban,create_intersection("E",4),create_black_stone())
        offline_turn_player(goban,create_white_stone(),l,"E3\nE6")
        assert goban_to_str(goban) == REF_TEST_TURN["2"]

class TestExtraGo:
    def test_1(self):
        input_str = 'A1\nB1\nB2\nA2\nA1\nA3\nA1\nC1\nE5\nP\nP\n'
        assert offline_go(9, (), (), input_str) == (False, REF_TEST_GO["1"])
        
    def test_2(self):
        white_intersections = 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'B3', 'I3', 'B4', 'D4', 'E4', 'F4', 'B5', 'D5', 'G5', 'I5', 'B6', 'D6', 'E6', 'F6', 'G6', 'I6', 'C7', 'I7', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'I8'
        black_intersections = 'C3', 'D3', 'E3', 'F3', 'G3', 'C4', 'G4', 'H4', 'C5', 'H5', 'C6', 'H6', 'D7', 'E7', 'F7', 'G7', 'H7'
        assert offline_go(9, white_intersections, black_intersections, 'E5\nF5\nE5\nP\nP\n') == (True, REF_TEST_GO["2"])

def offline_turn_player(board, stone, last, game_input):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(handle_input=game_input)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = player_turn(board, stone, last)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout


def offline_go(n, white_intersections, black_intersections, game_input):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(handle_input=game_input)
    
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

class ReplaceStdIn:
    def __init__(self, handle_input):
        self.input = handle_input.split('\n')
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

REF_TEST_GOBAN = {"1":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 . . . . . . . . .  4
 3 . . . . . . . . .  3
 2 . . . . . . . . .  2
 1 . . . . . . . . .  1
   A B C D E F G H I""","2":
"""   A B C D E F G H I J K L M
13 . . . . . . . . . . . . . 13
12 . . . . . . . . . . . . . 12
11 . . . . . . . . . . . . . 11
10 . . . . . . . . . . . . . 10
 9 . . . . . . . . . . . . .  9
 8 . . . . . . . . . . . . .  8
 7 . . . . O O O O O . . . .  7
 6 O O O O O X X X X . . . .  6
 5 X X X X . X X X X . . . .  5
 4 O O O X X X O O O . . . .  4
 3 . . O X X X O . . . . . .  3
 2 . . O X X X O . . . . . .  2
 1 . . O X . X O . . . . . .  1
   A B C D E F G H I J K L M"""}

REF_TEST_PLAY = {"1":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . X . . . .  6
 5 . . . X . X . . .  5
 4 . . . X . X . . .  4
 3 . . . X . X . . .  3
 2 . . . X . X . . .  2
 1 . . . X X X . . .  1
   A B C D E F G H I"""
,"2":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . O O O O O  7
 6 O O O O O . . . .  6
 5 . . . . O . . . .  5
 4 O O O . . . O O O  4
 3 . . O . . . O . .  3
 2 . . O . . . O . .  2
 1 . . O . . . O . .  1
   A B C D E F G H I"""
,"3":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . O O O O O  7
 6 O O O O O X X X X  6
 5 X X X X O X X X X  5
 4 O O O X X X O O O  4
 3 . . O X X X O . .  3
 2 . . O X X X O . .  2
 1 . . O X . X O . .  1
   A B C D E F G H I"""}

REF_TEST_TURN = {"1":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . . . . . .  6
 5 . . . . . . . . .  5
 4 O . . . . . . . .  4
 3 X X X . . . . . .  3
 2 O O X . . . . . .  2
 1 . O X . . . . . .  1
   A B C D E F G H I""","2":
"""   A B C D E F G H I
 9 . . . . . . . . .  9
 8 . . . . . . . . .  8
 7 . . . . . . . . .  7
 6 . . . . O . . . .  6
 5 . . . . O . . . .  5
 4 . . . O X O . . .  4
 3 . . . X . X . . .  3
 2 . . . . X . . . .  2
 1 . . . . . . . . .  1
   A B C D E F G H I"""}

REF_TEST_GO = {"1":
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
,"2":
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
}
