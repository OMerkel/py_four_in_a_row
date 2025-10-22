#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for AiPlayerRandom in py-four-in-a-row: A Python implementation of
the classic Four in a Row game.
This player uses Random Choice of available moves
to determine its moves.
"""
from engines.ai_player_random import AiPlayerRandom
from modules.board import Board


def test_ai_player_random_move():
    """Test that AiPlayerRandom selects a legal move.

    Given an AiPlayerRandom
    When get_move is called on a non-full board
    Then it should return a legal move
    """
    player = AiPlayerRandom(name="TestRandom", symbol="X", player_id=1)
    board = Board()
    legal_moves = board.get_legal_moves()
    move = player.get_move(board)
    assert move in legal_moves, "AiPlayerRandom selected an illegal move."


def test_ai_player_random_no_legal_moves():
    """Test that AiPlayerRandom returns -1 when no legal moves are available.

    Given an AiPlayerRandom
    When get_move is called on a full board
    Then it should return -1
    """
    player = AiPlayerRandom(name="TestRandom", symbol="X", player_id=1)
    board = Board()
    # Fill the board to simulate no legal moves
    for col in range(board.cols_):
        for _ in range(board.rows_):
            board.play_move(col)
    move = player.get_move(board)
    assert move == -1, ("AiPlayerRandom should return -1 when "
                        "no legal moves are available.")


def test_get_most_likely_variant_returns_empty():
    """Test get_most_likely_variant returns an empty list.

    Given an AiPlayerRandom
    When get_most_likely_variant is called
    Then it should return an empty list
    """
    player = AiPlayerRandom()
    assert not player.get_most_likely_variant()


def test_get_likelihood_for_win_returns_zero():
    """Test get_likelihood_for_win returns 0.0.

    Given an AiPlayerRandom
    When get_likelihood_for_win is called
    Then it should return 0.0
    """
    player = AiPlayerRandom()
    assert player.get_likelihood_for_win() == 0.0


def test_ai_player_random_init_custom():
    """Test AiPlayerRandom initialization with custom values.

    Given custom parameters
    When AiPlayerRandom is initialized
    Then it should have the provided name, symbol, and player_id
    """
    player = AiPlayerRandom(name="Bender", symbol="O", player_id=2)
    assert player.name_ == "Bender"
    assert player.symbol_ == "O"
    assert player.player_id_ == 2


def test_ai_player_random_multiple_instances():
    """Test multiple AiPlayerRandom instances have independent states.

    Given multiple AiPlayerRandom instances
    When they are initialized
    Then they should maintain independent states
    """
    player1 = AiPlayerRandom(name="The Gunslinger", symbol="X", player_id=1)
    player2 = AiPlayerRandom(name="Sonny", symbol="O", player_id=2)
    assert player1.name_ == "The Gunslinger"
    assert player2.name_ == "Sonny"
    assert player1.symbol_ == "X"
    assert player2.symbol_ == "O"
    assert player1.player_id_ == 1
    assert player2.player_id_ == 2
    assert player1 is not player2
    assert player1.get_move != player2.get_move
