#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
py-four-in-a-row: A Python implementation of the classic Four in a Row game.
"""
import random
from engines.abstract_player import AbstractPlayer
from engines.ai_player_uct_mcts import AiPlayerUctMcts
from engines.human_player import HumanPlayer
from modules.board import Board


def setup_players() -> list[AbstractPlayer]:
    """Setup players for the game."""
    player1_name: str = input("Enter name for Player 1: ") or "HAL9000"
    player1: AbstractPlayer = AiPlayerUctMcts(
        name=player1_name, symbol="X",
        simulations=400, player_id=1
    ) if player1_name == "HAL9000" else HumanPlayer(
        name=player1_name, symbol="X",
        player_id=1
    )
    player1.reset()

    player2_name: str = input("Enter name for Player 2: ") or "Dalek"
    player2: AbstractPlayer = AiPlayerUctMcts(
        name=player2_name, symbol="O",
        simulations=400, player_id=2
    ) if player2_name == "Dalek" else HumanPlayer(
        name=player2_name, symbol="O",
        player_id=2
    )
    player2.reset()
    return [player1, player2]


def main() -> int:
    """Main entry point for the py-four-in-a-row application."""
    print("Hello from py-four-in-a-row!")
    players = setup_players()
    board = Board(current_player=1, players=players)
    print(board)

    end_of_game: bool = False
    while not end_of_game:
        move: int = players[0].get_move(board) \
            if board.get_current_player() == 1 else \
            players[1].get_move(board)

        board.play_move(move)
        print(board)
        winner: int = board.check_winner()
        end_of_game = winner != 0 or board.is_full()
    print("Game over!")
    if winner != 0:
        message = [
            "Congratulations!",
            "Well played!",
            "You are the champion!",
            "Victory is yours!",
            "You nailed it!",
            "Amazing win!"
        ]
        winner_name = players[winner-1].name_
        print(f"Hey {winner_name}... {random.choice(message)}")
        print(f"Player {winner_name} wins!")
    else:
        print("It's a draw!")
    return winner


if __name__ == "__main__":  # pragma: no cover
    main()
