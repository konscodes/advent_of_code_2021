# [Day 7: Crab horizontal relocation](https://adventofcode.com/2021/day/7)

Approach with creating a counter for each position and trying to locate the most crowded space by splitting counter range in half didn't really work on a large set. 

### New approach
1. Data - horizontal positions
2. Range of the data is max position
3. For each position get the distance between elements
4. Apply factorial (actually Triangular number) for each distance in the range to get total cost distribution
5. Merge cost distribution for each position to get superposition of cost distribution
6. Minimum value index will be our position to align to. Well total cost is already there as well