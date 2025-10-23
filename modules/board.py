#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Board module for py-four-in-a-row:
A Python implementation of the classic Four in a Row game.

This module defines the Board class, which represents the game board
and provides methods to manipulate and query the board state.
"""


class Board:
    """Class representing the game board for Four in a Row."""

    def __init__(self, rows=6, cols=7, current_player=1,
                 players=None):
        """Initialize the board with given rows and columns."""
        self.rows_ = rows
        self.cols_ = cols
        self.grid_ = [[0 for _ in range(cols)] for _ in range(rows)]
        self.last_move_ = {"row": None, "col": None, "player": None}
        self.history_ = []
        self.current_player_ = current_player
        self.players = players

    def get_legal_moves(self):
        """Get a list of all legal moves (i.e., columns that
        are not full).

        Returns:
            list[int]: List of column indices where a move can be played."""
        if self.is_full() or self.check_winner() != 0:
            return []
        return [c for c in range(self.cols_) if self.grid_[0][c] == 0]

    def is_legal_move(self, col):
        """Check if a move in the given column is legal.

        Args:
            col (int): The column index to check.

        Returns:
            bool: True if the move is legal,
                  False otherwise.
        """
        if col < 0 or col >= self.cols_:
            return False
        if self.grid_[0][col] != 0:
            return False
        return True

    def is_game_over(self):
        """Check if the game is over (win or draw).

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.check_winner() != 0 or self.is_full()

    def reset(self):
        """Reset the board to the initial empty state."""
        self.grid_ = [[0 for _ in range(self.cols_)]
                      for _ in range(self.rows_)]
        self.last_move_ = None
        self.history_ = []
        self.current_player_ = 1

    def undo_move(self):
        """Undo the last move played on the board.

        Returns:
            bool: True if a move was undone,
                  False if there was no move to undo.
        """
        if not self.history_:
            return False
        history_entry = self.history_.pop()
        self.grid_[history_entry["row"]][history_entry["col"]] = 0
        self.current_player_ = history_entry["player"]
        self.last_move_ = self.history_[-1] if self.history_ else None
        return True

    def play_move(self, col):
        """Play a move for the given player in the specified column.

        Args:
            col (int): The column index where the player wants to play.
        Returns:
            bool: True if the move was successful, False if the column is full.
        """
        for r in reversed(range(self.rows_)):
            if self.grid_[r][col] == 0:
                self.grid_[r][col] = self.current_player_
                self.last_move_ = {
                        "row": r,
                        "col": col,
                        "player": self.current_player_
                    }
                self.history_.append(self.last_move_)
                self.current_player_ = 2 if self.current_player_ == 1 else 1
                return True
        return False

    def is_full(self):
        """Check if the board is full."""
        return all(self.grid_[0][c] != 0 for c in range(self.cols_))

    def check_winner(self) -> int:
        """Check for a winner.

        Returns:
            int: The player number (1 or 2) if there is a winner, 0 otherwise.
        """
        # Check horizontal, vertical, and diagonal for a winner
        for r in range(self.rows_):
            for c in range(self.cols_ - 3):
                if self.grid_[r][c] != 0 and all(
                        self.grid_[r][c + i] == self.grid_[r][c]
                        for i in range(4)):
                    return self.grid_[r][c]

        for c in range(self.cols_):
            for r in range(self.rows_ - 3):
                if self.grid_[r][c] != 0 and all(
                        self.grid_[r + i][c] == self.grid_[r][c]
                        for i in range(4)):
                    return self.grid_[r][c]

        for r in range(self.rows_ - 3):
            for c in range(self.cols_ - 3):
                if self.grid_[r][c] != 0 and all(
                        self.grid_[r + i][c + i] == self.grid_[r][c]
                        for i in range(4)):
                    return self.grid_[r][c]

        for r in range(3, self.rows_):
            for c in range(self.cols_ - 3):
                if self.grid_[r][c] != 0 and all(
                        self.grid_[r - i][c + i] == self.grid_[r][c]
                        for i in range(4)):
                    return self.grid_[r][c]

        return 0  # No winner yet

    def get_winner(self) -> int:
        """Get the winner of the game.

        Returns:
            int: The player number (1 or 2) if there is a winner, 0 otherwise.
        """
        return self.check_winner()

    def get_current_player(self) -> int:
        """Get the current player to move.

        Returns:
            int: The current player number (1 or 2).
        """
        return self.current_player_

    def dump_history(self):
        """Dump the history of moves played."""
        history_dump = []
        for i, move in enumerate(self.history_):
            player_name = self.players[move["player"] - 1].name_
            history_dump.append(f"board.play_move({move['col']})  "
                                f"# Move {i + 1}: Player "
                                f"{player_name} played at "
                                f"(row={move['row']}, col={move['col']})")
        return history_dump

    def __repr__(self):
        """String representation of the board."""
        symbols = {0: ".",
                   1: self.players[0].symbol_,
                   2: self.players[1].symbol_}
        rows = [" | ".join(symbols[cell] for cell in row)
                for row in self.grid_]
        rows.append("--+---+---+---+---+---+--")
        rows.append("0 | 1 | 2 | 3 | 4 | 5 | 6")
        name = self.players[self.current_player_ - 1].name_
        symbol = self.players[self.current_player_ - 1].symbol_
        if not self.is_game_over():
            rows.append(f"Current player: {name} "
                        f"({self.current_player_}, {symbol})")
        if self.history_:
            rows.append(f"Last move: {self.last_move_}")
        return "\n".join(rows)


if __name__ == "__main__":  # pragma: no cover
    print("This is the Board module.")
