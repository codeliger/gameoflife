class Universe:

    def __init__(self):
        self.index = dict()
        self.neighbours = [(x,y) for x in range(-1,2) for y in range(-1,2) if not (x == 0 and y == 0)]

    def __iter__(self):
        self.index.__iter__()

    def get_cell_at(self, position:tuple):
        return self.index[position]

    def has_cell_at(self,position:tuple):
        return position in self.index

    def revive_cell_at(self,position:tuple):
        if position in self.index:
            self.index[position] = True
        else:
            raise Exception("Could not revive a cell at {0} because it doesn't exist.".format(position))

    def kill_cell_at(self,position:tuple):
        if position in self.index:
            self.index[position] = False

    def create_cell_at(self,position:tuple):
        if self.has_cell_at(position):
            print("Overwriting cell at {0}".format(position))
        self.index[position] = True

    def destroy_cell_at(self,position:tuple):
        if position in self.index:
            self.index.pop(position)
        else:
            raise Exception("Could not destroy a cell at {0} because it doesn't exist.".format(position))

    def get_cell_neighbours(self,position:tuple)->list:
        return [tuple([position[0]+neighbour[0],position[1]+neighbour[1]]) for neighbour in self.neighbours]

    def get_cell_neighbour_states(self,cell_neighbours:list)->list:
        return [self.return_cell_at(position) for position in cell_neighbours]

    def count_alive_cell_neighbours(self,cell_neighbour_states:list)->int:
        return cell_neighbour_states.count(True)


if __name__ == '__main__':
    u = Universe()
    u.create_cell_at((0,1))
    u.create_cell_at((0,2))
    u.create_cell_at((0,3))




















