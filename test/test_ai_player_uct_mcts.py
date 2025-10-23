#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_ai_player_uct_mcts module is testing functions of ai_player_uct_mcts.
"""
from engines.ai_player_uct_mcts import AiPlayerUctMcts
from modules.board import Board


def test_ai_player_uct_mcts():
    """Test AiPlayerUctMcts initialization.

    Given no parameters
    When AiPlayerUctMcts is initialized
    Then it should have default name, symbol, and player_id
    """
    player = AiPlayerUctMcts()
    assert player is not None
    assert player.name_ == "UCT_MCTS"
    assert player.symbol_ == "X"
    assert player.player_id_ == 1


def test_get_likelihood_for_win_returns_zero():
    """Test get_likelihood_for_win returns 0.0.

    Given an AiPlayerUctMcts
    When get_likelihood_for_win is called
    Then it should return 0.0
    """
    player = AiPlayerUctMcts()
    assert player.get_likelihood_for_win() == 0.0


def test_get_most_likely_variant_returns_empty():
    """Test get_most_likely_variant returns an empty list.

    Given an AiPlayerUctMcts
    When get_most_likely_variant is called
    Then it should return an empty list
    """
    player = AiPlayerUctMcts()
    assert not player.get_most_likely_variant()


def test_ai_player_uct_mcts_custom():
    """Test AiPlayerUctMcts initialization with custom values.

    Given custom parameters
    When AiPlayerUctMcts is initialized
    Then it should have the provided name, symbol, and player_id
    """
    player = AiPlayerUctMcts(name="Ava", symbol="O", player_id=2)
    assert player.name_ == "Ava"
    assert player.symbol_ == "O"
    assert player.player_id_ == 2


def test_ai_player_uct_mcts_multiple_instances():
    """Test multiple AiPlayerUctMcts instances have independent states.

    Given multiple AiPlayerUctMcts instances
    When they are initialized
    Then they should maintain independent states
    """
    player1 = AiPlayerUctMcts(name="Player1", symbol="X", player_id=1)
    player2 = AiPlayerUctMcts(name="Player2", symbol="O", player_id=2)
    assert player1.name_ == "Player1"
    assert player2.name_ == "Player2"
    assert player1.symbol_ != player2.symbol_
    assert player1.player_id_ != player2.player_id_


def test_reset_does_nothing():
    """Test reset method does nothing.

    Given an AiPlayerUctMcts
    When reset is called
    Then it should not change any attributes
    """
    player = AiPlayerUctMcts()
    assert player.reset() is None


def test_ai_player_uct_mcts_play_move():
    """Test AiPlayerUctMcts can play a move.

    Given an AiPlayerUctMcts and a game state
    When get_move is called
    Then it should return a valid move
    """
    player = AiPlayerUctMcts()
    # Mock a simple game state with legal moves

    class MockGameState:
        """A mock game state for testing."""

        def get_legal_moves(self):
            """Get a list of all legal moves."""
            return [0, 1, 2, 3, 4, 5, 6]

        def play_move(self, move):
            """Play a move in the game state."""
            print(f"Playing: {move=}")

        def is_game_over(self):
            """Check if the game is over."""
            return True

        def get_winner(self):
            """Get the winner of the game."""
            return None

    state = MockGameState()
    move = player.get_move(state)
    assert move in state.get_legal_moves()


def test_ai_player_uct_mcts_immediate_win() -> None:
    """Test AiPlayerUctMcts simulation logic for immediate win.

    Given an AiPlayerUctMcts and a game state
    Given an immediate winning move possible
    When a simulation is run
    Then it should prioritize immediate wins
    """
    player = AiPlayerUctMcts(player_id=1)

    board: Board = Board()
    board.players = [
        type("Player", (), {"name_": "Player 1", "symbol_": "X"}),
        type("Player", (), {"name_": "Player 2", "symbol_": "O"})
    ]

    # Set up a board state where player 1 can win immediately
    board.play_move(0)  # Player 1
    board.play_move(1)  # Player 2
    board.play_move(1)  # Player 1
    board.play_move(2)  # Player 2
    board.play_move(3)  # Player 1
    board.play_move(2)  # Player 2
    board.play_move(2)  # Player 1
    board.play_move(3)  # Player 2
    board.play_move(4)  # Player 1
    board.play_move(3)  # Player 2
    # print(board)
    # Now player 1 can win by playing in column 3
    move = player.get_move(board)
    assert move == 3  # Expecting the winning move


def test_ai_player_uct_mcts_immediate_block() -> None:
    """Test AiPlayerUctMcts simulation logic for immediate block.

    Given an AiPlayerUctMcts and a game state
    Given an immediate blocking move possible
    When a simulation is run
    Then it should prioritize blocking opponent's immediate wins
    """
    player = AiPlayerUctMcts(player_id=2, symbol="O")

    board: Board = Board()
    board.players = [
        type("Player", (), {"name_": "Player 1", "symbol_": "X"}),
        type("Player", (), {"name_": "Player 2", "symbol_": "O"})
    ]

    # Set up a board state where player 1 can win immediately
    board.play_move(0)  # Player 1
    board.play_move(1)  # Player 2
    board.play_move(1)  # Player 1
    board.play_move(2)  # Player 2
    board.play_move(2)  # Player 1
    board.play_move(4)  # Player 2
    board.play_move(2)  # Player 1
    board.play_move(4)  # Player 2
    board.play_move(3)  # Player 1
    board.play_move(3)  # Player 2
    board.play_move(3)  # Player 1
    print(board)
    # Now player 1 can win by playing in column 3
    move = player.get_move(board)
    assert move == 3  # Expecting the blocking move
    assert move in board.get_legal_moves()


def test_ai_player_uct_mcts_block_obvious_situations() -> None:
    """Test AiPlayerUctMcts blocks obvious winning situations.

    Given an AiPlayerUctMcts and a game state
    Given an obvious winning move preparation for the opponent
    When get_move is called
    Then it should block the opponent's winning move preparation
    """
    player = AiPlayerUctMcts(player_id=2, symbol="O", simulations=7000)

    board: Board = Board()
    board.players = [
        type("Player", (), {"name_": "Player 1", "symbol_": "X"}),
        type("Player", (), {"name_": "Player 2", "symbol_": "O"})
    ]

    # Set up a board state where player 1 can win immediately
    board.play_move(3)  # Player 1
    board.play_move(3)  # Player 2
    board.play_move(1)  # Player 1
    # print(board)
    # Now player 2 should go for [0, 2, 4] to block
    # player 1's winning move preparation
    move = player.get_move(board)
    assert move in [0, 2, 4]  # Expecting the blocking move


def test_ai_player_uct_mcts_find_winning_move() -> None:
    """Test AiPlayerUctMcts finds winning move to force a win.

    Given an AiPlayerUctMcts
    Given a possible move to force a win
    When get_move is called
    Then it should find and play the winning move preparation
    """
    player = AiPlayerUctMcts(player_id=1, symbol="X", simulations=2000)

    board: Board = Board()
    board.players = [
        type("Player", (), {"name_": "Player 1", "symbol_": "X"}),
        type("Player", (), {"name_": "Player 2", "symbol_": "O"})
    ]

    # Set up board state
    board.play_move(1)  # Player 1
    board.play_move(1)  # Player 2
    board.play_move(3)  # Player 1
    board.play_move(3)  # Player 2
    # print(board)
    # Now player 1 can win by playing in column 2
    move = player.get_move(board)
    assert move == 2  # Expecting the winning move preparation
