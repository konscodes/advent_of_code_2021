# [Day 8: Seven Segment Search](https://adventofcode.com/2021/day/8)

## Part1: count the digits
How many times do digits 1, 4, 7, or 8 appear?
This is quite easy and can be done in single operation
```
counter += 1 if len(segment) <= 4 or len(segment) == 7
```

## Part2: decode digits from input and provide the sum of all digits from output
This is a more difficult task, yet easy to solve with just few conditions. There must be a better more efficient approach to this.

### Digits representation
```
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
```

### Solution with conditions
1. Take the input line and sort all into tuple from short to long values
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb 
2. Shortest 2 segments is 1: be; difference from decoded elements is be
 - Upper right: b, e
 - Lower right: b, e
3. Next is 3 segments 7: edb; difference from decoded elements is d
 - Upper right: b, e
 - Lower right: b, e
 - Upper: d
4. Next is 4 segments 4: cgeb; difference from decoded elements is cg
 - Upper right: b, e
 - Lower right: b, e
 - Upper: d
 - Upper left: c, g
 - Middle: c, g
5. Next is 5 segments 2,3,5 multiple values skip
6. Next is 6 segments 0,6,9 multiple values skip
7. Next is 7 segments 8: cfbegad; difference from decoded elements is fa
 - Upper right: b, e
 - Lower right: b, e
 - Upper: d
 - Upper left: c, g
 - Middle: c, g
 - Lower left: f, a
 - Lower: f, a
8. Take 5 segment values; 
fdcge fecdb fabcd
    if includes both  
    - Upper left: c, g
    - Middle: c, g
    then is 5 (fdcge)
        in fde not Upper righ and not Lower left (remove matched element)
 - Upper right: b
 - Lower right: e
 - Upper: d
 - Upper left: c, g
 - Middle: c, g
 - Lower left: a
 - Lower: f
    else in fecdb fabcd not Upper left (difference between [fecdb fabcd] and Upper left: [c, g])
 - Upper right: b
 - Lower right: e
 - Upper: d
 - Upper left: g
 - Middle: c
 - Lower left: a
 - Lower: f
    