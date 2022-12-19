import string
with open("input.txt", "r") as f:
 data = f.read()

# Parse input
rows = data.split('\n')
map = [[*row] for row in rows]
scoring_table = [*string.ascii_lowercase]

# Working on getting a class system set up. Not sure if I need a sub class for nodes or not. Just finished working on the GetNeighbors function. Might need a None type return if we hit another path? How do I have multiple paths? Still need to work on getting the height calculations in there for possible path directions.

class Path:
  valid_path: bool = True
  def __init__(self, current_position: tuple, last_position: tuple, height: int, total_steps: int):
    self.current_position = current_position
    self.last_position = last_position
    self.height = height
    self.total_steps = total_steps

  def GetLetterAtPosition(self, position: tuple):
    if(position[0] < 0 or position[1] < 0):
      return None
    if(position[0] > len(map[0]) or position[1] > len(map)):
      return None
    if(position == self.last_position):
      return None
    return map[position[1]][position[0]]

  def GetNeighbors (self):
    north = self.GetLetterAtPosition((self.current_position[0], self.current_position[1] - 1))
    east = self.GetLetterAtPosition((self.current_position[0] + 1, self.current_position[1]))
    south = self.GetLetterAtPosition((self.current_position[0], self.current_position[1] + 1))
    west = self.GetLetterAtPosition((self.current_position[0] - 1, self.current_position[1]))
    return (north, east, south, west)

  def GetHeightOfLetter (letter: str):
    for score, table_letter in enumerate(scoring_table):
      if(letter == table_letter):
        return score

  def JudgeNextStep(self):
    neighbors = self.GetNeighbors()

def FindLetterOnMap (letter: str):
  for y, row in enumerate(map):
    for x, map_letter in enumerate(row):
      if(map_letter == letter):
        return (x,y)

def PartOne ():
  start = FindLetterOnMap('S')
  end = FindLetterOnMap('E')
  print('Starting at',start)
  print('Working towards',end)

  genesis = Path(start, start, 0)
  print(genesis.JudgeNextStep())



PartOne()