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
    robot_names = [
        "HAL9000", "Dalek", "Ava", "Maria", "The Maschinenmensch",
        "Bishop", "Ash", "EVE", "Gort", "Robbie", "Chappie",
        "Sonny", "Dewey", "Huey", "Louie", "Ares",
        "Gigolo Joe", "Marvin", "Dot Matrix", "Bender", "Optimus Prime",
        "Megatron", "Johnny 5", "Roy Batty", "Pris", "Deckard",
        "Iron Giant", "VIKI", "Sonny", "Gigantor",
        "Maximilian", "Box", "Dot", "Twiki", "TARS", "CASE", "David",
        "Mother", "Atlas", "Rosie"
    ]
    random.shuffle(robot_names)
    player1_name: str = input("Enter name for Player 1: ")
    player1: AbstractPlayer = AiPlayerUctMcts(
        name=robot_names.pop(), symbol="X",
        simulations=1750, player_id=1
    ) if player1_name == "" else HumanPlayer(
        name=player1_name, symbol="X",
        player_id=1
    )
    player1.reset()

    player2_name: str = input("Enter name for Player 2: ")
    player2: AbstractPlayer = AiPlayerUctMcts(
        name=robot_names.pop(), symbol="O",
        simulations=1750, player_id=2
    ) if player2_name == "" else HumanPlayer(
        name=player2_name, symbol="O",
        player_id=2
    )
    player2.reset()
    return [player1, player2]


def game_loop(setup=setup_players) -> tuple[int, list[AbstractPlayer]]:
    """Main game loop for py-four-in-a-row."""
    players: list[AbstractPlayer] = setup()
    board: Board = Board(current_player=1, players=players)
    print(board)

    end_of_game: bool = False
    while not end_of_game:
        move: int = players[0].get_move(board) \
            if board.get_current_player() == 1 else \
            players[1].get_move(board)
        if move not in board.get_legal_moves():
            if move in HumanPlayer.command and move == 100:
                print("\n".join(board.dump_history()))
                continue
            print(f"Illegal move: {move}. Try again.")
            continue
        board.play_move(move)
        print(board)
        winner: int = board.check_winner()
        end_of_game = winner != 0 or board.is_full()
    print("Game over!")
    return winner, players


def main(game_entry_point=game_loop) -> int:
    """Main entry point for the py-four-in-a-row application."""
    print("Hello from py-four-in-a-row!")
    winner, players = game_entry_point()
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
