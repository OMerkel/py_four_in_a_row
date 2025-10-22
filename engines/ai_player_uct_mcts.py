#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ai Player for py-four-in-a-row: A Python implementation of
the classic Four in a Row game.
This player uses UCT MCTS (Upper Confidence Bound applied to Trees -
Monte Carlo Tree Search) to determine its moves.
"""
import copy
import math
import random
import sys
from engines.abstract_player import AbstractPlayer


class Node:
    """A node in the UCT MCTS tree."""

    def __init__(self, state, parent=None, move=None):
        """Initialize the node.
        Args:
            state (Board): The game state at this node.
            parent (Node): The parent node.
            move (int): The move that led to this state.
        """
        self.state_ = state
        self.parent_ = parent
        self.move_ = move
        self.children_ = []
        self.visits_ = 0
        self.wins_ = 0
        self.untried_moves_ = state.get_legal_moves()

    def uct_select_child(self):
        """Select a child node using the UCT formula.

        Returns:
            Node: The selected child node.
        """
        # UCT formula: win_rate + sqrt(2 * log(parent_visits) / child_visits)
        return max(
            self.children_,
            key=lambda c: c.wins_ / c.visits_ +
            math.sqrt(2 * math.log(self.visits_) / c.visits_)
        )

    def add_child(self, move, state):
        """Add a child node for the given move and state.
        Args:
            move (int): The move leading to the new state.
            state (Board): The game state after the move.
        Returns:
            Node: The newly created child node.
        """
        child = Node(state, parent=self, move=move)
        self.untried_moves_.remove(move)
        self.children_.append(child)
        return child

    def update(self, result):
        """Update this node's statistics.
        Args:
            result (int): The result of the simulation (1 for win, 0 for loss).
        """
        self.visits_ += 1
        self.wins_ += result


class AiPlayerUctMcts(AbstractPlayer):
    """AI Player using UCT MCTS strategy for Four in a Row."""

    def __init__(self, name="UCT_MCTS", symbol="X",
                 simulations=1000,
                 player_id: int = 1):
        """Initialize the UCT MCTS player.
        Args:
            name (str): Name of the player.
            simulations (int): Number of simulations to run per move.
        """
        super().__init__(name, symbol, player_id=player_id)
        self.simulations_ = simulations

    def get_move(self, board) -> int:
        """Perform UCT MCTS to select the best move.
        Args:
            board (Board): The current game board.
        Returns:
            int: The selected column index for the move.
        """
        print(f"{self.name_} is thinking... ", end="")
        sys.stdout.flush()
        root = Node(copy.deepcopy(board))
        for _ in range(self.simulations_):
            node = root
            state = copy.deepcopy(board)

            # Selection
            while node.untried_moves_ == [] and node.children_:
                node = node.uct_select_child()
                # state.play_move(node.move_, state.get_current_player())
                state.play_move(node.move_)

            # Expansion
            if node.untried_moves_:
                move = random.choice(node.untried_moves_)
                state.play_move(move)
                node = node.add_child(move, copy.deepcopy(state))

            # Simulation (improved): check for immediate win/loss, else random
            while not state.is_game_over():
                legal_moves = state.get_legal_moves()
                current_player = state.get_current_player()
                # Try to win immediately
                for move in legal_moves:
                    temp_state = copy.deepcopy(state)
                    temp_state.play_move(move)
                    if temp_state.is_game_over() and \
                            temp_state.get_winner() == current_player:
                        state.play_move(move)
                        break
                else:
                    # Try to block opponent's immediate win
                    opponent = 2 if current_player == 1 else 1
                    blocked = False
                    for move in legal_moves:
                        temp_state = copy.deepcopy(state)
                        temp_state.play_move(move)
                        # After this move, check if opponent can win next
                        opp_moves = temp_state.get_legal_moves()
                        for opp_move in opp_moves:
                            temp_state2 = copy.deepcopy(temp_state)
                            temp_state2.play_move(opp_move)
                            if temp_state2.is_game_over() and \
                                    temp_state2.get_winner() == opponent:
                                # This move allows opponent to win, so try next
                                break
                        else:
                            # No immediate win for opponent after this move
                            state.play_move(move)
                            blocked = True
                            break
                    if not blocked:
                        # No immediate win or block, play random
                        state.play_move(random.choice(legal_moves))

            # Backpropagation
            winner = state.get_winner()
            # Assume self is maximizing player
            result = 1 if winner == self.player_id_ else 0
            # current_player = self.player_id_
            while node is not None:
                node.update(result)
                node = node.parent_
                # Alternate the reward for each player as we move up the tree
                result = 1 - result

        # Print an overview of the visits for each move,
        # sorted by visits (max to min)
        sorted_children = sorted(root.children_, key=lambda c: c.visits_,
                                 reverse=True)
        print("Move visit counts (sorted): ", end="")
        for child in sorted_children:
            print(f"[move {child.move_}: {child.visits_}]", end=" ")
        print()

        # Print total amount of simulations
        # total_visits = sum(child.visits_ for child in root.children_)
        # print(f"Total simulations: {total_visits}")

        # Choose the move with the most visits
        best_child = max(root.children_, key=lambda c: c.visits_)

        print("Done")
        return best_child.move_

    def get_most_likely_variant(self) -> list[int]:
        """Return the most likely variant of the game based on the MCTS tree.
        Returns:
            List[int]: The sequence of moves representing the most
            likely variant.
        """
        # This method can be implemented to return the
        # most likely sequence of moves based on the MCTS tree.
        # For simplicity, we return an empty list here.
        return []

    def get_likelihood_for_win(self) -> float:
        """Return the likelihood of winning from the current position.
        Returns:
            float: Likelihood of winning (0.0 to 1.0).
        """
        # This method can be implemented to return the
        # likelihood of winning based on the MCTS statistics.
        # For simplicity, we return 0.0 here.
        return 0.0

    def reset(self):
        """Reset any internal state of the player."""
        # No internal state to reset for this AI player.
        # pass
        return
