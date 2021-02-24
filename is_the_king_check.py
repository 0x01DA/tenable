from itertools import product


def raw_input():
  return """w,p,c6+w,q,c8+w,p,g7+w,k,e5+b,b,b2+b,p,f3+b,k,f1 w,p,c4+w,r,a6+w,p,e6+w,p,h6+w,p,g7+w,k,h5+b,r,b2+b,p,f3+b,k,c2"""

def get_pos(pos):
  x = ord(pos[0]) - 96
  y = int(pos[1])
  return [x,y]

def pawn_mov(color, position):
  x, y = position
  if color == 'w':
    y = y + 1
  else:
    y = y - 1
  return [x,y]

def queen_mov(pos):
  x, y = pos

  return "{}{}".format(x,y)


def knight_moves(position):
    x, y = position
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
    return moves

def rook_moves(position):
  x, y = position
  moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
  moves = [[x,y] for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
  return moves

def bishop_moves(position):
  x, y = position
  moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
  moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
  return moves


'''
Takes '+' and ' ' delimited data of chess matches and parses into list of seperate matches
''' 
def ParseMatches(chess_matches):
    return [c.split('+') for c in chess_matches.split(' ')]

'''
:param chess_match: A list of chess pieces and their location on the board. ie: ['w,p,a2', 'w,q,a6','w,k,c1','b,r,h1','b,k,g3']
:return: returns True or False if a King is in check
'''
def IsKingInCheck(chess_match):
  blocked = {'w': [], 'b': []}
  king = {}
  for piece in chess_match:
    color = piece[0]
    rank  = piece[2]
    pos   = get_pos(piece[4:6])
    print(pos)
    if rank == 'p':
      blocked[color].append(pawn_mov(color, pos))
    if rank == 'n':
      blocked[color].append(knight_moves(pos))
    if rank == 'r':
      blocked[color].extend(rook_moves(pos))
    if rank == 'b':
      blocked[color].append(bishop_moves(pos))
    if rank == 'q':
      blocked[color].append(queen_mov(pos))
    if rank == 'k':
      king[color] = pos

  print(blocked)
  print(king)
  if king['w'] in blocked['b'] or king['b'] in blocked['w']:
    return True

  return False


result = []
chess_matches = ParseMatches(raw_input())
for chess_match in chess_matches:
    result.append(IsKingInCheck(chess_match))
    
print(result)
