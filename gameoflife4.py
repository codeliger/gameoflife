intersections = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

diagnals = {
    'SE': (1, -1),
    'SW': (-1, -1),
    'NE': (1, 1),
    'NW': (-1, 1)
}

cells = dict()
cells[(0,1)] = True
cells[(0,2)] = True
cells[(0,3)] = True

for c in cells:

    def check_cell(position: tuple):
        cv = cells[c]
        count = 0
        for n in NEIGHBOURHOOD:
            nv = NEIGHBOURHOOD[n]
            neighbour = tuple([nv[0]+c[0],nv[1]+c[1]])
            if neighbour in cells.keys():
                count += 1
        print("Cell {0} has {1} neighbours".format(c,count))







