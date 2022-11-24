
_map =  [
    [0, 1, 1],
    [0, 1, 0],
    [0, 0, 0],
  ]

path_stack = []

col = len(_map) -1
row = len(_map[0]) -1

found = False

def maze(x, y, finish_x, finish_y):

    if x > row or y > col : 
        return
    if x < 0 or y < 0 :
        return
    
    val = _map[y][x]
    # print(val)
    if val == 1 :
        return 

    global found
    global path_stack

    _map[y][x] = 
    if x == finish_x and y == finish_y :
        found = True
        return path_stack
    path_stack.append([x, y])
    
    maze(x  , y+1, finish_x, finish_y)
    # maze(x+1, y+1, finish_x, finish_y)
    maze(x+1, y  , finish_x, finish_y)
    # maze(x+1, y-1, finish_x, finish_y)
    maze(x  , y-1, finish_x, finish_y)
    # maze(x-1, y-1, finish_x, finish_y)
    maze(x-1, y  , finish_x, finish_y)
    # maze(x-1, y+1, finish_x, finish_y)

    # if found == False:
    #     path_stack = []

print(maze(0, 0, 2, 1))
print(_map)
