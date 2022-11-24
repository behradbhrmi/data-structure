
# _map =  [
#     [0, 0, 1, 1],
#     [0, 1, 0, ],
#     [0, 0, 0],
#   ]

_map = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0],


]
path_stack = []

col = len(_map) -1
row = len(_map[0]) -1

found = False

def printer(input):
    for row in input:
        for col in row:
            print(col, end=' ')
        print()

def maze(y, x, finish_y, finish_x):
    global found
    if found == True:
        return 

    if x > row or y > col : 
        return

    if x < 0 or y < 0 :
        return
    
    if [y, x] in path_stack:
        return
    
    val = _map[y][x]
    # print(val)
    if val == 1 :
        return 

    path_stack.append([y, x])

    if x == finish_x:
        print('x is ok')
    if y == finish_y :
        print('y is ok')
    if x == finish_x and y == finish_y :
        found = True
        print('done')
        return 
    
    maze(y+1, x  , finish_y, finish_x)
    maze(y+1, x+1, finish_y,  finish_x)
    maze(y ,x+1, finish_y, finish_x)
    maze(y-1, x+1, finish_y, finish_x)
    maze(y-1, x, finish_y, finish_x)
    maze(y-1, x-1, finish_y, finish_x)
    maze(y, x-1, finish_y, finish_x)
    maze(y+1, x-1, finish_y, finish_x)

def main():
    maze(0, 0, 4, 5)
    printer(_map)
    print()
    print(path_stack)
    print(found)

main()