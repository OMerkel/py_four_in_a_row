#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_human_player module is testing functions of human_player.
"""
from engines.human_player import HumanPlayer


class DummyBoard:
    """A dummy board class for testing purposes."""
    def __init__(self, legal_moves, cols):
        """Initialize the dummy board with legal moves."""
        self._legal_moves = legal_moves
        self.cols_ = cols

    def get_legal_moves(self):
        """Return the list of legal moves."""
        return self._legal_moves


def test_human_player_init_defaults():
    """Test HumanPlayer initialization with default values.

    Given no parameters
    When HumanPlayer is initialized
    Then it should have default name, symbol, and player_id
    """
    player = HumanPlayer()
    assert player.name_ == "Human"
    assert player.symbol_ == "O"
    assert player.player_id_ == 1


def test_human_player_init_custom():
    """Test HumanPlayer initialization with custom values.

    Given custom parameters
    When HumanPlayer is initialized
    Then it should have the provided name, symbol, and player_id
    """
    player = HumanPlayer(name="Alice", symbol="X", player_id=2)
    assert player.name_ == "Alice"
    assert player.symbol_ == "X"
    assert player.player_id_ == 2


def test_get_most_likely_variant_returns_empty():
    """Test get_most_likely_variant returns an empty list.

    Given a HumanPlayer
    When get_most_likely_variant is called
    Then it should return an empty list
    """
    player = HumanPlayer()
    assert not player.get_most_likely_variant()


def test_get_likelihood_for_win_returns_zero():
    """Test get_likelihood_for_win returns 0.0.

    Given a HumanPlayer
    When get_likelihood_for_win is called
    Then it should return 0.0
    """
    player = HumanPlayer()
    assert player.get_likelihood_for_win() == 0.0


def test_reset_does_nothing():
    """Test reset method does nothing.

    Given a HumanPlayer
    When reset is called
    Then it should not change any attributes
    """
    player = HumanPlayer()
    assert player.reset() is None


def test_get_move_valid(monkeypatch):
    """Test get_move with a valid input.

    Given a HumanPlayer and a valid move input
    When get_move is called
    Then it should return the valid move
    """
    board = DummyBoard([0, 2, 3], 7)
    player = HumanPlayer(name="Tester")
    inputs = iter(["5", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    move = player.get_move(board)
    assert move == 2


def test_get_move_invalid_then_valid(monkeypatch):
    """Test get_move with invalid inputs followed by a valid input.

    Given a HumanPlayer and invalid move inputs followed by a valid one
    When get_move is called
    Then it should return the valid move after rejecting invalid ones
    """
    board = DummyBoard([1, 4], 7)
    player = HumanPlayer(name="Tester")
    inputs = iter(["a", "3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    move = player.get_move(board)
    assert move == 4
