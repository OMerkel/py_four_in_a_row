#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
human_player module implements a human player for py-four-in-a-row.
"""
from engines.abstract_player import AbstractPlayer


class HumanPlayer(AbstractPlayer):
    """Human player for the Four in a Row game."""

    command = {
        100: "dump history",
    }

    def __init__(self, name="Human", symbol="O", player_id: int = 1):
        """Initialize the human player.
        Args:
            name (str): Name of the player.
        """
        super().__init__(name, symbol, player_id=player_id)

    def get_move(self, board) -> int:
        """Get the human player's move.
        Args:
            board (Board): The current game board.
        Returns:
            int: The selected column index for the move.
        """
        move = -1
        while (move not in board.get_legal_moves()) and \
              (move not in self.command):
            try:
                move_input = input(
                    f"{self.name_} ({self.symbol_}), "
                    f"enter your move (0-{board.cols_-1}): "
                )
                move = int(move_input)
            except ValueError:
                continue
        return move

    def reset(self):
        """Reset any internal state of the player."""
        # No internal state to reset for human player
        # pass
        return

    def get_most_likely_variant(self):
        """Return the most likely variant of the game.
        For a human player, this is not applicable.
        Returns:
            list[int]: Empty list as human players do not predict variants.
        """
        return []

    def get_likelihood_for_win(self):
        """Return the likelihood of winning from the current position.
        For a human player, this is not applicable.
        Returns:
            float: 0.0 as human players do not calculate win likelihood.
        """
        return 0.0
