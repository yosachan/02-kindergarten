import random
import math

BOARD_SIZE = 9

def generate_pos(size):
    x = random.randrange(0,size)
    y = random.randrange(0, size)

    return (x, y)

def calc_distance(pos1, pos2):
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)

def move_pos(direction, pos):
   current_x, current_y = pos
   
   if direction == 'r':
       current_y = current_y - 1
   elif direction == 'v':
       current_y = current_y + 1
   elif direction == 'f':
       current_x = current_x - 1
   elif direction == 'g':
       current_x = current_x + 1
   
   return (current_x, current_y)
    
def suika_wari():
    suika_pos = generate_pos(BOARD_SIZE)
    player_pos = generate_pos(BOARD_SIZE)

    while (suika_pos != player_pos):
        distance = calc_distance(player_pos, suika_pos)
        print(distance)
        c = input('r:北に移動 v:南に移動 g:東に移動 f:西に移動')
        player_pos = move_pos(c, player_pos)
    print('OK')
      
suika_wari()





