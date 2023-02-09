# Card Counting Simulation
## Usage
- Use an existing strategy or create a custom card-counting strategy (see `src/strategies`).
- Simulate with varying number of decks in the shoe and vary number of shoes (see `/src/execution/runner.py`)

## Codebase Structure
```
.
├── LICENSE
├── README.md
└── src
    ├── blackjack
    │   └── Blackjack.py
    ├── execution
    │   └── runner.py
    ├── shoe
    │   ├── Card.py
    │   └── Shoe.py
    ├── strategies
    │   ├── BaseStrategy.py
    │   ├── Dealer.py
    │   └── HiOpt1.py
    └── utils
        └── card_utils.py
```