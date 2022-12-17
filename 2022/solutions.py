from collections import defaultdict
#from queue import PriorityQueue
from random import choices
from string import ascii_lowercase

def printpuz(puzzle_number, actual_output, expected_output):
  if actual_output == expected_output:
    print(f"✅ Puzzle {puzzle_number}: {actual_output} == {expected_output}")
  else:
    print(f"❌ Puzzle {puzzle_number}: {actual_output} != {expected_output}")


shapetoscore = {
  "A": 1, # 2b rock
  "B": 2, # 2b paper
  "C": 3, # 2b scissors
  "X": 1, # 2a rock
  "Y": 2, # 2a paper
  "Z": 3, # 2a scissors
}

combotoscore = {
  "A X": 3, # both rock
  "B Y": 3, # both paper
  "C Z": 3, # both scissors
  "A Y": 6, # rock loses to paper
  "B Z": 6, # paper loses to scissors
  "C X": 6, # scissors loses to rock
  "A Z": 0, # rock beats scissors
  "B X": 0, # paper beats rock
  "C Y": 0, # scissors beats paper
}

# 2b
outcometoscore = {
  "X": 0, # i lose
  "Y": 3, # we tie
  "Z": 6, # i win
}

def get_my_move(line):
  line_to_move = {
    "A Y": "A", # they play rock, we tie -> I play rock
    "B Y": "B", # 
    "C Y": "C", # 
    "A X": "C", # they play rock, I lose -> I play scissors
    "B X": "A", # they play paper, I lose -> I play rock
    "C X": "B", # they play scissors, I lose -> I play paper
    "A Z": "B", # they play rock, I win -> I play paper
    "B Z": "C", # they play paper, I win -> I play scissors
    "C Z": "A", # they play scissors, I win -> I play rock
  }
  return line_to_move[line]


def day2round(line):
  if not line:
    return 0
  [_, me] = line.split(" ")
  myshapescore = shapetoscore[me]
  outcomescore = combotoscore[line]
  return myshapescore + outcomescore

def day2(input):
  lines = input.split("\n")
  score = 0
  for line in lines:
    score += day2round(line)
  return score

def day2bround(line):
  if not line:
    return 0
  [_, outcome] = line.split(" ")
  me = get_my_move(line)
  myshapescore = shapetoscore[me]
  outcomescore = outcometoscore[outcome]
  return myshapescore + outcomescore

def day2b(input):
  lines = input.split("\n")
  score = 0
  for line in lines:
    score += day2bround(line)
  return score

itemtopriority = {
  'a': 1,
  'b': 2,
  'c': 3,
  'd': 4,
  'e': 5,
  'f': 6,
  'g': 7,
  'h': 8,
  'i': 9,
  'j': 10,
  'k': 11,
  'l': 12,
  'm': 13,
  'n': 14,
  'o': 15,
  'p': 16,
  'q': 17,
  'r': 18,
  's': 19,
  't': 20,
  'u': 21,
  'v': 22,
  'w': 23,
  'x': 24,
  'y': 25,
  'z': 26,
  'A': 27,
  'B': 28,
  'C': 29,
  'D': 30,
  'E': 31,
  'F': 32,
  'G': 33,
  'H': 34,
  'I': 35,
  'J': 36,
  'K': 37,
  'L': 38,
  'M': 39,
  'N': 40,
  'O': 41,
  'P': 42,
  'Q': 43,
  'R': 44,
  'S': 45,
  'T': 46,
  'U': 47,
  'V': 48,
  'W': 49,
  'X': 50,
  'Y': 51,
  'Z': 52,
}

def day3singlerucksack(line):
  halfway = int(len(line)/2)
  left = set(line[:halfway])
  right = set(line[halfway:])
  itemsInBoth = left.intersection(right)
  return itemsInBoth.pop()

def find_common_item(elf1, elf2, elf3):
  return set(elf1).intersection(elf2).intersection(elf3).pop()

def day3(input):
  lines = input.split("\n")
  score = 0
  for line in lines:
    item = day3singlerucksack(line)
    score += itemtopriority[item]
  return score

def day3b(input):
  lines = dropNothing(input.split("\n"))
  num_groups = int(len(lines) / 3)
  score = 0

  for group_index in range(num_groups):
    item = find_common_item(lines[group_index * 3], lines[group_index * 3 + 1], lines[group_index * 3 + 2])
    score += itemtopriority[item]
  return score

def day4_singlepairofelves(line: str, debug: bool):
  if not line:
    return False
  [elf1, elf2] = line.split(",")
  [elf1start, elf1finish] = [int(x) for x in elf1.split("-")]
  [elf2start, elf2finish] = [int(x) for x in elf2.split("-")]
  if elf1start <= elf2start and elf1finish >= elf2finish:
    maybeprint("!" + line, debug)
    return True # elf1 contains elf2
  if elf2start <= elf1start and elf2finish >= elf1finish:
    maybeprint("*" + line, debug)
    maybeprint(f"{elf2start} <= {elf1start} and {elf2finish} >= {elf1finish}", debug)
    return True # elf2 contains elf1
  return False

def day4(input, debug=False):
  lines = input.split("\n")
  numToReconsider = 0
  for line in lines:
    if day4_singlepairofelves(line, debug):
      numToReconsider += 1
  return numToReconsider


def dropNothing(array):
  return [a for a in array if a]

def get_tops_of_stacks(stacks):
  tops = []
  for s in stacks.values():
    tops.append(s[-1])
  return "".join(tops)

def day5(input:str, debug=False, part_b=False):
  moveindex = input.find("move")
  drawing_string = input[:moveindex]
  drawing_lines = dropNothing(drawing_string.split("\n"))
  # final_drawing_line = drawing_lines[-1]
  drawing_lines_reversed = drawing_lines[::-1][1:] # also take out final_drawing_line

  move_string = input[moveindex:]
  moves = dropNothing(move_string.split("\n"))

  stacks = defaultdict(list)
  for l in drawing_lines_reversed:
    stack_index = 0
    line_index = 1
    while line_index < len(l):
      if l[line_index] != ' ':
        stacks[stack_index].append(l[line_index])
      stack_index += 1
      line_index += 4
  # return stacks.values()

  for move in moves:
    words = move.split(" ")
    count = int(words[1])
    from_stack = int(words[3]) - 1 # Convert "1" to 0, etc
    to_stack = int(words[5]) - 1
    if debug:
      print(stacks.values())
      print(f"Move [{count}] from [{from_stack}] to [{to_stack}]")
    if part_b:
      to_move = stacks[from_stack][-count:]
      for block in to_move:
        stacks[to_stack].append(block)
      del stacks[from_stack][-count:]
    else:
      while count:
        stacks[to_stack].append(stacks[from_stack].pop())
        count -= 1
    if debug:
      print(stacks.values())
  
  # ASSUMPTION: At most 9 stacks, each one takes 3 characters, one space between each

  # drawing_string.split("\n")
  return get_tops_of_stacks(stacks)



def day6(input, count):
  if input[-1] == "\n":
    input = input[:-1]
  i = 0
  while i + count < len(input):
    s = set(input[i:i+count])
    if len(s) == count:
      break    
    i += 1
  return i + count


class file():
  def __init__(self, name: str, size: int) -> None:
    self.name = name
    self.size = size

  def __str__(self) -> str:
    return f"File [{self.name}] = [{self.size}]"

class directory():
  def __init__(self, name) -> None:
    self.name = name
    self.subdirs: list[directory] = []
    self.files: list[file] = []

  def __str__(self) -> str:
    return f"Dir [{self.name}]"

  def add_subdir(self, subdir):
    self.subdirs.append(subdir)

  def add_file(self, file):
    self.files.append(file)

  def get_total_size(self):
    size = 0
    for f in self.files:
      size += f.size
    for d in self.subdirs:
      size += d.get_total_size()
    return size

def test_directories():
  dir_a = directory("A")
  dir_a.add_file(file("a", 1))
  dir_a.add_file(file("b", 2))
  print(dir_a)
  print(dir_a.get_total_size())

  dir_b = directory("B")
  dir_b.add_file(file("c", 3))
  print(dir_b.get_total_size())

  dir_a.add_subdir(dir_b)
  print(dir_a)
  print(dir_a.get_total_size())

#test_directories()

def maybeprint(txt, debug):
  if debug:
    print(txt)

def day7_preprocess(input, debug):
  root_dir = directory("/") # Assume start at root??
  current_dir_path = [root_dir]
  lines = dropNothing(input.split("\n"))
  for l in lines[1:]:
    if l[0] == "$":
      command = l[2:4]
      if command == "cd":
        dir_name = l[5:]
        if dir_name == "..":
          maybeprint("GO UP A DIR", debug)
          current_dir_path.pop()
        else:
          newdir = directory(dir_name)
          maybeprint(f"CD {newdir}", debug)
          current_dir_path[-1].add_subdir(newdir)
          current_dir_path.append(newdir)
      elif command == "ls":
        maybeprint(f"LS", debug)
    else:
      if l[:3] == "dir":
        maybeprint(f"DIR {l[4:]}", debug)
      else:
        [size, filename] = l.split(" ")
        maybeprint(f"FILE {filename} - {size}", debug)
        newfile = file(name=filename, size=int(size))
        current_dir_path[-1].add_file(newfile)
  maybeprint(root_dir, debug)
  maybeprint(root_dir.get_total_size(), debug)
  return root_dir

def day7a(input, debug=False):
  root_dir = day7_preprocess(input, debug)

  # BFS
  l: list[directory] = []
  l.append(root_dir)

  size_of_all_candidates = 0
  while l:
    curr = l.pop()
    l.extend(curr.subdirs)
    size = curr.get_total_size()
    if size <= 100000:
      size_of_all_candidates += size
  return size_of_all_candidates

def day7b(input, debug=False):
  root_dir = day7_preprocess(input, debug)
  
  total_disk_space = 70000000
  used_disk_space = root_dir.get_total_size()
  currently_available_disk_space = total_disk_space - used_disk_space
  additional_needed_disk_space = 30000000 - currently_available_disk_space

  smallest_sufficient_dirsize_to_delete = used_disk_space

  # BFS
  l: list[directory] = []
  l.append(root_dir)

  while l:
    curr = l.pop()
    l.extend(curr.subdirs)
    size = curr.get_total_size()
    if additional_needed_disk_space <= size < smallest_sufficient_dirsize_to_delete:
      smallest_sufficient_dirsize_to_delete = size

  return smallest_sufficient_dirsize_to_delete


def count_visible(visible):
  count = 0
  for row in visible:
    for entry in row:
      if entry:
        count += 1
  return count

def day8(input):
  lines = dropNothing(input.split("\n"))
  num_rows = len(lines)
  num_cols = len(lines[0])

  visible = [[False for y in range(num_rows)] for x in range(num_cols)]

  for i in range(num_rows):
    highest_left = -1
    for j in range(num_cols):
      x = int(lines[i][j])
      if x > highest_left:
        highest_left = x
        visible[i][j] = True

    highest_right = -1
    for j in range(num_cols)[::-1]:
      x = int(lines[i][j])
      if x > highest_right:
        highest_right = x
        visible[i][j] = True

  for j in range(num_cols):
    highest_up = -1
    for i in range(num_rows):
      x = int(lines[i][j])
      if x > highest_up:
        highest_up = x
        visible[i][j] = True

    highest_down = -1
    for i in range(num_rows)[::-1]:
      x = int(lines[i][j])
      if x > highest_down:
        highest_down = x
        visible[i][j] = True

  return count_visible(visible)

# def day8b(input):
#   return -1

def add_letter_around_outside(lines, letter):
  # num_rows = len(lines)
  num_cols = len(lines[0])
  first_row = letter * (num_cols+2)
  middle_rows = [letter + l + letter for l in lines]
  last_row = letter * (num_cols+2)
  return [first_row] + middle_rows + [last_row]


def compute_scenic_score(lines, i, j, maximum):
  left = 1
  while lines[i][j] > lines[i][j - left]:
    left += 1
  if lines[i][j - left] == maximum:
    left -= 1

  right = 1
  while lines[i][j] > lines[i][j + right]:
    right += 1
  if lines[i][j + right] == maximum:
    right -= 1

  up = 1
  while lines[i][j] > lines[i - up][j]:
    up += 1
  if lines[i - up][j] == maximum:
    up -= 1

  down = 1
  while lines[i][j] > lines[i + down][j]:
    down += 1
  if lines[i + down][j] == maximum:
    down -= 1

  # print(left, right, up, down)
  return left * right * up * down



def day8b(input):
  lines = dropNothing(input.split("\n"))
  num_rows = len(lines)
  num_cols = len(lines[0])

  sentinel = "A"
  lines2 = add_letter_around_outside(lines, sentinel)

  highest_scenic_score = 0
  for i in range(num_rows):
    for j in range(num_cols):
      score = compute_scenic_score(lines2, i + 1, j + 1, sentinel)
      if score > highest_scenic_score:
        highest_scenic_score = score

  return highest_scenic_score

def get_new_head(old_head, dir):
  (x, y) = old_head
  if dir == "R":
    return (x, y+1)
  elif dir == "L":
    return (x, y-1)
  elif dir == "U":
    return (x+1, y)
  elif dir == "D":
    return (x-1, y)

def get_new_tail(old_tail, new_head):
  diff_x = new_head[0] - old_tail[0]
  diff_x_magnitude = abs(diff_x)
  dir_x = 1 if diff_x > 0 else -1
  diff_y = new_head[1] - old_tail[1]
  diff_y_magnitude = abs(diff_y)
  dir_y = 1 if diff_y > 0 else -1

  if diff_x_magnitude <= 1 and diff_y_magnitude <= 1:
    return old_tail

  if diff_x_magnitude == 2 and diff_y_magnitude == 2:
    return (new_head[0] - dir_x, new_head[1] - dir_y)

  if diff_x_magnitude == 2:
    return (new_head[0] - dir_x, new_head[1])

  if diff_y_magnitude == 2:
    return (new_head[0], new_head[1] - dir_y)
  
  print(f"OH NO {old_tail} {new_head}")

def day9(input, debug=False):
  current_head = (0,0)
  current_tail = (0,0)
  tail_positions = set()
  tail_positions.add(current_tail)
  lines = dropNothing(input.split("\n"))
  for line in lines:
    maybeprint(line, debug)
    [dir, num] = line.split(" ")
    num = int(num)
    # part 1 (first step might go diagonally or not)
    new_head = get_new_head(current_head, dir)
    new_tail = get_new_tail(current_tail, new_head)
    tail_positions.add(new_tail)
    current_head = new_head
    current_tail = new_tail
    maybeprint(f"{current_head} {current_tail}", debug)
    # part 2 (second step might move tail or not)
    if num > 1:
      new_head = get_new_head(current_head, dir)
      new_tail = get_new_tail(current_tail, new_head)
      tail_positions.add(new_tail)
      current_head = new_head
      current_tail = new_tail
      maybeprint(f"{current_head} {current_tail}", debug)
    # part 3 (tail follows head)
    while num > 2:
      new_head = get_new_head(current_head, dir)
      new_tail = current_head
      tail_positions.add(new_tail)
      current_head = new_head
      current_tail = new_tail
      num -= 1
      maybeprint(f"{current_head} {current_tail}", debug)
  return len(tail_positions)

def get_signal_strength_to_add(cycle, value):
  cycles_to_check = set([20, 60, 100, 140, 180, 220])
  if cycle in cycles_to_check:
    return cycle * value
  else:
    return 0

def day10(input, debug=False):
  lines = dropNothing(input.split("\n"))
  # cycles_to_check = set([20, 60, 100, 140, 180, 220])

  current_cycle = 1
  register_x_value = 1
  
  total_signal_strength = 0
  for line in lines:
    maybeprint(f"@ Value in mid of cycle {current_cycle} = {register_x_value}", debug)
    total_signal_strength += get_signal_strength_to_add(current_cycle, register_x_value)

    if line == "noop":
      current_cycle += 1
    else:
      # maybeprint(value_to_add, debug)
      current_cycle += 1
      maybeprint(f"* Value in mid of cycle {current_cycle} = {register_x_value}", debug)
      total_signal_strength += get_signal_strength_to_add(current_cycle, register_x_value)
      current_cycle += 1
      # maybeprint(f"& Value in mid of cycle {current_cycle} = {register_x_value}", debug)
      # total_signal_strength += get_signal_strength_to_add(current_cycle, register_x_value)
      register_x_value += int(line.split(" ")[1])

  return total_signal_strength


def is_divisible(a: int, b: int) -> bool:
  return (a / b) % 1 == 0

huge = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

class monkey():
  def __init__(self, id, operation, test, partb) -> None:
    self.id = id
    self.partb = partb

    if " + " in operation:
      self.to_add = int(operation.split(" + ")[1])
      self.to_multiply = 1
      self.to_square = False
    elif "old * old" in operation:
      self.to_add = 0
      self.to_multiply = 1
      self.to_square = True
    elif " * " in operation:
      self.to_add = 0
      self.to_multiply = int(operation.split(" * ")[1])
      self.to_square = False

    self.testDivisibleBy = int(test[0].split(" ")[-1])
    self.ifmonkey = int(test[1].split(" ")[-1])
    self.elsemonkey = int(test[2].split(" ")[-1])

    self.inspectionCount = 0

  def __str__(self) -> str:
    return f"Monkey {self.id}"

  def giveItem(self, i):
    self.inspectionCount += 1

    # Apply self.operation to i
    newWorryLevel = (i + self.to_add) * self.to_multiply
    if self.to_square:
      newWorryLevel = i * i
    
    if self.partb:
      newWorryLevel = newWorryLevel % huge
    else:
      newWorryLevel = newWorryLevel // 3

    if is_divisible(newWorryLevel, self.testDivisibleBy):
      return (self.ifmonkey, newWorryLevel)
    else:
      return (self.elsemonkey, newWorryLevel)


def day11(input, partb=False, debug=False):
  lines = dropNothing(input.split("\n"))
  num_monkeys = int(len(lines) / 6)

  items = [[] for i in range(num_monkeys)]

  monkeys = []

  for i in range(num_monkeys):
    starting_items = lines[i * 6 + 1].split(":")[1].split(",")
    items[i] = [int(num.strip()) for num in starting_items]
    maybeprint(items[i], debug)

    operation = lines[i * 6 + 2]
    test = lines[i * 6 + 3 : i * 6 + 6]
    m = monkey(i, operation, test, partb)
    maybeprint(m, debug)
    monkeys.append(m)

  num_rounds = 10000 if partb else 20

  for round in range(num_rounds):
    for i in range(num_monkeys):
      m = monkeys[i]
      monkeyitems = items[i]
      items[i] = []
      for monkeyitem in monkeyitems:
        (newMonkey, newWorryLevel) = m.giveItem(monkeyitem)
        items[newMonkey].append(newWorryLevel)
    # maybeprint(items, debug)

  inspectionCounts = [m.inspectionCount for m in monkeys]
  maybeprint(inspectionCounts, debug)
  inspectionCounts.sort(reverse=True)
  # maybeprint(inspectionCounts, debug)
  return inspectionCounts[0] * inspectionCounts[1]
