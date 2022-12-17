from solutions import printpuz, day2, day2b, day3, day3b, day4, day5, day6, day7a, day7b, day8, day8b, day9, day10, compute_scenic_score, dropNothing, add_letter_around_outside
from solutions import day11

def printans(puzzle_number, actual_output):
  print(f"Puzzle {puzzle_number}: {actual_output}")


with open("input2.txt") as f:
    input = f.read()
    printpuz("2A", day2(input), 15572)
    printpuz("2B", day2b(input), 16098)

with open("input3.txt") as f:
    input = f.read()
    printpuz("3A", day3(input), 8176)
    printpuz("3B", day3b(input), 2689)

with open("input4.txt") as f:
    input = f.read()
    printpuz("4A", day4(input, False), 538)
    printpuz("4B", -1, -2)

with open("input5.txt") as f:
    input = f.read()
    printpuz("5A", day5(input), "CVCWCRTVQ")
    printpuz("5B", day5(input, False, True), "CNSCZWLVT")

with open("input6.txt") as f:
    input = f.read()
    printpuz("6A", day6(input, 4), 1896)
    printpuz("6B", day6(input, 14), 3452)

with open("input7.txt") as f:
    input = f.read()
    printpuz("7A", day7a(input), 1334506)
    printpuz("7B", day7b(input), 7421137)

with open("input8.txt") as f:
    input = f.read()
    printpuz("8A", day8(input), 1708)
    printpuz("8B", day8b(input), 504000)

with open("input9.txt") as f:
    input = f.read()
    printpuz("9A", day9(input), 6367)
    printpuz("9B", -1, -2)

with open("input10.txt") as f:
    input = f.read()
    printpuz("10A", day10(input), 13720)
    printpuz("10B", -1, -2)

with open("input11.txt") as f:
    input = f.read()
    printpuz("11A", day11(input), 98280)
    printpuz("11B", day11(input, True, False), 17673687232)
