#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_py_four_in_a_row module is testing
functions of py-four-in-a-row.
"""
from py_four_in_a_row import main, game_loop
from py_four_in_a_row import setup_players
from engines.ai_player_random import AiPlayerRandom
from engines.ai_player_uct_mcts import AiPlayerUctMcts
from engines.human_player import HumanPlayer


def test_setup_players_ai(monkeypatch):
    """Test setup_players returns two AI players when
    default names are used.

    Given default player names
    When setup_players is called
    Then it should return two AI players
    """
    # Simulate pressing Enter for both player names (defaults to AI)
    monkeypatch.setattr("builtins.input", lambda prompt: "")
    players = setup_players()
    assert len(players) == 2
    # Both should be AI players
    assert isinstance(players[0], AiPlayerUctMcts)
    assert isinstance(players[1], AiPlayerUctMcts)
    assert players[0].symbol_ == "X"
    assert players[1].symbol_ == "O"


def test_setup_players_human(monkeypatch):
    """Test setup_players returns HumanPlayer when
    custom names are given.

    Given custom player names
    When setup_players is called
    Then it should return two Human players
    """
    # Simulate custom names for both players
    names = iter(["Alice", "Bob"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(names))
    players = setup_players()
    assert len(players) == 2
    assert isinstance(players[0], HumanPlayer)
    assert isinstance(players[1], HumanPlayer)
    assert players[0].name_ == "Alice"
    assert players[1].name_ == "Bob"


def test_main_entry_point(monkeypatch):
    """Test main function with a custom game entry point.

    Given a custom game entry point
    Given that game results in a win
    When main is called
    Then it should use the provided entry point
    """
    # Simulate custom names for both players
    names = iter(["Alice", "Bob"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(names))

    def dummy_game_loop():
        return 1, [HumanPlayer(name="Alice"), HumanPlayer(name="Bob")]

    winner = main(game_entry_point=dummy_game_loop)
    assert winner == 1


def test_main_entry_point_draw(monkeypatch):
    """Test main function with a custom game entry point.

    Given a custom game entry point
    Given that game results in a draw
    When main is called
    Then it should use the provided entry point
    """
    # Simulate custom names for both players
    names = iter(["Alice", "Bob"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(names))

    def dummy_game_loop():
        return 0, [HumanPlayer(name="Alice"), HumanPlayer(name="Bob")]

    winner = main(game_entry_point=dummy_game_loop)
    assert winner == 0


def test_game_loop_draw():
    """Test game_loop function.

    Given a custom game entry point
    Given players decide randomly on their moves
    When game_loop is called
    Then it any result is possible
    """

    def dummy_setup_players():
        return [AiPlayerRandom(name="Maria", symbol="X", player_id=1),
                AiPlayerRandom(name="Maschinenmensch", symbol="O",
                               player_id=2)]
    winner, players = game_loop(setup=dummy_setup_players)
    assert winner in [0, 1, 2]
    assert len(players) == 2
