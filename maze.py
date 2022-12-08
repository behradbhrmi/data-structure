from copy import deepcopy as dc
from os import system


_map = [
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
]
path_stack = []
col = len(_map) -1
row = len(_map[0]) -1
found = False

def maze(y, x, finish_y, finish_x):
    global found
    if finish_y > col or finish_x > row :
        print('>> Error : your X or Y is bigger than map scale. input corret inputs again!')
        return 
    if found == True : return 
    if x > row or y > col : return
    if x < 0 or y < 0 : return
    if [y, x] in path_stack : return
    
    val = _map[y][x]
    if val == 1 : return 
    path_stack.append([y, x])

    if  y == finish_y and x == finish_x:
        found = True
        return 
    maze(y+1, x  , finish_y, finish_x)
    maze(y ,x+1, finish_y, finish_x)
    maze(y-1, x, finish_y, finish_x)
    maze(y, x-1, finish_y, finish_x)
    maze(y+1, x+1, finish_y,  finish_x)
    maze(y-1, x+1, finish_y, finish_x)
    maze(y-1, x-1, finish_y, finish_x)
    maze(y+1, x-1, finish_y, finish_x)

def printer(input_list):
    for row in input_list:
        print(*row)

def correct_path_printer():
    new_list = dc(_map)
    for j, item1 in enumerate(new_list):
        for i, item2 in enumerate(item1) :
            if [j, i] in path_stack:
                new_list[j][i] = 1
                continue
            new_list[j][i] = 0
    printer(new_list)
    return new_list

def main():
    system('cls')
    print('---Map---')
    printer(_map)
    print('------')

    print('>> Enter the Starting Point Coordinates :')
    start_y =  int(input('[y]: '))
    start_x =  int(input('[x]: '))

    print('\n>> Enter Finishing Point Coordinates :')
    finish_y = int(input('[y]: '))
    finish_x = int(input('[x]: '))

    maze(start_y, start_x, finish_y, finish_x)

    if found == True: 
        print('\n--Correct Path--')
        correct_path_printer()
        print("--List--")
        print(*path_stack,"\n")
    else: print('> Could Not Reach Finishing Point :(')

       
if __name__ == '__main__':
    main()
