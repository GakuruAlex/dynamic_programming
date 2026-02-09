# House Robber #
 You are a robber planning to rob houses along a street. Each house has a certain a mount of treasure stashed, the only constraint stopping you from robbing all the houses is the security system that is triggered when two consecutive houses are broken into in the same night. Given a list of integers representing the amount of money in each house, determine the maximum amount of money you can rob in one night without alerting the police.

## Input ##

An array of integers representing amount of money in each house.

## Output ##
An integer of the maximum amount of money robbed.


## Usage ##

```bash
python main.py
```

# Tests #

## Usage ##
```bash
pytest test_house_robber.py
```

| Test Case | Input Array                                                                 | Expected Output |
|-----------|-----------------------------------------------------------------------------|-----------------|
| Case 1    | [1, 2, 3, 1]                                                                | 4               |
| Case 2    | [2, 7, 9, 3, 1]                                                             | 12              |
| Case 3    | [2, 1, 1, 2]                                                                | 4               |
| Case 4    | [5, 3, 4, 11, 2]                                                            | 16              |
| Case 5    | [10, 1, 2, 10, 5, 1]                                                        | 21              |
| Case 6    | [1, 20, 3]                                                                  | 20              |
| Case 7    | [100]                                                                       | 100             |
| Case 8    | []                                                                          | 0               |

 # Complexity #

## Time Complexity ##

Linear time complexity O(n)

## Space Complexity ##

Constant space complexity O(1) 