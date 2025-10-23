#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_illegal_move_handling module is testing
the handling of illegal moves and commands in the game loop.
"""
import pytest
from engines.human_player import HumanPlayer
from py_four_in_a_row import game_loop


class DummyHuman(HumanPlayer):
    """Dummy player for testing purposes."""
    # Simulate a sequence of moves, including illegal and command moves
    def __init__(self, moves, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._moves = iter(moves)

    def get_move(self, board):
        return next(self._moves)


@pytest.mark.parametrize("illegal_move, command_dump_history", [
    (99, 100),
])
def test_illegal_and_command_moves(monkeypatch, illegal_move,
                                   command_dump_history, capsys):
    """Test that illegal moves are handled properly
    and that command moves work as expected."""
    # Setup: Player 1 tries illegal move, then command move, then a legal move
    legal_move = 0
    moves = [illegal_move, command_dump_history, legal_move, legal_move,
             legal_move, legal_move, legal_move]

    def dummy_setup():
        p1 = DummyHuman([6]*4, name="TestDummy 1", symbol="X", player_id=1)
        p2 = DummyHuman(moves, name="TestDummy 2", symbol="O", player_id=2)
        return [p1, p2]
    winner, players = game_loop(setup=dummy_setup)
    out = capsys.readouterr().out
    assert f"Illegal move: {illegal_move}. Try again." in out
    assert "Game over!" in out
    assert winner == 1
    assert isinstance(players[0], DummyHuman)
    assert isinstance(players[1], DummyHuman)
    assert isinstance(monkeypatch, object)
    # Check that the command move triggers the
    # board history print (should not error)
    # (board.dump_history() output is printed)
    assert any("Last move" in line or "Current player" in line
               for line in out.splitlines())
    assert ("board.play_move(6)  # Move 1: "
            "Player TestDummy 1 played at (row=5, col=6)") in out
    assert "Illegal move: 99. Try again." in out
    # print(out)
