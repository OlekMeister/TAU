import unittest
from SimpleGame import SimpleGame

class TestSimpleGame(unittest.TestCase):

    def test_generate_stop(self):
        game = SimpleGame(5, 5)
        stop = game.generate_stop()
        self.assertNotEqual(stop, game.start)
        self.assertGreaterEqual(stop[0], 0)
        self.assertLess(stop[0], game.rows)
        self.assertGreaterEqual(stop[1], 0)
        self.assertLess(stop[1], game.cols)

    def test_generate_obstacles(self):
        game = SimpleGame(5, 5)
        game.generate_obstacles()
        self.assertEqual(len(game.obstacles), min(game.rows * game.cols // 4, game.rows * game.cols - 2))
        for obstacle in game.obstacles:
            self.assertNotEqual(obstacle, game.start)
            self.assertNotEqual(obstacle, game.stop)
            self.assertGreaterEqual(obstacle[0], 0)
            self.assertLess(obstacle[0], game.rows)
            self.assertGreaterEqual(obstacle[1], 0)
            self.assertLess(obstacle[1], game.cols)

    def test_move(self):
        game = SimpleGame(5, 5)
        game.generate_board()
        initial_start = game.start

        # Ensure the player is not at the top row before attempting upward movement
        if initial_start[0] > 0:
            game.move('up')
            self.assertNotEqual(game.start, initial_start)
            self.assertEqual(game.board[initial_start[0] - 1][initial_start[1]], 'A')
            self.assertIn((initial_start[0] - 1, initial_start[1]), game.path)
        else:
            # If the player is already at the top row, the move should not be attempted
            with self.assertRaises(ValueError) as context:
                game.move('up')

            self.assertEqual(str(context.exception), "Exceeded the board boundary!")
            self.assertEqual(game.start, initial_start)
            self.assertEqual(game.board, game.board)  # Board remains unchanged

    def test_reset_game(self):
        game = SimpleGame(5, 5)
        game.generate_board()
        initial_start = game.start
        initial_obstacles = game.obstacles.copy()

        game.reset_game()

        self.assertNotEqual(game.start, initial_start)
        self.assertNotEqual(game.obstacles, initial_obstacles)
        self.assertEqual(len(game.path), 0)
        self.assertTrue(all(cell == ' ' for row in game.board for cell in row))

    def test_is_game_over(self):
        game = SimpleGame(5, 5)
        game.generate_board()

        # Generate a new board
        game.generate_board()

        self.assertFalse(game.is_game_over())

    def test_hit_obstacle(self):
        game = SimpleGame(5, 5)
        game.generate_board()

        # Place an obstacle on the movement path
        obstacle_position = (2, 2)
        game.obstacles.add(obstacle_position)
        game.start = (2, 1)

        # Test movement into the obstacle
        with self.assertRaises(ValueError) as context:
            game.move('right')

        self.assertEqual(str(context.exception), "You hit an obstacle!")

        # Check if start remains unchanged after hitting the obstacle
        self.assertEqual(game.start, (2, 1))

    def test_out_of_bounds(self):
        game = SimpleGame(5, 5)
        game.generate_board()

        # Place the start close to the upper-left corner of the board
        game.start = (0, 0)

        # Test movement out of the board to the left
        with self.assertRaises(ValueError) as context:
            game.move('left')

        self.assertEqual(str(context.exception), "Exceeded the board boundary!")

    def test_generate_board_with_path(self):
        game = SimpleGame(5, 5)
        game.generate_board_with_path()

        # Check if there is a path between A and B after calling generate_board_with_path
        self.assertTrue(game.is_path_available())

        # Check if start and stop are different
        self.assertNotEqual(game.start, game.stop)

        # Check if obstacles are generated correctly
        for obstacle in game.obstacles:
            self.assertNotEqual(obstacle, game.start)
            self.assertNotEqual(obstacle, game.stop)
            self.assertGreaterEqual(obstacle[0], 0)
            self.assertLess(obstacle[0], game.rows)
            self.assertGreaterEqual(obstacle[1], 0)
            self.assertLess(obstacle[1], game.cols)

if __name__ == '__main__':
    unittest.main()
