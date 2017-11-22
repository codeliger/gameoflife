class Universe:

    def __init__(self):
        self.index = dict()
        self.neighbours = [(x,y) for x in range(-1,2) for y in range(-1,2) if not (x == 0 and y == 0)]

    def __iter__(self):
        return self.index.__iter__()

    def has_cell_at(self,position:tuple):
        return position in self.index

    def get_cell_at(self, position:tuple):
        value = self.index[position]
        if value is None:
            raise Exception("Could not revive a cell at {0}".format(value))
        else:
            return value

    def create_cell_at(self,position:tuple):
        if self.has_cell_at(position):
            print("Overwriting cell at {0}".format(position))
        self.index[position] = True

    def destroy_cell_at(self,position:tuple):
        if self.has_cell_at(position):
            self.index.pop(position)
        else:
            raise Exception("Could not destroy a cell at {0} because it doesn't exist.".format(position))

    def revive_cell_at(self,position:tuple):
        if self.has_cell_at(position):
            self.index[position] = True
        else:
            raise Exception("Could not revive a cell at {0} because it doesn't exist.".format(position))

    def kill_cell_at(self,position:tuple):
        if self.has_cell_at(position):
            self.index[position] = False
        else:
            raise Exception("Could not kill cell at {0} because it doesn't exist.".format(position))





if __name__ == '__main__':
    universe = Universe()
    universe_b = Universe()
    universe.create_cell_at((0,1))
    universe.create_cell_at((0,2))
    universe.create_cell_at((0,3))

    def getCellState(location:tuple):
        neighbour_count = 0
        dead_cells_to_create = list()
        for neighbour in universe.neighbours:
            neighbour = tuple([cell[0] + neighbour[0], cell[1] + neighbour[1]])
            if universe.has_cell_at(neighbour):
                neighbour_state = universe.get_cell_at(neighbour)
                if neighbour_state == True:
                    neighbour_count+=1
            else:
                dead_cells_to_create.append(neighbour)
        cell_state = neighbour_count > 1 and neighbour_count < 4
        if cell_state:
            return map(getCellState,set(dead_cells_to_create))
        return list(cell)


    #evaluate dead cells
    for cell in universe:
        if universe.index[cell] == False:
            neighbour_count = 0
            for neighbour in universe.neighbours:
                neighbour = tuple([cell[0] + neighbour[0], cell[1] + neighbour[1]])
                if universe.has_cell_at(neighbour):
                    neighbour_state = universe.get_cell_at(neighbour)
                    if neighbour_state == True:
                        neighbour_count+=1
                else:
                    universe.create_cell_at(neighbour)
                    universe.kill_cell_at(neighbour)
            cell_state = neighbour_count > 1 and neighbour_count < 4
            if cell_state:
                universe_b.create_cell_at(cell)

























