# [Day 7: Crab horizontal relocation](https://adventofcode.com/2021/day/7)

Approach with creating a counter for each position and trying to locate the most crowded space by splitting counter range in half didn't really work on a large set. 

New approach:
1. Data - horizontal positions
1. Range of the data is max position
1. For each positions get the distance between distance_between_elements
1. Apply factorial for each distance in the range to get total cost cost_distribution
1. Merge cost distribution for each position to get superposition of cost_distribution
1. Minimum value index will be our position to align to. Well total cost is already there as well