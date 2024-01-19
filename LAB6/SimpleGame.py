"""
SimpleGame class represents a basic grid-based game where the player moves from point A to point B
while avoiding obstacles. The game guarantees the existence of a path between A and B.

Author: Aleksander Guzik

Methods:
    generate_board_with_path(): Generates a game board with a guaranteed path between A and B.
    is_path_available(): Checks if a path exists between the starting point A and the destination point B.
    generate_board(): Generates a random game board with starting point A, destination point B, and obstacles.
    generate_stop(): Generates a random destination point B, avoiding the starting point A column.
    generate_obstacles(): Generates random obstacles on the board, avoiding A, B, and previous obstacles.
    display_board(): Displays the current state of the game board.
    move(direction: str): Moves the player in the specified direction (up, down, left, right).
    handle_move(new_row: int, new_col: int): Handles the player's move, updating the board and path.
    reset_game(): Resets the game to its initial state.
    is_game_over(): Checks if the game is over, i.e., if the player has reached the destination point B.
"""

import random
from collections import deque

class SimpleGame:
    def __init__(self, rows, cols):
        # Initialize the game with the specified number of rows and columns.
        self.rows = rows
        self.cols = cols
        # Create an empty game board filled with spaces.
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        # Initialize the starting and destination points, obstacles, and the player's path.
        self.start = (0, 0)
        self.stop = (0, 0)
        self.obstacles = set()
        self.path = []

    def generate_board_with_path(self):
        # Generate a game board with a guaranteed path between A and B.
        while True:
            self.generate_board()
            if self.is_path_available():
                break

    def is_path_available(self):
        # Check if a path exists between the starting point A and the destination point B.
        visited = set()
        queue = deque([self.start])

        while queue:
            current_row, current_col = queue.popleft()

            if (current_row, current_col) == self.stop:
                return True

            visited.add((current_row, current_col))

            neighbors = [
                (current_row - 1, current_col),
                (current_row + 1, current_col),
                (current_row, current_col - 1),
                (current_row, current_col + 1),
            ]

            for neighbor_row, neighbor_col in neighbors:
                if (
                    0 <= neighbor_row < self.rows
                    and 0 <= neighbor_col < self.cols
                    and (neighbor_row, neighbor_col) not in visited
                    and (neighbor_row, neighbor_col) not in self.obstacles
                ):
                    queue.append((neighbor_row, neighbor_col))

        return False

    def generate_board(self):
        # Generate a random game board with a starting point A, destination point B, and obstacles.
        self.start = (random.randint(0, self.rows - 1), random.randint(0, self.cols - 1))
        self.stop = self.generate_stop()

        self.board[self.start[0]][self.start[1]] = 'A'
        self.board[self.stop[0]][self.stop[1]] = 'B'

        self.generate_obstacles()

    def generate_stop(self):
        # Generate a random destination point B, avoiding the starting point A column.
        stop_col = random.randint(0, self.cols - 1)
        while stop_col == self.start[1]:
            stop_col = random.randint(0, self.cols - 1)
        stop_row = random.randint(0, self.rows - 1)
        return stop_row, stop_col

    def generate_obstacles(self):
        # Generate random obstacles on the board, avoiding A, B, and previous obstacles.
        for _ in range(min(self.rows * self.cols // 4, self.rows * self.cols - 2)):
            obstacle_row = random.randint(0, self.rows - 1)
            obstacle_col = random.randint(0, self.cols - 1)
            while (obstacle_row, obstacle_col) in {self.start, self.stop} or (obstacle_row, obstacle_col) in self.obstacles:
                obstacle_row = random.randint(0, self.rows - 1)
                obstacle_col = random.randint(0, self.cols - 1)
            self.obstacles.add((obstacle_row, obstacle_col))
            self.board[obstacle_row][obstacle_col] = 'X'

    def display_board(self):
        # Display the current state of the game board.
        for row in self.board:
            print(' '.join(row))
        print()

    def move(self, direction):
        # Move the player in the specified direction (up, down, left, right).
        current_row, current_col = self.start
        new_row, new_col = current_row, current_col

        if direction == 'up' and current_row > 0:
            new_row = current_row - 1
        elif direction == 'down' and current_row < self.rows - 1:
            new_row = current_row + 1
        elif direction == 'left' and current_col > 0:
            new_col = current_col - 1
        elif direction == 'right' and current_col < self.cols - 1:
            new_col = current_col + 1
        else:
            raise ValueError("Exceeded the board boundary!")

        self.handle_move(new_row, new_col)

    def handle_move(self, new_row, new_col):
        # Handle the player's move, updating the board and path.
        if (new_row, new_col) not in self.obstacles:
            self.board[self.start[0]][self.start[1]] = ' '
            self.start = (new_row, new_col)
            self.board[new_row][new_col] = 'A'
            self.path.append((new_row, new_col))
        else:
            raise ValueError("You hit an obstacle!")

    def reset_game(self):
        # Reset the game to its initial state.
        self.__init__(self.rows, self.cols)

    def is_game_over(self):
        # Check if the game is over, i.e., if the player has reached the destination point B.
        return self.start == self.stop

# Example usage:
game = SimpleGame(rows=5, cols=5)
game.generate_board_with_path()
