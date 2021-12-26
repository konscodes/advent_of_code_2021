# [Day 9: Smoke Basin](https://adventofcode.com/2021/day/9)

## Part1: Find the low points
The locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively.

```
2**1**9994321**0**
3987894921
98**5**6789892
8767896789
989996**5**678
```
### Solution with low map
Lows map will represent the whole space in the form of list of lists with rows and columns filled with 0's.
```[[0,0,0], [0,0,0], [0,0,0]]``` for 3x3 space
Initially I did compare each row and column values with nearby values by using sliding window. However now I know it would be easier with *zip* function.
Once we get local lows for each row and column we now need to compare the two to find those lows that match.
Low map was used for that purpose. We increment the match on the map and match those that are more than 1 to row elements.  


## Part2: 
