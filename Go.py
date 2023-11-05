"""2nd Project for Foundations of Programming 2023/2024

A Python program that allows you to play the game Go.

This project focuses on the use of Abstract Data Types (ADTs).
"""

# Intersection ADT
# Constructor
def create_intersection(column:str,row:int) -> 'tuple[str,int]':
    """
    Creates an intersection from a column and a row.

    :param column: Column letter (A to S).
    :type column: str
    :param row: Row number (1 to 19).
    :type row: int

    :return: The intersection formed from the given row and column.
    :rtype: tuple[str,int]
    """
    # Argument Validation
    if not isinstance(column,str) or not isinstance(row,int)\
        or isinstance(row, bool) or len(column) != 1 \
        or not ord("A")<=ord(column)<=ord("S") or not 1<=row<=19:
        raise ValueError("create_intersection: invalid arguments")

    return (column,row)

# Selectors
def obtain_col(intersection: 'tuple[str,int]') -> str:
    """
    Obtains the intersection's column.

    :param intersection: An intersection.
    :type intersection: tuple(str,int)

    :return: The letter representing the column.
    :rtype: str
    """
    return intersection[0]

def obtain_row(intersection: 'tuple[str,int]') -> int:
    """
    Obtains the intersection's row.

    :param intersection: Any valid intersection.
    :type intersection: tuple(str,int)

    :return: The row number.
    :rtype: int
    """
    return intersection[1]

# Recognizers
def is_intersection(arg: any) -> bool:
    """
    Verifies if the argument is a valid intersection.

    :param arg: Any type of argument
    :type arg: any

    :return: True if the argument is a valid interesction. False otherwise,
    :rtype: bool
    """
    try:
        if len(arg) != 2:
            return False
        create_intersection(arg[0], arg[1])
        return True
    except (TypeError, ValueError):
        return False

# Tests
def equal_intersections(intersection1:any, intersection2:any) -> bool:
    """
    Verifies the two intersections are equal.

    :param intersection1: First intersection.
    :type intersection1: any
    :param intersection2: Second intersection.
    :type intersection2: any

    :return: True if the two intersections are equal, False otherwise.
    :rtype: bool
    """
    return is_intersection(intersection1) and is_intersection(intersection2)\
        and obtain_col(intersection1) == obtain_col(intersection2)\
        and obtain_row(intersection1) == obtain_row(intersection2)

# Transformers (mutators)
def intersection_to_str(intersection: 'tuple[str,int]') -> str:
    """
    Converts an intersection to a string.

    :param intersection: A valid intersection.
    :type intersection: tuple(str,int)

    :return: A string representing the intersection. (External Representation of an Intersection)
    :rtype: str
    """
    return  obtain_col(intersection) + str(obtain_row(intersection))

def str_to_intersection(string: str) -> 'tuple[str,int]':
    """
    Converts a string to an intersection.

    :param string: A string representing an intersection.
    :type string: str

    :return: An intersection in its internal representation.
    :rtype: tuple[str,int]
    """
    return create_intersection(string[0], int(string[1:]))

# High-Level Functions
def obtain_adjacent_intersections(intersection: 'tuple[str,int]', last_intersection: 'tuple[str,int]') -> 'tuple[tuple[str,int], ...]':
    """
    Obtains the intersections adjacent to an intersection given the board's upmost intersection.

    :param intersection: Any intersection on the board.
    :type intersection: tuple[str,int]
    :param last_intersection: The intersection in the upper right corner of the Go board.
    :type last_intersection: tuple(str,int)

    :return: A tuple with the intersections adjacent to the given intersection, sorted by the reading order of the Go board.
    :rtype: tuple(tuple(str,int), ...)
    """
    adjacents = []
    for x, y in [(0, -1), (-1, 0), (1, 0), (0, 1)]: # Adjacent Coordinate Vectors
        try:
            new_intersection = create_intersection(chr(ord(obtain_col(intersection)) + x), obtain_row(intersection) + y)
            # Verifies the new intersection is within the limits of the board.
            if ord(obtain_col(new_intersection)) <= ord(obtain_col(last_intersection)) \
                and obtain_row(new_intersection) <= obtain_row(last_intersection):
                adjacents.append(new_intersection)
        except ValueError:
            pass
    return sort_intersections(tuple(adjacents))

def sort_intersections(tuple_intersections: 'tuple[tuple[str,int], ...]') -> 'tuple[tuple[str,int], ...]':
    """
    Sorts a tuple of intersections by the reading order of the Go board.

    :param tuple_intersections: A tuple of intersections.
    :type tuple_intersections: tuple(tuple(str,int), ...)

    :return: The given tuple of intersections sorted by the reading order of the Go board.
    :rtype: tuple(tuple(str,int), ...)
    """
    return tuple(sorted(tuple_intersections, key=lambda x: (obtain_row(x), obtain_col(x))))

# Stone ADT
# Constructors
def create_white_stone() -> str:
    """
    Creates a white stone.

    :return: A stone belonging to the white player.
    :rtype: str
    """
    return 'W'

def create_black_stone() -> str:
    """
    Creates a black stone.

    :return: A stone belonging to the black player.
    :rtype: str
    """
    return 'B'

def create_neutral_stone() -> str:
    """
    Creates a neutral stone (a stone that doesn't belong to any player).

    :return: A neutral stone.
    :rtype: str
    """
    return 'N'

# Recognizers
def is_stone(arg:any) -> bool:
    """
    Verifies if the argument is a valid stone.

    :param arg: Any type of argument.
    :type arg: any

    :return: True if the argument is a valid stone, False otherwise.
    :rtype: bool
    """
    return arg in {create_white_stone(),create_black_stone(),create_neutral_stone()}

def is_white_stone(stone: str) -> bool:
    """
    Verifies if a stone is white.

    :param stone: Any stone.
    :type stone: str

    :return: True if the stone belongs to the white player, False otherwise.
    :rtype: bool
    """
    return stone == create_white_stone()

def is_black_stone(stone: str) -> bool:
    """
    Verifies if a stone is black.

    :param stone: Any stone.
    :type stone: str

    :return: True if the stone belongs to the black player, False otherwise.
    :rtype: bool
    """
    return stone == create_black_stone()

# Test
def equal_stones(stone1: str,stone2: str) -> bool:
    """
    Verifies if two stones are equal.

    :param stone1: Any stone.
    :type stone1: str
    :param stone2: Another stone.
    :type stone2: str

    :return: True if the stones are equal, False otherwise.
    :rtype: bool
    """
    return is_stone(stone1) and is_stone(stone2) \
        and ((is_white_stone(stone1) and is_white_stone(stone2)) or\
        (is_black_stone(stone1) and is_black_stone(stone2)) or\
        (not is_player_stone(stone1) and not is_player_stone(stone2)))

# Transformer (mutator)
def stone_to_str(stone: str) -> str:
    """
    Converts a stone to a string representation.

    :param stone: Any stone in its internal representation.
    :type stone: str

    :return: A string that represents the stone (external representaion).
    :rtype: str
    """
    if is_white_stone(stone):
        return "O"
    elif is_black_stone(stone):
        return "X"
    else:
        return "."

# High-Level Functions
def is_player_stone(stone: str) -> bool:
    """
    Verifies if a stone belongs to a player (if it's a white or black stone).

    :param stone: Any stone in its internal representation. 
    :type stone: str

    :return: True if the stone belongs to a player, False otherwise.
    :rtype: bool
    """
    return is_white_stone(stone) or is_black_stone(stone)

# Goban ADT
# Constructor
def create_empty_goban(n: int) -> list:
    """
    Create an empty Go board (Goban).

    :param n: The size of the Goban (9, 13 ou 19).
    :type n: int

    :return: An empty Goban
    :rtype: list
    :raises ValueError: If the argument is invalid
                        (if n is not an integer and not 9, 13 or 19).
    """
    # Argument Validation
    if not isinstance(n,int) or n not in {9, 13, 19}:
        raise ValueError('create_empty_goban: invalid argument')
    return [[create_neutral_stone() for _ in range(n)] for _ in range(n)]

def create_goban(n: int, white_intersections: 'tuple[tuple[str,int], ...]', black_intersections: 'tuple[tuple[str,int], ...]') -> list:
    """
    Creates a Goban with black and white stones in the specified intersections.

    :param n: The size of the Goban (9, 13 ou 19).
    :type n: int
    :param white_intersections: A tuple with the intersections occupied by white stones.
    :type black_intersections: tuple
    :param ip: A tuple with the intersections occupied by black stones.
    :type ip: tuple

    :return: Um tabuleiro de Go com as stones nas posições especificadas.
    :rtype: list
    :raises ValueError: If the arguments are invalid (not formatted as expected or
                        if there's intersections occupied by both black and white pieces simultaneously).
    """
    # Argument Validation
    try:
        create_empty_goban(n)
    except ValueError as e:
        raise ValueError("create_goban: invalid arguments") from e # Re-raises ValueError
    if not isinstance(white_intersections, tuple) or not isinstance(black_intersections, tuple):
        raise ValueError('create_goban: invalid arguments')
    if len(set(white_intersections)) != len(white_intersections) or len(set(black_intersections)) != len(black_intersections): # Searches for duplicates
        raise ValueError('create_goban: invalid arguments')

    goban = create_empty_goban(n)

    for white_intersection in white_intersections:
        # Verifies the intersections are valid and are not found in black_intersections.
        if not is_intersection(white_intersection) or not is_valid_intersection(goban, white_intersection)\
            or white_intersection in black_intersections:
            raise ValueError('create_goban: invalid arguments')
        place_stone(goban,white_intersection,create_white_stone())

    for black_intersection in black_intersections:
        # Verifies all intersections in black_intersections are valid intersections.
        if not is_intersection(black_intersection) or not is_valid_intersection(goban, black_intersection):
            raise ValueError('create_goban: invalid arguments')
        place_stone(goban,black_intersection,create_black_stone())
    return goban

def create_copy_goban(goban: list) -> list:
    """
    Creates a copy of the goban.

    :param goban: Any goban.
    :type goban: list

    :return: A deep copy of the original goban.
    :rtype: list
    """
    return [[stone for stone in row] for row in goban] # Deep Copy

# Selectors
def obtain_last_intersection(goban: list) -> 'tuple[str,int]':
    """
    Obtains the intersection in the top right corner of the goban.

    :param goban: Any goban.
    :type goban: list

    :return: The intersection in the top right corner of the goban.
    :rtype: tuple
    """
    return create_intersection(chr(len(goban)-1+ord("A")),len(goban))

def obtain_stone(goban: list, intersection: 'tuple[str,int]') -> str:
    """
    Obtains the stone at the intersection specified.

    :param goban: A goban.
    :type goban: list
    :param intersection: Any intersection present in the goban.
    :type intersection: tuple(str,int)

    :return: The stone found in the given intersection.
    :rtype: str
    """
    return goban[ord(obtain_col(intersection))-ord("A")][obtain_row(intersection)-1]

def obtain_chain(goban: list, intersection: 'tuple[str,int]'):
    """
    Obtains a chain of intersections connected to the specified intersection.

    :param goban: A goban.
    :type goban: list
    :param intersection: Any intersection in the goban.
    :type intersection: tuple[str,int]

    :return: A list of intersections in the chain of the given intersection sorted by reading order of the goban.
    :rtype: list[tuple[str,int]]
    """
    # Tail Recursion
    def _find_chain(goban: list, intersection: tuple[str,int], visited: set['tuple[str,int]']) -> list[tuple[str,int]]:
        # Auxiliary Internal function that looks for chains by finding adjacents of adjacents
        visited.add(intersection)
        adjacents = obtain_adjacent_intersections(intersection, obtain_last_intersection(goban))
        chain = [intersection]
        for new_intersection in adjacents:
            if new_intersection not in visited and\
                equal_stones(obtain_stone(goban, new_intersection),obtain_stone(goban, intersection)):
                chain.extend(_find_chain(goban, new_intersection, visited))
        return chain

    visited = set() # Using a set to avoid duplicates
    return sort_intersections(tuple(tuple(chain) for chain in _find_chain(goban,intersection,visited)))

# Modifiers
def place_stone(goban: list, intersection: 'tuple[str,int]', stone: str) -> list:
    """
    Places a stone on the goban at the given intersection.

    :param goban: A goban.
    :type goban: list
    :param intersection: Any intersection on the goban.
    :type intersection: tuple[str,int]
    :param stone: Any stone.
    :type stone: str

    :return: A modified goban board with the stone placed.
    :rtype: list
    """
    goban[ord(obtain_col(intersection))-ord("A")][obtain_row(intersection)-1] = stone
    return goban

def remove_stone(goban: list, intersection: 'tuple[str,int]') -> list:
    """
    Removes the stone from the given intersection in the goban.

    :param goban: Any goban.
    :type goban: list
    :param intersection: Any intersection in the goban.
    :type intersection: tuple[str,int]

    :return: The modified goban with the stoned removed.
    :rtype: list
    """
    goban[ord(obtain_col(intersection))-ord("A")][obtain_row(intersection)-1] = create_neutral_stone()
    return goban

def remove_chain(goban: list, tuple_intersections: 'tuple[str,int]') -> list:
    """
    Removes a chain of stones from the goban.

    :param goban: A goban.
    :type goban: list
    :param tuple_intersections: A tuple containing the intersections that form the chain to be removed.
    :type tuple_intersections: tuple[str,int]

    :return: The modified goban with the given chain removed.
    :rtype: list
    """
    for intersection in tuple_intersections:
        remove_stone(goban, intersection)
    return goban

# Recognizers
def is_goban(arg: any) -> bool:
    """
    Verifies if the argument is a valid Go board.

    :param arg: Any argument.
    :type arg: any

    :return: True if the argument is a valid Go board, False otherwise.
    :rtype: bool
    """
    # Argument Validation
    try:
        if (isinstance(arg, list) and\
        all(isinstance(row, list) and len(row) == len(arg) for row in arg) and\
        all(is_stone(stone) for row in arg for stone in row)):
            create_empty_goban(len(arg))
            return True
    except ValueError:
        pass
    return False

def is_valid_intersection(goban: list, intersection: 'tuple[str,int]') -> bool:
    """
    Verifies if an intersection is valid. (Is in the correct form and within the limits of the goban)

    :param goban: Any goban
    :type goban: list
    :param intersection: Any
    :type intersection: tuple[str,int]

    :return: True if the intersection is an intersection and its within the limits of the goban, False otherwise.
    :rtype: bool
    """
    return is_intersection(intersection) and\
        (ord(obtain_col(intersection))-ord("A")+1) <= obtain_row(obtain_last_intersection(goban))\
        and obtain_row(intersection) <= obtain_row(obtain_last_intersection(goban))

# Test
def equal_gobans(goban1: list, goban2: list) -> bool:
    """
    Verifies the two gobans are equal.

    :param goban1: A goban.
    :type goban1: list
    :param goban2: Another goban.
    :type goban2: list

    :return: True if the gobans are equal, False otherwise.
    :rtype: bool
    """
    return is_goban(goban1) and is_goban(goban2) and\
        equal_intersections(obtain_last_intersection(goban1),obtain_last_intersection(goban2)) and\
        all(all(equal_stones(stone1,stone2) for stone1, stone2 in zip(row1,row2)) for row1, row2 in zip(goban1,goban2))


# Transformer (mutator)
def goban_to_str(goban: list) -> str:
    """
    Converts a goban from its internal representation to a string.

    :param goban: A goban.
    :type goban: list

    :return: A string that represents the goban.
    :rtype: str
    """
    # Can use obtain_row because the goban is square so it has the same number of columns and rows.
    num_columns = obtain_row(obtain_last_intersection(goban))
    # Creates a dictionary that connects the indices of the column to the letters A, B, C, etc.
    vertical_label = {i: chr(65+i) for i in range(num_columns)}
    res = "   " + " ".join([vertical_label[i] for i in range(num_columns)]) + "\n "
    # Inverse loop over the rows of the goban.
    for j in range(obtain_row(obtain_last_intersection(goban))-1,-1,-1):
        horizontal_label = str(j+1)
        # Adjusts horizontal label spacing in case the label has two digits.
        if len(horizontal_label) == 2:
            res = res[:-1] # Removes a space before adding the label.
        res += f"{horizontal_label}"
        # Adds the stone representations to the current row.
        for k in range(num_columns):
            res += " " + stone_to_str(goban[k][j])
        # Adds the horizontal label to the row
        # Ajusts the spacing in case the label has two digits by removing a space before the label.
        if len(horizontal_label) == 2:
            res += f" {horizontal_label}\n "
        else:
            res += f"  {horizontal_label}\n "
    # Adds the vertical labels again at the end of the board.
    return res + "  " + " ".join([vertical_label[i] for i in range(num_columns)])

# High-Level Functions
def obtain_territories(goban: list) -> 'tuple[tuple[tuple[str,int], ...], ...]':
    """
    Obtains the territories in a goban.

    :param goban: A goban.
    :type goban: list

    :return: A tuple sorted by the reading order of the goban
             where each territory is a tuple of intersections.
    :rtype: tuple(tuple(tuple(str,int), ...), ...)
    """
    territories = []
    # Nested loops to go through all the intersections in the goban
    for j in range(obtain_row(obtain_last_intersection(goban))):
        for k in range(obtain_row(obtain_last_intersection(goban))):
            intersection = create_intersection(chr(j+ord("A")),k+1)
            # Checks if an intersections is valid and free
            if is_valid_intersection(goban, intersection) and\
                (not is_player_stone(obtain_stone(goban,intersection)) and\
                not any(intersection in i for i in territories)):
                territories.append(obtain_chain(goban,intersection))
    # Sort the territory according to the coordinates of the first intersections
    return tuple(sorted(tuple(territories), key=lambda x: (obtain_row(x[0]), obtain_col(x[0]))))

def obtain_different_adjacents(goban: list, tuple_intersections: 'tuple[tuple[str,int], ...]') -> 'tuple[tuple[str,int], ...]':
    """
    Obtains the adjacents intersections with different stone types.

    :param goban: A goban
    :type goban: list
    :param tuple_intersections: A tuple of intersections
    :type tuple_intersections: tuple[tuple[str,int], ...]

    :return: A tuple of adjacent free intersections if the intersections in the given tuple are occupied by player stones
             or a tuple of intersections occupied by player stones (black or white), if the intersections in the given tuple are free.
    :rtype: tuple[tuple[str,int], ...]
    """
    different_adjacents = set()
    set_intersections = set(tuple_intersections)
    # Iterates over the intersections in the given tuple
    for intersection in tuple_intersections:
        adjacents = obtain_adjacent_intersections(intersection, obtain_last_intersection(goban))
        # Iterates over the adjacent intersections
        for adjacent in adjacents:
            if adjacent not in set_intersections:
                # If the original intersection is ocupied add free intersections to the different_adjacents set.
                # Otherwise, if the original intersection is free add the intersections occupied by player stones to the set.
                if (equal_stones(obtain_stone(goban, adjacent),create_neutral_stone()) and\
                    not equal_stones(obtain_stone(goban, intersection),create_neutral_stone())) or \
                   (not equal_stones(obtain_stone(goban, adjacent),create_neutral_stone()) and\
                     equal_stones(obtain_stone(goban, intersection),create_neutral_stone())):
                    different_adjacents.add(adjacent)
    return sort_intersections(tuple(different_adjacents))

def play(goban: list, intersection: 'tuple[str,int]', stone: str) -> list:
    """
    Makes a play in a game of Go.

    :param goban: A goban.
    :param intersection: An intersection.
    :param stone: A stone.

    :return: The modified goban after the move is made.
    """
    goban = place_stone(goban, intersection, stone)

    adjacents = obtain_adjacent_intersections(intersection, obtain_last_intersection(goban))
    # Filters the adjacent intersections which contain an opponent stone.
    oponent_adjacents = list(filter(lambda adjacent: not equal_stones(obtain_stone(goban, adjacent),stone)\
                                    and is_player_stone(obtain_stone(goban,adjacent)),adjacents))
    # Removes opponent chains without liberties
    for adjacent in oponent_adjacents:
        adjacent_chain = obtain_chain(goban, adjacent)
        if not obtain_different_adjacents(goban, adjacent_chain):
            goban = remove_chain(goban, adjacent_chain)
    return goban

def obtain_num_player_stones(goban: list) -> tuple:
    """
    Obtains the number of white and black stones in the Goban.

    :param goban: A goban.
    :type goban: list

    :return: A tuple containing the number of white and black stones, respectively.
    :rtype: tuple
    """
    black = 0
    white = 0
    # Iterates over the rows and columns of the goban.
    for i in range(obtain_row(obtain_last_intersection(goban))):
        for j in range(obtain_row(obtain_last_intersection(goban))):
            # Creates an intersection with the current indexes.
            intersection = create_intersection((chr(i+ord("A"))),(j+1))
            # Checks if a stone is white and if so increments the white counter.
            if equal_stones(obtain_stone(goban, intersection),create_white_stone()):
                white += 1
            # Checks if a stone is black and if so, increments the black counter.
            if equal_stones(obtain_stone(goban, intersection),create_black_stone()):
                black +=1
    return (white,black)

def calculate_points(goban: list) -> 'tuple[int, int]':
    """
    Calculates the points of the white and black player in a given goban.

    :param goban: A goban.
    :type goban: list

    :return: A tuple containing the number of points of the white and black player, respectively.
    :rtype: tuple
    """
    territories = obtain_territories(goban)
    white_territory = 0
    black_territory = 0

    # Iterates of the tuple of territories.
    for territory in territories:
        # Assume the territory can be both white and black.
        is_white_territory = True
        is_black_territory = True
        for intersection in territory:
            adjacents = obtain_adjacent_intersections(intersection, obtain_last_intersection(goban))
            for adjacent in adjacents:
                # Checks if there is black or white stones adjacent to the territory.
                if equal_stones(obtain_stone(goban, adjacent), create_black_stone()):
                    # If the stones adjacent to the territory are black then the territory isn't white.
                    is_white_territory = False
                elif equal_stones(obtain_stone(goban, adjacent), create_white_stone()):
                    # Likewise, if the stones adjacent to the territory are white then the territory isn't black.
                    is_black_territory = False

        white_stones, black_stones = obtain_num_player_stones(goban)

        # If a goban is empty and the territory isn't black or white.
        if white_stones == 0 and black_stones == 0:
            is_white_territory = False
            is_black_territory = False

        # Adds the number of intersections of the territory to the corresponding counter based on whether the territory is black or white.
        if is_white_territory:
            white_territory += len(territory)
        if is_black_territory:
            black_territory += len(territory)

    return (white_territory + white_stones, black_territory + black_stones)

def is_legal_play(goban: list, intersection: 'tuple[str,int]', stone: str, prev_goban: list) -> bool:
    """
    Verifies if a play is legal.

    :param goban: A goban.
    :type goban: list
    :param intersection: A valid intersection for the given goban.
    :type intersection: tuple(str,int)
    :param stone: A stone.
    :type stone: str
    :param prev_goban: The state the goban can't reach after the play is made (Ko's Rule).
    :type prev_goban: list

    :return: True if the play is legal, False otherwise.
    :rtype: bool
    """
    # Argument Validation. If they're invalid the play is illegal.
    if not is_valid_intersection(goban, intersection) or \
    is_player_stone(obtain_stone(goban, intersection)):
        return False

    copy_goban = create_copy_goban(goban)
    play(copy_goban, intersection, stone)

    # Checks Ko's Rule
    if equal_gobans(copy_goban, prev_goban):
        return False

    # Checks the Suicide Rule
    if not obtain_different_adjacents(copy_goban,obtain_chain(copy_goban,intersection)):
        return False
    return True

def player_turn(goban: list, stone: str, prev_goban: list) -> bool:
    """
    A player's turn in a game of Go.

    :param goban: A goban.
    :type goban: list
    :param stone: A player stone.
    :type stone: str
    :param prev_goban: The state the goban can't reach after the play is made (Ko's Rule).
    :type prev_goban: list

    :return: True if the player makes a valid play, False otherwise.
    :rtype: bool
    """
    valid_turn = False
    while not valid_turn:
        # Asks the player for a move.
        move = input(f"Write down an intersection or 'P' to pass the turn [{stone_to_str(stone)}]:")
        # Checks if a player decided to pass their turn.
        if move == 'P':
            return False
        else:
            try:
                # Converts the player's input into an intersection.
                intersection = str_to_intersection(move)
                # Makes the play if the play is legal.
                if is_legal_play(goban, intersection, stone, prev_goban):
                    goban = play(goban, intersection, stone)
                    valid_turn = True
                else:
                    pass
            except (ValueError, IndexError):
                pass # If the move is illegal ask for a move again.
    return True

def go(n: int, white_intersections: 'tuple[str,...]', black_intersections: 'tuple[str,   ]') -> bool:
    """
    The main function that allows a full game of Go to be played.

    :param n: The size of the goban (9, 13 or 19)
    :type n: int
    :param white_intersections: A tuple of intersections where white stones are placed.
    :type white_intersections: tuple of strings
    :param black_intersections: A tuple of intersections where black stones are placed.
    :type black_intersections: tuple of strings

    :return: True if the player with white stones wins, False otherwise.
    :rtype: bool
    """
    if not isinstance(black_intersections, tuple) or not isinstance(white_intersections,tuple):
        raise ValueError('go: invalid arguments')
    internal_white_intersections = []
    internal_black_intersections = []
    # Argument Validation
    # Converts the intersections given in string format to their internal representation.
    try:
        for white_intersection in white_intersections:
            if isinstance(white_intersection,str):
                try:
                    internal_white_intersections.append(str_to_intersection(white_intersection))
                except ValueError as e:
                    raise ValueError('go: invalid arguments') from e
            else:
                internal_white_intersections.append(white_intersection)
        for black_intersection in black_intersections:
            if isinstance(black_intersection,str):
                try:
                    internal_black_intersections.append(str_to_intersection(black_intersection))
                except ValueError as e:
                    raise ValueError('go: invalid arguments') from e
            else:
                internal_black_intersections.append(black_intersection)
        goban = create_goban(n, tuple(internal_white_intersections), tuple(internal_black_intersections))
    except (TypeError, ValueError) as e:
        raise ValueError('go: invalid arguments') from e

    pass_turn = 0 # Counts how many times the players passed their turn.
    black_player = True # The black player starts
    old_gobans = []  # To save old goban states.
    prev_goban = create_copy_goban(goban)

    while pass_turn < 2:
        # Shows the score board
        points_white, points_black = calculate_points(goban)
        print("White (O) has", points_white, "points")
        print("Black (X) has", points_black, "points")
        old_gobans.append(create_copy_goban(goban))

        if black_player:
            stone = create_black_stone()
        else:
            stone = create_white_stone()

        # Show the board and play the player turn.
        print(goban_to_str(goban))
        current_turn = player_turn(goban, stone, prev_goban)

        if not current_turn: # If a player passes their turn.
            pass_turn += 1
        else:
            pass_turn = 0 # Reset counter so that the games only ends if two turns are skipped in a row.

        if len(old_gobans) >= 1:
            prev_goban = old_gobans[-1] # Gets the previous board state.
            old_gobans.pop(0) # Removes old gobans to save memory.
        black_player = not black_player # Changes player.

    # Shows the final board and scoreboard.
    print("White (O) has", points_white, "points")
    print("Black (X) has", points_black, "points")
    print(goban_to_str(goban))

    # Returns True if the white player wins, False otherwise.
    return points_white >= points_black
