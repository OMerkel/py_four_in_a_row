# Software Architecture: py_four_in_a_row

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.txt)
[![Pytest](https://img.shields.io/badge/tested%20with-pytest-blue.svg)](https://docs.pytest.org/)
[![UV](https://img.shields.io/badge/managed%20by-uv-purple.svg)](https://github.com/astral-sh/uv)

## Quick Start

```bash
...$ git clone https://github.com/OMerkel/py_four_in_a_row
...$ cd py_four_in_a_row
...$ python -m venv .venv
...$ source .venv/bin/activate
...$ pip install -r requirements.txt
...$ uv sync
...$ uv run ./py_four_in_a_row.py
```

## Directory Structure

```text
py_four_in_a_row/
├── [py_four_in_a_row.py](../py_four_in_a_row.py)         # Main entry point
├── [pyproject.toml](../pyproject.toml)                   # Project configuration
├── [requirements.txt](../requirements.txt)               # Python dependencies
├── [AUTHORS](../AUTHORS)                                 # Contributors with non-trivial changes
├── [LICENSE.txt](../LICENSE.txt)                         # MIT License text
├── [README.md](../README.md)                             # Project overview
├── doc/
│   └── [software_architecture.md](software_architecture.md)    # Architecture documentation
├── engines/
│   ├── [abstract_player.py](../engines/abstract_player.py)        # Abstract player interface
│   ├── [ai_player_uct_mcts.py](../engines/ai_player_uct_mcts.py)  # AI player (UCT MCTS)
│   └── [human_player.py](../engines/human_player.py)              # Human player implementation
├── modules/
│   └── [board.py](../modules/board.py)                   # Board logic
└── test/
    ├── [test_board.py](../test/test_board.py)            # Board unit tests
    ├── [test_human_player.py](../test/test_human_player.py)         # HumanPlayer unit tests
    └── [test_py_four_in_a_row.py](../test/test_py_four_in_a_row.py) # Main game tests 
```

----

## License

This project is licensed under the terms of the [LICENSE.txt](../LICENSE.txt) file in the root directory.

----

## Architecture Diagram (Conceptual)

Below is a conceptual diagram of the main components and their relationships:

```uml
   +--------------------------------+
   |   py_four_in_a_row.py (main)   |
   +--------------------------------+
                  |
                  v
        +-------------------+
        |      Board        |
        +-------------------+
            /           \
           v             v
  +-------------+   +---------------------+
  | HumanPlayer |   |   AiPlayerUctMcts   |
  +-------------+   +---------------------+
         ^                  ^
         |                  |
     +-----------------------------+
     |     AbstractPlayer          |
     +-----------------------------+
```

This diagram shows the main script interacting with the Board and Player classes, with both human and AI players inheriting from AbstractPlayer.

## Overview

**py_four_in_a_row** is a modular Python implementation of the classic "Four in a Row" (Connect Four) game. It supports both human and AI players, with the AI using Upper Confidence bounds applied to Trees (UCT) Monte Carlo Tree Search (MCTS) for decision-making. The architecture is designed for extensibility, testability, and clarity.

----

## Main Components

### 1. Entry Point

- **[`py_four_in_a_row.py`](../py_four_in_a_row.py)**
  - Contains the `main()` function.
  - Handles player setup, game loop, and user interaction.
  - Instantiates the game board and player objects.

----

## Player/Board Interaction

The main game loop alternates between players, calling each player's `get_move(board)` method. The returned move is validated and applied to the `Board` instance, which updates the game state and switches the current player.

### 2. Game Board

- **[`modules/board.py`](../modules/board.py)**
  - Implements the `Board` class.
  - Manages the game state, move legality, win/draw detection, and board representation.
  - Provides methods for playing moves, undoing moves, and querying the board.

### 3. Player Abstraction

- **[`engines/abstract_player.py`](../engines/abstract_player.py)**
  - Defines the `AbstractPlayer` base class.
  - Specifies the interface for all player types (AI or human).

### 4. Player Implementations

- **[`engines/human_player.py`](../engines/human_player.py)**
  - Implements `HumanPlayer`, which interacts with the user for move input.

- **[`engines/ai_player_uct_mcts.py`](../engines/ai_player_uct_mcts.py)**
  - Implements `AiPlayerUctMcts`, an AI player using UCT MCTS.
  - Contains the `Node` class for MCTS tree nodes.
  - Handles selection, expansion, simulation, and backpropagation phases of MCTS.

### 5. Testing

- **[`test/`](../test/)**
  - Contains unit tests for the board and main game logic.
  - Uses `pytest` and `unittest` for test execution.

----

## Data Flow

1. **Startup:**  
   The main script prompts for player names and creates player objects (AI or human).

2. **Game Loop:**  
   - The board is displayed.
   - The current player is asked for a move.
   - The move is validated and played on the board.
   - The board is updated and displayed.
   - The game checks for a win or draw.

3. **AI Move Selection:**  
   - The AI uses MCTS to simulate many possible futures.
   - The move with the highest visit count is selected.

4. **Player/Board Interaction:**
   - The `get_move(board)` method is called for the current player.
   - The move is applied to the board, which updates the state and switches the player.

5. **End of Game:**
   - The winner or draw is announced.

----

## Extensibility

- **Adding New Player Types:**  
  Inherit from `AbstractPlayer` and implement the required methods.

- **Changing Board Size:**  
  Modify the `Board` class constructor parameters.

- **Improving AI:**  
  Enhance the MCTS logic in `AiPlayerUctMcts` or add new AI strategies.

----

## AI Implementation

### Monte Carlo Tree Search (MCTS)

MCTS is a heuristic search algorithm used for decision-making in games and other domains. It builds a search tree incrementally and uses random simulations to estimate the value of moves. MCTS consists of four main steps:

1. **Selection:** Starting from the root node, recursively select child nodes using a policy like UCT until a node with untried moves or a terminal state is reached.
2. **Expansion:** If the selected node is not terminal, expand the tree by adding a new child node corresponding to an untried move.
3. **Simulation (Rollout):** From the new node, play out the game to the end using random (or semi-random) moves to simulate the outcome.
4. **Backpropagation:** Propagate the simulation result back up the tree, updating statistics (wins, visits) for each node along the path.

After many iterations, the move corresponding to the child node with the highest visit count is chosen as the best move. MCTS is effective because it focuses computational effort on the most promising parts of the search space.

### Upper Confidence bounds applied to Trees (UCT)

#### Customizing the Exploration Constant

The exploration constant `c` in the UCT formula controls the balance between exploration and exploitation. Increasing `c` makes the AI explore more, while decreasing it makes the AI focus more on moves that have already shown good results. You can adjust this value in the AI code to tune the AI's playing style.

UCT is a strategy used within MCTS to balance exploration and exploitation when selecting which node (move) to explore next in the search tree. The UCT formula assigns a value to each child node based on its average reward (exploitation) and how often it has been visited relative to its parent (exploration). The formula is:

  UCT = (w_i / n_i) + c * sqrt(ln(N) / n_i)

where:

- w_i = number of wins for child i
- n_i = number of simulations for child i
- N = total simulations for the parent node
- c = exploration constant (controls the balance between exploration and exploitation)

UCT ensures that the search does not focus only on the most promising moves (exploitation), but also occasionally tries less-visited moves (exploration) to discover potentially better strategies.

#### Common Pitfalls on Implementations

If the code is selecting the move with the lowest UCB value (e.g., using min() instead of max()), it will consistently pick the worst move, as lower UCB values indicate less promising moves.

In Reward Propagation (Backpropagation) the approach is usually to alternate the reward for the opponent. In standard MCTS, the reward is usually flipped for the opponent at each level up the tree, so that each node’s statistics reflect the perspective of the player who made the move at that node. Without this, the tree may not properly learn to avoid moves that are good for the opponent. This can cause the AI to misinterpret which moves are actually good for itself versus the opponent, leading to poor move choices. This is a common pitfall in MCTS implementations. Thus non-alternated rewards may result in biased statistics.

Following a standard random playout policy (performing any random allowed moves) is not optimal. In Connect Four, random playouts are often extremely noisy and do not reflect the true value of a position, especially with a large branching factor. This can make the MCTS value estimates very poor, even with many simulations.

The simulation could prioritize immediate wins or blocks, otherwise the AI may miss obvious threats or opportunities. As such it is implemented that direct threats (immediate wins) should roughly be preferred in a pre-move-analysis. Still this could be improved.

----

## AI Improvements

The AI's simulation policy is enhanced: during rollouts, it checks for immediate winning moves and blocks the opponent's immediate win, making the AI more robust than pure random playouts.

----

## Configuration and Customization

- **Number of Simulations:** Change the `simulations` parameter when creating an `AiPlayerUctMcts` instance.
- **Board Size:** Pass different `rows` and `cols` to the `Board` constructor.
- **Player Types:** Modify the player setup logic in `py_four_in_a_row.py` to use human or AI players as desired.

----

## Error Handling

The codebase is designed to handle invalid moves and unexpected input gracefully. For example, the Board class checks for move legality, and the main game loop ensures only valid moves are played. If an error occurs, the program will print an informative message and prompt for a new input or safely terminate.

----

## Logging and Debugging

For troubleshooting or understanding the AI's decision process, you can add print statements or use Python's logging module in the AI and game loop. This can help trace the sequence of moves, AI choices, and board states during development or debugging.

----

## Contributing

Contributions are welcome! To contribute:

- Fork the repository and create a new branch for your feature or bugfix.
- Follow PEP8 coding style and add docstrings to new functions/classes.
- Add or update tests in the `test/` directory as appropriate.
- Open a pull request with a clear description of your changes.

For questions or suggestions, please open an issue in the repository.

----

## Further Reading and References

- [Monte Carlo Tree Search (Wikipedia)](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
- [Upper Confidence Bound for Trees (UCT)](https://www.cs.princeton.edu/courses/archive/fall18/cos402/readings/uct.pdf)
- [Connect Four Strategy](https://en.wikipedia.org/wiki/Connect_Four#Strategy)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [pytest Documentation](https://docs.pytest.org/)

----

## Dependencies

- Python 3.8+
- `uv` (for dependency management and virtual environment handling)
- `pytest`, `unittest` (for testing)
- `coverage` (for measurement of code coverage)
- `flake8`, `ruff`, `pylint`, `isort` (for statical code analysis and linting)
- `black`, `pep8` (for code formatting)
- `prettier` (for markdown linting)
- `jscpd` (copy/paste detection)

----

## How to Run

```bash
...$ uv run ./py_four_in_a_row.py
```

----

## How to Test

```bash
...$ pytest
```

## Testing & Quality

- All core logic is covered by unit tests in the `test/` directory.
- The project uses `pytest` for test discovery and execution.
- Code is modular to facilitate isolated testing and future refactoring.

----

*This document provides a high-level overview of the architecture and is intended for developers and contributors.*
