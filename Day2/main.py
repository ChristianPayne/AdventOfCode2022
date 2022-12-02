with open("input.txt", "r") as f:
 data = f.read()

moves = [move.split(' ') for move in data.split('\n')]

RPS_MAP = {
  'Z' : 'B',
  'X' : 'C',
  'Y' : 'A',
  'A' : 'Z',
  'B' : 'X',
  'C' : 'Y'
}

DRAW_MAP = {
  'A': 'X',
  'B': 'Y',
  'C': 'Z'
}

RPS_MAP_BACKWARDS = {
  'B': 'Z',
  'C': 'X',
  'A': 'Y'
}

def Get_Move (outcome, their_move):
  # Draw
  if(outcome == 'Y'):
    return DRAW_MAP[their_move]
  elif(outcome == 'X'):
    return RPS_MAP[their_move]
  elif(outcome == 'Z'):
    return RPS_MAP_BACKWARDS[their_move]

# A,X - ROCK LOSE
# B,Y - PAPER DRAW
# C,Z - SCISSORS WIN

RPC_SCORE_MAP = {
  'X': 1,
  'Y': 2,
  'Z': 3
}

SCORE_MULTIPLIER = {
  'lose': 0,
  'draw': 3,
  'win': 6,
}

# Calc two moves and return score. Input my move
def Determine_Round(my_move, their_move):
  # Win
  if(RPS_MAP[my_move] == their_move):
    return RPC_SCORE_MAP[my_move] + SCORE_MULTIPLIER['win']
  # Lose
  elif (my_move == RPS_MAP[their_move]):
    return RPC_SCORE_MAP[my_move] + SCORE_MULTIPLIER['lose']
  else:
    # Draw
    return RPC_SCORE_MAP[my_move] + SCORE_MULTIPLIER['draw']

# Part 1
round_1_results = [Determine_Round(result[1], result[0]) for result in moves]
# Part 2
round_2_results = [Determine_Round(Get_Move(result[1], result[0]), result[0]) for result in moves]

print('Part 1', sum(round_1_results))
print('Part 2', sum(round_2_results))