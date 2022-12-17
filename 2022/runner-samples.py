from solutions import printpuz, day2, day2b, day3, day3b, day4, day5, day6, day7a, day7b, day8, day8b, day9, day10, compute_scenic_score, dropNothing, add_letter_around_outside
from solutions import day11



day2sample = """A Y
B X
C Z"""

printpuz("2A", day2(day2sample), 15)
printpuz("2B", day2b(day2sample), 12)

day3sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

printpuz("3A", day3(day3sample), 157)
printpuz("3B", day3b(day3sample), 70)

day4sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

printpuz("4A", day4(day4sample, False), 2)

day4sample2 = """6-10,5-5"""
printpuz("4A", day4(day4sample2, True), 0)

printpuz("4B", -1, -2)

day5sample = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

printpuz("5A", day5(day5sample, False, False), "CMZ") # non-debug 5a
# printpuz("5A", day5(day5sample, True, False), "CMZ") # Debug 5a
printpuz("5B", day5(day5sample, False, True), "MCD") # non-debug 5b
# printpuz("5B", day5(day5sample, True, True), "MCD") # debug 5b

day6sample1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # 7
day6sample2 = """bvwbjplbgvbhsrlpgdmjqwftvncz
""" # 5
day6sample3 = "nppdvjthqldpwncqszvftbrmjlhg" # 6
day6sample4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 10
day6sample5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # 11

printpuz("6A1", day6(day6sample1, 4), 7)
printpuz("6A2", day6(day6sample2, 4), 5)
printpuz("6A3", day6(day6sample3, 4), 6)
printpuz("6A4", day6(day6sample4, 4), 10)
printpuz("6A5", day6(day6sample5, 4), 11)

printpuz("6B1", day6(day6sample1, 14), 19)
printpuz("6B2", day6(day6sample2, 14), 23)
printpuz("6B3", day6(day6sample3, 14), 23)
printpuz("6B4", day6(day6sample4, 14), 29)
printpuz("6B5", day6(day6sample5, 14), 26)



day7sample = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

printpuz("7A", day7a(day7sample, False), 95437)
# printpuz("7A", day7a(day7sample, True), 95437)
printpuz("7B", day7b(day7sample, False), 24933642)
# printpuz("7B", day7b(day7sample, True), 24933642)

day8sample = """
30373
25512
65332
33549
35390
"""

printpuz("8A", day8(day8sample), 21)
printpuz("8B", day8b(day8sample), 8)

lines = dropNothing(day8sample.split("\n"))
sentinel = "A"
lines2 = add_letter_around_outside(lines, sentinel)

printpuz("8B 1st example", compute_scenic_score(lines2, 2, 3, "A"), 4)
printpuz("8B 2nd example", compute_scenic_score(lines2, 4, 3, "A"), 8)

day9sample = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

printpuz("9A", day9(day9sample), 13)
printpuz("9B", -1, 36)

day10sample = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""

printpuz("10A", day10(day10sample, False), 13140)
printpuz("10B", -1, -2)

day11sample = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

printpuz("11A", day11(day11sample, False, False), 10605)
# printpuz("11B", day11(day11sample, True, False), 2713310158)
printpuz("11B", day11(day11sample, True, False), 2567194800)
