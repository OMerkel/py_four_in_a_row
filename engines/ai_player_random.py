#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ai Player for py-four-in-a-row: A Python implementation of
the classic Four in a Row game.
This player uses Random Choice of available moves
to determine its moves.
"""
import random
from engines.abstract_player import AbstractPlayer


class AiPlayerRandom(AbstractPlayer):
    """AI Player using Random Choice strategy for Four in a Row."""

    def __init__(self, name="Random", symbol="X", player_id: int = 1):
        """Initialize the Random Choice player.

        Args:
            name (str): Name of the player.
            symbol (str): Symbol representing the player on the board.
            player_id (int): The ID assigned to this player.
        """
        super().__init__(name, symbol, player_id=player_id)

    def get_move(self, board) -> int:
        """Select a random move from the available legal moves.

        Args:
            board (Board): The current game board.
        Returns:
            int: The selected column index for the move.
                 -1 if no legal moves are available.
        """
        legal_moves = board.get_legal_moves()
        return random.choice(legal_moves) if legal_moves else -1

    def get_most_likely_variant(self) -> list[int]:
        """Return the most likely variant of the game.

        Returns:
            List[int]: The sequence of moves representing the most
            likely variant.
        """
        # For simplicity, we return an empty list here.
        return []

    def get_likelihood_for_win(self) -> float:
        """Return the likelihood of winning from the current position.

        Returns:
            float: Likelihood of winning (0.0 to 1.0).
        """
        # This method can be implemented to return the
        # likelihood of winning.
        # For simplicity, we return 0.0 here.
        return 0.0

    def reset(self):
        """Reset any internal state of the player."""
        # No internal state to reset for this AI player.
        # pass
        return
