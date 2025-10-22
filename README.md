# py-four-in-a-row

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.txt)
[![Pytest](https://img.shields.io/badge/tested%20with-pytest-blue.svg)](https://docs.pytest.org/)
[![UV](https://img.shields.io/badge/managed%20by-uv-purple.svg)](https://github.com/astral-sh/uv)

A modular Python implementation of the classic Four in a Row (Connect Four) game, featuring both human and AI players. The AI uses Upper Confidence bounds applied to Trees (UCT) Monte Carlo Tree Search (MCTS) for competitive gameplay.

----

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

----

## Features

- Play against a human or AI opponent
- AI uses UCT MCTS for move selection
- Modular, extensible architecture
- Unit tests for core logic
- Easy configuration for board size, player types, and AI strength

----

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

## How to Play

Run the main script and follow the prompts to set up players and start the game.
Leave the player names empty to activate AI players.
You can configure player types and AI strength in `py_four_in_a_row.py`.

----

## How to Test

```bash
...$ pytest
```

----

## Documentation

See [`doc/software_architecture.md`](doc/software_architecture.md) for a detailed overview of the architecture and design.

----

## License

This project is licensed under the terms of the MIT [LICENSE.txt](LICENSE.txt) file.

----

## Contact

For questions or contributions, please open an issue or pull request on GitHub.

----

## Further Reading

- [Monte Carlo Tree Search (Wikipedia)](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
- [Connect Four Strategy](https://en.wikipedia.org/wiki/Connect_Four#Strategy)

----
