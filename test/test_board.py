#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_board module is testing the Board class of py-four-in-a-row.
"""
import unittest
from modules.board import Board


class TestBoard(unittest.TestCase):
    """Unit tests for the Board class."""

    def setUp(self):
        """Fixture setup before each test method."""
        self.board = Board()

    def test_initialization(self):
        """Test board initialization.

        Given a new Board instance
        When the board is initialized
        Then the board should have the correct number of rows and columns
        And all cells should be empty (0)
        """
        self.assertEqual(self.board.rows_, 6)
        self.assertEqual(self.board.cols_, 7)
        self.assertEqual(self.board.grid_, [[0 for _ in range(7)]
                                            for _ in range(6)])

    def test_get_legal_moves(self):
        """Test getting legal moves.

        Given a new Board instance
        When get_legal_moves is called
        Then it should return a list of all valid column indices
        """
        self.assertEqual(self.board.get_legal_moves(), [0, 1, 2, 3, 4, 5, 6])
        for _ in range(6):
            self.board.play_move(2)
        self.assertEqual(self.board.get_legal_moves(), [0, 1, 3, 4, 5, 6])

    def test_play_move(self):
        """Test playing a move.

        Given a new Board instance
        When play_move is called with a valid column
        Then the move should be played in the lowest available row
        """
        self.assertTrue(self.board.play_move(0))
        self.assertEqual(self.board.grid_[5][0], 1)
        self.assertTrue(self.board.play_move(0))
        self.assertEqual(self.board.grid_[5][0], 1)
        self.assertEqual(self.board.grid_[4][0], 2)
        self.assertTrue(self.board.play_move(0))
        self.assertEqual(self.board.grid_[3][0], 1)

    def test_play_move_on_full_column(self):
        """Test playing a move on a full column.

        Given a new Board instance
        When play_move is called with a full column
        Then the move should not be played and return False
        """
        for _ in range(3):
            self.assertTrue(self.board.play_move(1))
            self.assertTrue(self.board.play_move(1))
        self.assertEqual(self.board.grid_[0][1], 2)
        self.assertFalse(self.board.play_move(1))
        self.assertFalse(self.board.play_move(1))

    def test_is_full(self):
        """Test if the board is full.

        Given a new Board instance
        When is_full is called
        Then it should return False
        When all columns are filled
        Then it should return True
        """
        self.assertFalse(self.board.is_full())
        for col in range(7):
            for _ in range(6):
                self.board.play_move(col)
        self.assertTrue(self.board.is_full())

    def test_check_winner_horizontal(self):
        """Test checking for a winner in horizontal direction.

        Given a new Board instance
        When check_winner is called with no winning condition
        Then it should return 0
        When a player has four in a row horizontally
        Then it should return that player's number
        """
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(0)
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(0)
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(1)
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(1)
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(2)
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(2)
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(3)
        self.assertEqual(self.board.check_winner(), 1)

    def test_check_winner_vertical(self):
        """Test checking for a winner in vertical direction.

        Given a new Board instance
        When a player has four in a row vertically
        Then it should return that player's number
        """
        for _ in range(3):
            self.assertEqual(self.board.check_winner(), 0)
            self.board.play_move(0)
            self.assertEqual(self.board.check_winner(), 0)
            self.board.play_move(1)
        self.board.play_move(0)
        self.assertEqual(self.board.check_winner(), 1)

    def test_check_winner_diagonal_bottom_left_to_top_right(self):
        """Test checking for a winner in diagonal direction.

        Given a new Board instance
        When a player has four in a row diagonally
        Then it should return that player's number
        """
        self.assertEqual(self.board.check_winner(), 0)
        # Create a diagonal from bottom-left to top-right for player 1
        self.board.play_move(0)  # Row 5, Col 0
        self.board.play_move(1)
        self.board.play_move(1)  # Row 4, Col 1
        self.board.play_move(2)
        self.board.play_move(2)  # Row 4, Col 2
        self.board.play_move(3)
        self.board.play_move(2)  # Row 3, Col 2
        self.board.play_move(3)
        self.board.play_move(3)  # Row 3, Col 3
        self.board.play_move(0)
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(3)  # Row 2, Col 3
        # print(self.board)  # For debugging purposes
        self.assertEqual(self.board.check_winner(), 1)

    def test_check_winner_diagonal_top_left_to_bottom_right(self):
        """Test checking for a winner in diagonal direction.

        Given a new Board instance
        When a player has four in a row diagonally
        Then it should return that player's number
        """
        self.assertEqual(self.board.check_winner(), 0)
        # Create a diagonal from top-left to bottom-right for player 1
        self.board.play_move(6)  # Row 5, Col 6
        self.board.play_move(5)
        self.board.play_move(5)  # Row 4, Col 5
        self.board.play_move(4)
        self.board.play_move(4)  # Row 4, Col 4
        self.board.play_move(3)
        self.board.play_move(4)  # Row 3, Col 4
        self.board.play_move(3)
        self.board.play_move(3)  # Row 3, Col 3
        self.board.play_move(6)
        self.assertEqual(self.board.check_winner(), 0)
        self.board.play_move(3)  # Row 2, Col 3
        # print(self.board)  # For debugging purposes
        self.assertEqual(self.board.check_winner(), 1)

    def test_board_repr_empty(self):
        """Test the string representation of an empty board.

        Given a new Board instance
        When repr is called
        Then it should return the correct string of the empty board
        """
        board = Board(current_player=1)
        board.players = [
            type("Player", (), {"name_": "Player 1", "symbol_": "X"}),
            type("Player", (), {"name_": "Player 2", "symbol_": "O"})
        ]
        expected = "\n".join([". | . | . | . | . | . | ."] * 6)
        expected += "\n--+---+---+---+---+---+--\n"
        expected += "0 | 1 | 2 | 3 | 4 | 5 | 6"
        expected += "\nCurrent player: Player 1 (1, X)"
        assert repr(board) == expected

    def test_board_repr_after_moves(self):
        """Test the string representation of the board after some moves.

        Given a Board instance with some moves played
        When repr is called
        Then it should return the correct string representation of the board
        """
        board = Board()
        board.players = [
            type("Player", (), {"name_": "Player 1", "symbol_": "X"}),
            type("Player", (), {"name_": "Player 2", "symbol_": "O"})
        ]
        board.play_move(0)
        board.play_move(1)
        board.play_move(0)
        expected_rows = [
            ". | . | . | . | . | . | .",
            ". | . | . | . | . | . | .",
            ". | . | . | . | . | . | .",
            ". | . | . | . | . | . | .",
            "X | . | . | . | . | . | .",
            "X | O | . | . | . | . | .",
            "--+---+---+---+---+---+--",
            "0 | 1 | 2 | 3 | 4 | 5 | 6"
        ]
        expected = "\n".join(expected_rows)
        expected += "\nCurrent player: Player 2 (2, O)"
        expected += f"\nLast move: {board.last_move_}"
        actual = repr(board)
        assert actual == expected

    def test_is_legal_move_after_game_over(self):
        """Test that no legal moves are available after game over.

        Given a Board instance where the game is over
        When get_legal_moves is called
        Then it should return an empty list
        """
        # Simulate a winning condition for player 1
        for col in range(4):
            self.board.play_move(col)  # Player 1
            if col < 3:
                self.board.play_move(col)  # Player 2
        self.assertEqual(self.board.check_winner(), 1)
        self.assertEqual(self.board.get_legal_moves(), [])

    def test_is_legal_move_after_board_full(self):
        """Test that no legal moves are available after board is full.

        Given a Board instance that is full
        When get_legal_moves is called
        Then it should return an empty list
        """
        for col in range(7):
            for _ in range(6):
                self.board.play_move(col)
        self.assertTrue(self.board.is_full())
        self.assertEqual(self.board.get_legal_moves(), [])

    def test_is_legal_move_normal(self):
        """Test that legal moves are available in a normal game state.

        Given a new Board instance
        When is_legal_moves is called with a column index
        Then it should return True for legal columns
        And False for illegal columns
        """
        self.assertTrue(self.board.is_legal_move(0))
        self.assertTrue(self.board.is_legal_move(1))
        self.assertFalse(self.board.is_legal_move(7))

    def test_is_legal_move_partial(self):
        """Test that legal moves are available in a partially filled board.

        Given a Board instance with some moves played
        When get_legal_moves is called
        Then it should return the correct list of legal column indices
        """
        self.board.play_move(0)
        self.board.play_move(1)
        self.board.play_move(0)
        self.assertEqual(self.board.get_legal_moves(), [0, 1, 2, 3, 4, 5, 6])

    def test_is_legal_move_with_invalid_column(self):
        """Test that an invalid column returns False for is_legal_move.

        Given a Board instance
        When is_legal_move is called with an invalid column
        Then it should return False
        """
        self.assertFalse(self.board.is_legal_move(-1))
        self.assertFalse(self.board.is_legal_move(7))

    def test_is_legal_move_on_full_column(self):
        """Test that a full column returns False for is_legal_move.

        Given a Board instance with a full column
        When is_legal_move is called on that column
        Then it should return False
        """
        for _ in range(6):
            self.board.play_move(3)
        self.assertFalse(self.board.is_legal_move(3))

    def test_reset_board(self):
        """Test resetting the board.

        Given a Board instance with some moves played
        When reset is called
        Then the board should be empty
        And current player should be reset to 1
        """
        self.board.play_move(0)
        self.board.play_move(1)
        self.board.reset()
        self.assertEqual(self.board.grid_, [[0 for _ in range(7)]
                                            for _ in range(6)])
        self.assertEqual(self.board.current_player_, 1)

    def test_undo_move(self):
        """Test undoing the last move.

        Given a Board instance with some moves played
        When undo_move is called
        Then the last move should be removed
        And current player should switch back
        """
        self.board.play_move(0)  # Player 1
        self.board.play_move(1)  # Player 2
        self.board.undo_move()
        self.assertEqual(self.board.grid_[5][1], 0)
        self.assertEqual(self.board.current_player_, 2)
        self.board.undo_move()
        self.assertEqual(self.board.grid_[5][0], 0)
        self.assertEqual(self.board.current_player_, 1)

    def test_undo_move_empty_history(self):
        """Test undoing a move when no history exists.

        Given a Board instance with no moves played
        When undo_move is called
        Then it should return False
        """
        self.assertFalse(self.board.undo_move())

    def test_undo_move_multiple(self):
        """Test undoing multiple moves.

        Given a Board instance with multiple moves played
        When undo_move is called multiple times
        Then the moves should be undone in reverse order
        """
        moves = [0, 1, 2, 3]
        for move in moves:
            self.board.play_move(move)
        for move in reversed(moves):
            self.board.undo_move()
            col = move
            for row in range(6):
                self.assertEqual(self.board.grid_[row][col], 0)
            for c in range(col):
                self.assertNotEqual(self.board.grid_[5][c], 0)

    def test_undo_move_switch_player(self):
        """Test that undo_move switches the current player back.

        Given a Board instance with some moves played
        When undo_move is called
        Then the current player should switch back to the previous player
        """
        self.board.play_move(0)  # Player 1
        self.assertEqual(self.board.current_player_, 2)
        self.board.play_move(1)  # Player 2
        self.assertEqual(self.board.current_player_, 1)
        self.board.undo_move()
        self.assertEqual(self.board.current_player_, 2)
        self.board.undo_move()
        self.assertEqual(self.board.current_player_, 1)

    def test_undo_move_last_move_update(self):
        """Test that undo_move updates the last_move attribute.

        Given a Board instance with some moves played
        When undo_move is called
        Then the last_move attribute should be updated correctly
        """
        self.board.play_move(0)  # Player 1
        first_move = self.board.last_move_.copy()
        self.board.play_move(1)  # Player 2
        self.board.undo_move()
        self.assertEqual(self.board.last_move_, first_move)
        self.board.undo_move()
        self.assertIsNone(self.board.last_move_)

    def test_get_winner_no_winner(self):
        """Test get_winner when there is no winner.

        Given a new Board instance
        When get_winner is called
        Then it should return 0
        """
        self.assertEqual(self.board.get_winner(), 0)

    def test_get_winner_with_winner(self):
        """Test get_winner when there is a winner.

        Given a Board instance with a winning condition
        When get_winner is called
        Then it should return the winning player's number
        """
        for col in range(4):
            self.board.play_move(col)  # Player 1
            if col < 3:
                self.board.play_move(col)  # Player 2
        self.assertEqual(self.board.get_winner(), 1)

    def test_get_current_player(self):
        """Test get_current_player method.

        Given a Board instance
        When get_current_player is called
        Then it should return the correct current player number
        """
        self.assertEqual(self.board.get_current_player(), 1)
        self.board.play_move(0)
        self.assertEqual(self.board.get_current_player(), 2)
        self.board.play_move(1)
        self.assertEqual(self.board.get_current_player(), 1)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
