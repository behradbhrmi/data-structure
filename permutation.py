from os import system


counter = 0


def perm(_list, first, last):
    global counter

    if first == last:

        counter += 1
        return print(f"{counter}. {''.join(_list)}")
    
    for i in range(first, last+1):
        _list[first],_list[i] = _list[i], _list[first]
        perm(_list, first+1, last)
        _list[first],_list[i] = _list[i], _list[first]

    
def main():
    system('cls')
    print('=======(( Start ))=======')

    string = [x for x in input('> Enter Your Array : ')]
    first = 0 
    last  = len(string) - 1
    perm(string, first, last)

    print('=======(( Done ))=======')


if __name__ == '__main__':
    main()
