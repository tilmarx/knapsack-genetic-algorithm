# Knapsack Problem – Genetic Algorithm

Genetic algorithm as heuristic for the 0/1 knapsack problem – written in Python as a self-directed school project.

## What is the 0/1 Knapsack Problem?

The knapsack problem is a classic problem in combinatorial optimization: given a set of items, each with a weight and a value, determine which items to include in a collection so that the total weight does not exceed a given limit and the total value is maximized.

The **0/1** variant means each item can either be taken (1) or left behind (0) – no fractions allowed. This makes it an NP-hard problem, meaning no efficient exact solution is known for large inputs. A heuristic like a genetic algorithm is therefore a practical approach.

## How it works

The algorithm mimics the process of natural evolution through three core steps:

**1. Selection**  
The weakest solutions (those with the lowest total value) are removed from the population, keeping only the best candidates for reproduction.

**2. Crossover**  
Pairs of surviving solutions are combined at a random cut point to produce new offspring solutions, similar to how DNA is exchanged in biological reproduction.

**3. Mutation**  
Each solution has a 20% chance per item of being randomly flipped (0 → 1 or 1 → 0), introducing variation and preventing the algorithm from getting stuck in local optima.

These steps repeat for a set number of generations, after which the best solution found is returned.

## Usage

Run the script and follow the prompts:

```bash
python main.py
```

You will be asked to enter:
- Knapsack capacity
- Number of items
- Maximum item value
- Maximum item weight
- Number of generations

### Example output

```
Das sind alle zur Verfügung stehenden Gegenstände: [(8, 3), (5, 7), (12, 4), (3, 2)]
Der Rucksack hat eine Kapazität von 10kg. Davon werden 90.0% genutzt.
Der erzielte Wert liegt bei 23€.
Die mitgenommenen Gegenstände sind Folgende: [(8, 3), (12, 4)]
```

## Known limitations

- Bug in the mutation function: items are not mutated correctly due to Python's loop variable scoping
- No object-oriented structure – all logic runs in the global namespace
- `bin` is used as a variable name, which shadows Python's built-in function
- These issues are intentional to preserve the original school project state and will be addressed in a future refactor

## Requirements

- Python 3.x
- No external libraries required

## What I learned

- How to represent combinatorial solutions as binary arrays
- The three core mechanics of evolutionary algorithms: selection, crossover, mutation
- Why NP-hard problems require heuristic approaches
- Basic Python: lists, functions, random number generation, user input

## Future improvements

- [ ] Fix mutation bug
- [ ] Refactor into classes
- [ ] Add fitness function
- [ ] Visualize fitness over generations with matplotlib
- [ ] Compare results against brute-force for small inputs
