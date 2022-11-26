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


def printer(input):
    for row in input:
        print(*row)


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

    if  y == finish_y :
        found = True
        return 
    
    maze(y+1, x  , finish_y, finish_x)
    maze(y+1, x+1, finish_y,  finish_x)
    maze(y ,x+1, finish_y, finish_x)
    maze(y-1, x+1, finish_y, finish_x)
    maze(y-1, x, finish_y, finish_x)
    maze(y-1, x-1, finish_y, finish_x)
    maze(y, x-1, finish_y, finish_x)
    maze(y+1, x-1, finish_y, finish_x)

    if found == True :
        l = [finish_y, finish_x]
        if l not in path_stack:
            path_stack.append(l)


def main():
    system('cls')
    print('---Map---')
    printer(_map)
    print('------')

    print('\n>> Enter the Starting Point Coordinates :')
    start_y =  int(input('[y]: '))
    start_x =  int(input('[x]: '))

    print('\n>> Enter Finishing Point Coordinates :')
    finish_y = int(input('[y]: '))
    finish_x = int(input('[x]: '))

    maze(start_y, start_x, finish_y, finish_x)

    print('------')
    if found == True: print('\nCorrect Path is :\n', *path_stack)
    else: print('> Could Not Reach Finishing Point :(')


if __name__ == '__main__':
    main()
