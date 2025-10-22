#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abstract base class for players in the py-four-in-a-row game engine.

"""
from abc import ABC, abstractmethod


class AbstractPlayer(ABC):
    """Abstract base class for a player in the
    py-four-in-a-row game engine."""
    def __init__(self, name, symbol, player_id: int = 1):
        """Initialize the player with a name.
        Args:
            name (str): The name of the player.
        """
        self.name_ = name
        self.symbol_ = symbol
        self.player_id_ = player_id
        self.reset()
        print(f"Player {self.name_} joined the game.")

    def set_player_id(self, player_id: int):
        """Set the player ID for this AI.
        Args:
            player_id (int): The ID assigned to this player.
        """
        self.player_id_ = player_id

    @abstractmethod
    def reset(self):
        """Reset any internal state of the player."""
        # pass

    @abstractmethod
    def get_move(self, board):
        """Return the move to be played on the given board.

        Args:
            board (Board): The current game board.
        Returns:
            int: The column index where the player wants to play.
        """
        # pass

    @abstractmethod
    def get_most_likely_variant(self):
        """Return the most likely variant of the game.
        The variant is represented as a list of moves from the
        current position.
        As such it can be used to predict the likely course of the game.

        Returns:
            list[int]: List of column indices representing the moves.
        """
        # pass

    @abstractmethod
    def get_likelihood_for_win(self):
        """Return a float between 0 and 1 representing the likelihood
        of winning from the current position.

        Returns:
            float: Likelihood of winning (0.0 to 1.0)."""
        # pass


# --- IGNORE ---
if __name__ == "__main__":
    print("This is the AbstractPlayer module.")
# --- IGNORE ---
