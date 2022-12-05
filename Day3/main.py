with open("input.txt", "r") as f:
 data = f.read()

ranking = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def GetIntersection (sack: str):
  comp_length = int(len(sack) / 2)
  most_char_comp_1 = sack[0:comp_length]
  most_char_comp_2 = sack[comp_length:]

  intersect_list = [value for value in most_char_comp_1 if value in most_char_comp_2]
  return intersect_list[0]

def GetRank(letter):
  res = [x for x in range(len(ranking)) if ranking[x] == letter] 
  if(len(res) > 0):
    return res[0] + 1
  else:
    return 0

def PartOne():
  rucksacks = [GetIntersection(sack) for sack in data.split('\n')]
  ruck_ranks = [GetRank(ruck) for ruck in rucksacks]
  print('Part 1:', sum(ruck_ranks))


def PartTwo():
  rucksacks = [sack for sack in data.split('\n')]

  ranks = []
  for i, _ in enumerate(rucksacks):
    if((i + 1) % 3 == 0):
      badge = list(set(rucksacks[i]) & set(rucksacks[i - 1]) & set(rucksacks[i - 2]))
      ranks.append(GetRank(badge[0]))

  print("Part 2:", sum(ranks))

PartOne()
PartTwo()
