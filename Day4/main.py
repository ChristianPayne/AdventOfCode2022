with open("input.txt", "r") as f:
 data = f.read()

def getRange (elf_range: str):
  start, end = elf_range.split('-')
  return list(range(int(start), int(end) + 1))

def fully_overlapped(a: list, b: list):
  len_set = len(set([*a, *b]))
  return len_set == len(a) or len_set == len(b)

pairs = [x.split(',') for x in data.split('\n')]

def PartOne():
  overlapped_pairs = [pair for pair in pairs if fully_overlapped(getRange(pair[0]), getRange(pair[1]))]
  print('Part One | Overlapped Pairs:', len(overlapped_pairs))

PartOne()