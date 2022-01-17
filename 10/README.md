# [Day 10: Syntax Scoring](https://adventofcode.com/2021/day/10)

## Part1: Find the the total syntax error score
First idea is to loop over each element and keep the kist of open symbols. Then pop the matching close symbol. 
If close symbol doesn't correspond to open one its a corruption. 

```
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
```
