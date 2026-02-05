from typing import List

from min_cost_climbing_stairs import min_cost_stairs

def main():
    #min_cost_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) test array output 6
    cost_array: List[int] = [int(element) for element in input("Enter the cost array, separated by a space i.e 2 4 6: ").split()]
    print(f"The minimum cost for given the cost array {cost_array} is {min_cost_stairs(cost_array)}")

if __name__ == '__main__':
    main()