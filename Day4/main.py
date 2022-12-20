with open("input.txt", "r") as f:
 data = f.read()


def getRange (elf_range: str):
  start, end = elf_range.split('-')
  range_of_elf = list(range(int(start), int(end) + 1))
  return range_of_elf

def compare_ranges(a: list, b: list):
  len_set = len(set([*a, *b]))

  if( len_set == len(a) or len_set == len(b) ):
    return True
  else:
    return False


pairs = [x.split(',') for x in data.split('\n')]

def PartOne():
  ranges = [compare_ranges(getRange(pair[0]), getRange(pair[1])) for pair in pairs]
  print('Part One:', len([x for x in ranges if x == True]))

PartOne()