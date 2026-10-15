# PyHood

**Exploring Python by rebuilding things from scratch.**

PyHood is a collection of programming experiments, educational reimplementations, and algorithmic explorations written in Python.

The goal is to understand how programming concepts work by solving problems under constraints, implementing solutions from scratch, and exploring different approaches to the same problem.

This project is a learning laboratory, not a replacement for Python's built-in functionality.

## Experiments

| Experiment | Implementation | Documentation | Focus |
|---|---|---|---|
| String Reversal | [`reverse.py`](src/pyhood/reverse.py) | [`reverse.md`](docs/reverse.md) | Reversing strings without using `[::-1]` |

As the project grows, new experiments will be added to this table.

## Project Structure

```text
PyHood/
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   └── pyhood/
│       └── reverse.py
├── tests/
│   └── test_reverse.py
└── docs/
    └── reverse.md
```

Each experiment has its own implementation, tests, and documentation.

- `src/pyhood/` contains the Python implementations.
- `tests/` contains tests that verify their behavior.
- `docs/` explains the motivation, approach, constraints, and lessons learned for each experiment.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/mohammadtahaabdinasab/PyHood
cd PyHood
```

Install the project and its development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the test suite:

```bash
python -m pytest -v
```

## Adding an Experiment

Each new experiment should follow a consistent structure.

For example, a future sorting experiment could include:

```text
src/pyhood/sorting.py
tests/test_sorting.py
docs/sorting.md
```

Its documentation should explain why the experiment exists, any constraints, the implementation approach, and relevant observations.

The README should then be updated to include the new experiment in the table above.

Not every experiment needs to be complicated. Small problems can be valuable when they reveal something interesting about algorithms, data structures, or Python's behavior.

## Principles

- Learn by implementing, not just using existing functionality.
- Understand constraints before choosing an approach.
- Prefer readable implementations over unnecessary complexity.
- Test normal cases, edge cases, and unexpected inputs.
- Explore alternative solutions and their trade-offs.
- Record the reasoning behind each experiment.

## Status

**Early development.**

Currently exploring string manipulation through a custom string-reversal implementation.

New experiments will be added as the project evolves.
