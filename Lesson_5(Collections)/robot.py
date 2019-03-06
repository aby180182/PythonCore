def make_move(sticks):
    while True:
        if (sticks + 1) % 4 == 0:
            return  3
        elif sticks % 2 == 0:
            return 2
        else:
            return 1