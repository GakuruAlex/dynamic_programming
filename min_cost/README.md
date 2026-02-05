# Min Cost Climbing Stairs #
____
## Problem Statement ##
You are given an integer array ***cost*** where ***cost[i]*** is the cost of i-th step on a staircase. Once you pay the cost you can either climb one or two steps.
You can start from the stair index 0 or index 1. Return the minimum cost to reach the top of the floor.
****
## Usage ##

Run
```bash

python main.py
```


## Test ##
```markdown
Examples:
    Input: cost = [10, 15, 28]
    Output: 15

    Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    Output: 6

```
Run
```bash

pytest test_min_cost_climbing_stairs.py
```
***
## Complexity ##

### Space Complexity ###

Keep track of the two previous minimum costs.

Constant space complexity O(1)

### Time Complexity ###

Iterates through all the elements of cost array : O(N), where N is  size of  cost array



