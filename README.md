# Go
The game Go as a Python text-based game.

This was the 2nd Project for my Fundamentals of Programming class, mainly meant to test the use of Abstract Data Types. The `.pdf` file contains the instructions provided by the teacher. The included Python Tests (public and private) were also provided by the teacher.

## How to Play

1. **Setup**: Ensure you have Python installed on your system.

2. **Run the Game**: Execute the following command in your terminal:
    ```sh
    $ python PlayGo.py
    ```

3. **Game Board**: The game board is a 9x9, 13x13, or 19x19 grid. The columns are labeled with letters, and the rows are numbered. Here is an example of a 9x9 grid:
    <pre>
        A B C D E F G H I  
     9 . . . . . . . . .  9  
     8 . . . . . . . . .  8  
     7 . . . . . . . . .  7  
     6 . . . . . . . . .  6  
     5 . . . . . . . . .  5  
     4 . . . X . . . . .  4  
     3 . . O . . . . . .  3  
     2 . . O . . X . . .  2  
     1 . . . . . . . . .  1  
        A B C D E F G H I</pre>
- `X` represents a black stone.
- `O` represents a white stone.
- `.` represents an empty intersection.  

5. **Placing Stones**:
- Players take turns to place stones on the board.
- Use coordinates to specify where to place your stone (e.g., `D4`).

7. **Objective**: Capture the opponent's stones by surrounding them.

8. **End Game**: The game ends when both players pass their turn consecutively.

Enjoy playing Go!