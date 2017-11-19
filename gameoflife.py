import operator, multiprocessing

cells = dict()

class Cell:

    def __init__(self, x, y, cells,alive=False):
        self.x = x
        self.y = y
        self.cells = cells
        self.is_alive = alive

    def location(self):
        return tuple([self.x,self.y])

    NEIGHBOURHOOD = {
        'N':(0,1),
        'NE':(1,1),
        'NW':(-1,1),
        'E':(1,0),
        'S':(0,-1),
        'SE':(1,-1),
        'SW':(-1,-1),
        'W':(-1,0)
    }

    def count_neighbours(self):
        i = 0
        for n in self.NEIGHBOURHOOD.values():
            lookup = tuple([self.x+n[0],self.y+n[1]])
            if lookup in self.cells:
                if self.cells[lookup].is_alive:
                    i+=1
        return i

if __name__ == '__main__':

    a = Cell(1,1,cells)
    b = Cell(1,2,cells)
    c = Cell(1,3,cells)

    cells[a.location()] = a
    cells[b.location()] = b
    cells[c.location()] = c

    print(a.count_neighbours())











