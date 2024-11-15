"""2nd Project for Foundations of Programming 2023/2024

A Python program that allows you to play the game Go.

This project focuses on the use of Abstract Data Types (ADTs).
"""

# Intersection ADT
# Auxiliary Function
def is_valid_intersection_arguments(column:str, row:int) -> bool:
    """
    Verifies if the arguments are valid for the intersection ADT.

    :param column: Column letter (A to S).
    :type column: str
    :param row: Row number (1 to 19).
    :type row: int

    :return: True if the arguments are valid, False otherwise.
    :rtype: bool
    """
    return isinstance(column, str) and isinstance(row, int)\
    and len(column) == 1 and not isinstance(row, bool)\
    and "A" <= column <= "S" and 1 <= row <= 19

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
    if not is_valid_intersection_arguments(column, row):
        raise ValueError("create_intersection: invalid arguments")
    return (column, row)

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
    return isinstance(arg, tuple) and len(arg) == 2 and \
    is_valid_intersection_arguments(obtain_col(arg), obtain_row(arg))

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
    return obtain_col(intersection) + str(obtain_row(intersection))

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
    col, row = obtain_col(intersection), obtain_row(intersection)
    max_col, max_row = obtain_col(last_intersection), obtain_row(last_intersection)
    adjacents = []
    for x, y in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
        if "A" <= chr(ord(col) + x) <= max_col and 1 <= row + y <= max_row:
            adjacents.append(create_intersection(chr(ord(col) + x), row + y))
    return sort_intersections(tuple(adjacents))

def sort_intersections(tuple_intersections: 'tuple[tuple[str,int], ...]') -> 'tuple[tuple[str,int], ...]':
    """
    Sorts a tuple of intersections by the reading order of the Go board.

    :param tuple_intersections: A tuple of intersections.
    :type tuple_intersections: tuple(tuple(str,int), ...)

    :return: The given tuple of intersections sorted by the reading order of the Go board.
    :rtype: tuple(tuple(str,int), ...)
    """
    return tuple(sorted(tuple_intersections,key=lambda intersection:
    (obtain_row(intersection), obtain_col(intersection))))

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
    return arg in {create_white_stone(), create_black_stone(), create_neutral_stone()}

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
    if stone == create_white_stone():
        return "O"
    if stone == create_black_stone():
        return "X"
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
# Auxiliary Function
def is_valid_goban_size(n: any) -> bool:
    """
    Verifies if the size of the goban is valid.

    :param n: The size of the goban.
    :type n: int

    :return: True if the size is valid, False otherwise.
    :rtype: bool
    """
    return isinstance(n, int) and not isinstance(n, bool) and n in {9, 13, 19}
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
    if not is_valid_goban_size(n):
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
    if not is_valid_goban_size(n) or \
    not isinstance(white_intersections, tuple) or \
    not isinstance(black_intersections, tuple) or \
    not all(is_intersection(intersection) \
    for intersection in white_intersections + black_intersections) or \
    len(set(white_intersections + black_intersections)) \
    != len(white_intersections) + len(black_intersections):
        raise ValueError('create_goban: invalid arguments')

    goban = create_empty_goban(n)
    for intersection in white_intersections + black_intersections:
        if not is_valid_intersection(goban, intersection):
            raise ValueError('create_goban: invalid arguments')
        if intersection in white_intersections:
            stone = create_white_stone()
        else:
            stone = create_black_stone()
        place_stone(goban, intersection, stone)
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
    return create_intersection(chr(ord("A") + len(goban) - 1), len(goban))

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
    return goban[obtain_row(intersection) - 1][ord(obtain_col(intersection)) - ord("A")]

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
    def _find_chain(goban, intersection, visited):
        visited.add(intersection)
        chain = [intersection]
        for adj in obtain_adjacent_intersections(intersection, obtain_last_intersection(goban)):
            if adj not in visited and equal_stones(obtain_stone(goban, adj), obtain_stone(goban, intersection)):
                chain.extend(_find_chain(goban, adj, visited))
        return chain
    return sort_intersections(tuple(_find_chain(goban, intersection, set())))

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
    goban[obtain_row(intersection)-1][ord(obtain_col(intersection))-ord("A")] = stone
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
    return place_stone(goban, intersection, create_neutral_stone())

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
    return isinstance(arg, list) and is_valid_goban_size(len(arg)) and \
    all(isinstance(row, list) and len(row) == len(arg) for row in arg) and \
    all(is_stone(stone) for row in arg for stone in row)

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
    return is_goban(goban) and is_intersection(intersection) and \
    obtain_col(intersection) <= obtain_col(obtain_last_intersection(goban)) and \
    obtain_row(intersection) <= obtain_row(obtain_last_intersection(goban))

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
    if not is_goban(goban1) or not is_goban(goban2):
        return False
    last_intersection = obtain_last_intersection(goban1)
    if last_intersection != obtain_last_intersection(goban2):
        return False
    dim = obtain_row(last_intersection)
    return all(equal_stones(
    obtain_stone(goban1, create_intersection(chr(col + ord("A")), row + 1)),
    obtain_stone(goban2, create_intersection(chr(col + ord("A")), row + 1)))
    for row in range(dim) for col in range(dim))

# Transformer (mutator)
def goban_to_str(goban: list) -> str:
    """
    Converts a goban from its internal representation to a string.

    :param goban: A goban.
    :type goban: list

    :return: A string that represents the goban.
    :rtype: str
    """
    dim = obtain_row(obtain_last_intersection(goban))
    columns = [chr(i) for i in range(ord('A'), ord('A') + dim)]
    string = '   ' + ' '.join(columns[:dim]) + '\n'
    for i in range(dim - 1, -1, -1):
        string += f'{i+1:2} ' + ' '\
        .join(stone_to_str(obtain_stone(goban, create_intersection(columns[col],i+1)))\
        for col in range(dim)) + f' {i+1:2}\n'
    string += '   ' + ' '.join(columns[:dim])
    return string

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
    visited = set()
    dim = obtain_row(obtain_last_intersection(goban))
    for row in range(dim):
        for col in range(dim):
            intersection = create_intersection(chr(col + ord("A")), row + 1)
            if intersection not in visited and \
            not is_player_stone(obtain_stone(goban, intersection)):
                chain = obtain_chain(goban, intersection)
                territories.append(chain)
                visited.update(chain)
    return tuple(sort_intersections(tuple(territory)) for territory in territories)

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
    return sort_intersections(tuple({
    adjacent for intersection in tuple_intersections \
    for adjacent in obtain_adjacent_intersections(intersection, obtain_last_intersection(goban)) \
    if adjacent not in tuple_intersections and \
    is_player_stone(obtain_stone(goban, adjacent)) != \
    is_player_stone(obtain_stone(goban, intersection))}))

def play(goban: list, intersection: 'tuple[str,int]', stone: str) -> list:
    """
    Makes a play in a game of Go.

    :param goban: A goban.
    :param intersection: An intersection.
    :param stone: A stone.

    :return: The modified goban after the move is made.
    """
    goban = place_stone(goban, intersection, stone)

    for adjacent in obtain_adjacent_intersections(
    intersection, obtain_last_intersection(goban)):
        if is_player_stone(obtain_stone(goban, adjacent)) and \
        not equal_stones(obtain_stone(goban, adjacent), stone) and \
        not obtain_different_adjacents(goban, obtain_chain(goban, adjacent)):
            goban = remove_chain(goban, obtain_chain(goban, adjacent))
    return goban

def obtain_num_player_stones(goban: list) -> tuple:
    """
    Obtains the number of white and black stones in the Goban.

    :param goban: A goban.
    :type goban: list

    :return: A tuple containing the number of white and black stones, respectively.
    :rtype: tuple
    """
    dim = obtain_row(obtain_last_intersection(goban))
    columns = [chr(i) for i in range(ord('A'), ord('A') + dim)]
    white = sum(is_white_stone(obtain_stone(goban, create_intersection(col, row))) \
    for col in columns[:dim] for row in range(1, dim + 1))
    black = sum(is_black_stone(obtain_stone(goban, create_intersection(col, row))) \
    for col in columns[:dim] for row in range(1, dim + 1))
    return (white, black)

def calculate_points(goban: list) -> 'tuple[int, int]':
    """
    Calculates the points of the white and black player in a given goban.

    :param goban: A goban.
    :type goban: list

    :return: A tuple containing the number of points of the white and black player, respectively.
    :rtype: tuple
    """
    territories = obtain_territories(goban)
    points = obtain_num_player_stones(goban)
    white_territory = sum(len(territory) for territory in territories \
    if obtain_different_adjacents(goban, territory) and \
    all(is_white_stone(obtain_stone(goban, intersection)) \
    for intersection in obtain_different_adjacents(goban, territory)))
    black_territory = sum(len(territory) for territory in territories \
    if obtain_different_adjacents(goban, territory) and \
    all(is_black_stone(obtain_stone(goban, intersection)) \
    for intersection in obtain_different_adjacents(goban, territory)))
    return (points[0] + white_territory, points[1] + black_territory)

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
    return obtain_different_adjacents(copy_goban,obtain_chain(copy_goban,intersection))

def player_turn(goban: list, stone: str, prev_goban: list) -> bool:
    """
    A player's turn in a game of Go.

    :param goban: A goban.
    :type goban: list
    :param stone: A player stone.
    :type stone: str
    :param prev_goban: The state the goban can't reach after the play is made (Ko's Rule).
    :type prev_goban: list

    :return: True if the player makes a valid play, False when the player passes his turn.
    :rtype: bool
    """
    while True:
        move = input(f"Write down an intersection or 'P' to pass the turn [{stone_to_str(stone)}]:")
        if move == 'P':
            return False
        try:
            intersection = str_to_intersection(move)
            if is_legal_play(goban, intersection, stone, prev_goban):
                play(goban, intersection, stone)
                return True
        except ValueError:
            continue

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
