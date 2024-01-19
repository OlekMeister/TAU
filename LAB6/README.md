# SimpleGame

SimpleGame is a Python class representing a basic grid-based game where the player navigates from point A to point B while strategically avoiding obstacles. The game ensures the existence of a traversable path between A and B.

## Class Methods

- **generate_board_with_path():** Generates a game board with a predetermined path between A and B.
- **is_path_available():** Checks for the existence of a path between the starting point A and the destination point B.
- **generate_board():** Generates a random game board with a starting point A, destination point B, and obstacles.
- **generate_stop():** Generates a random destination point B, avoiding the starting point A column.
- **generate_obstacles():** Places random obstacles on the board, avoiding A, B, and existing obstacles.
- **display_board():** Displays the current state of the game board.
- **move(direction: str):** Moves the player in the specified direction (up, down, left, right).
- **handle_move(new_row: int, new_col: int):** Handles the player's movement, updating the board and path.
- **reset_game():** Resets the game to its initial state.
- **is_game_over():** Checks if the game is over, i.e., if the player has reached the destination point B.

## GitHub Actions screenshots

![App Screenshot](https://snipboard.io/LlC9xX.jpg)

![App Screenshot](https://snipboard.io/suPSR8.jpg)

## Example Usage

```python
from SimpleGame import SimpleGame

# Initialize the game with 5 rows and 5 columns
game = SimpleGame(rows=5, cols=5)

# Generate a board with a guaranteed path between A and B
game.generate_board_with_path()

# Display the initial state of the game board
game.display_board()

# Move the player and update the board
game.move('right')

# Check if the game is over
if game.is_game_over():
    print("Congratulations! You reached the destination!")
else:
    print("Keep navigating to reach the destination.")

# Reset the game to its initial state
game.reset_game()
