# 0x0A-primegame

## Prime Game

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

### Prototype
```python
def isWinner(x, nums)
```

### Parameters
- `x`: number of rounds
- `nums`: array of n values (one for each round)

### Return
- Name of the player that won the most rounds
- If the winner cannot be determined, return `None`

### Constraints
- `n` and `x` will not be larger than 10000
- Cannot import any packages

### Example

**Input:** `x = 3, nums = [4, 5, 1]`

**Round 1: n = 4**
- Initial set: {1, 2, 3, 4}
- Maria picks 2 and removes 2, 4, leaving {1, 3}
- Ben picks 3 and removes 3, leaving {1}
- Ben wins because there are no prime numbers left for Maria to choose

**Round 2: n = 5**
- Initial set: {1, 2, 3, 4, 5}
- Maria picks 2 and removes 2, 4, leaving {1, 3, 5}
- Ben picks 3 and removes 3, leaving {1, 5}
- Maria picks 5 and removes 5, leaving {1}
- Maria wins because there are no prime numbers left for Ben to choose

**Round 3: n = 1**
- Initial set: {1}
- Ben wins because there are no prime numbers for Maria to choose

**Result:** Ben has the most wins (2 wins vs 1 win for Maria)

### Usage Example

```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

**Output:**
```
Winner: Ben
```

### Game Rules
1. Players take turns choosing prime numbers from the set
2. When a prime number is chosen, both that number and all its multiples are removed from the set
3. Maria always goes first
4. Both players play optimally
5. The player who cannot make a move (no prime numbers left to choose) loses that round
6. The player with the most round wins is the overall winner
