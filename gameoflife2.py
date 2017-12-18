import sys

'''
    Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
'''

class Cell:
  def __init__(self,universe:dict,x,y,state=False):
    print("Creating cell ",(x,y))
    self.universe = universe
    self.x = x
    self.y = y
    self.current_state = state
    self.future_state = None
    self.neigbour_locations = [(self.x+nx,self.y+ny) for nx in range(-1,2) for ny in range(-1,2) if not (nx == 0 and ny == 0)]
  
  def __eq__(self,o):
    if type(o) == type(self) and self.x == o.x and self.y == o.y and self.current_state == o.current_state and self.future_state == o.future_state:
      return True
    return False

  def __str__(self):
    return "str:" + str((self.x,self.y))

  def pair(self):
    return (self.x,self.y)

  def create_dead(self):
    for n in self.neigbour_locations:
      if n not in self.universe:
        c = Cell(self.universe,n[0],n[1])
        self.universe[c.pair()] = c

  def count_alive(self):
    count = 0
    for n in self.neigbour_locations:
      print("Checking in universe for ",n)
      if n in self.universe:
        if self.universe[n].current_state: 
          print(self.pair(),' neighbour ',n," is alive")
          count += 1
    return count

  # Set the next state of the cell
  def update_future_state(self,neighbour_count):
    self.future_state = (self.current_state and (neighbour_count == 2 or neighbour_count == 3)) or (not self.current_state and neighbour_count == 2)

  # Update the current state of the cell to next iteration
  def update_current_state(self):
      self.current_state = self.future_state
      self.future_state = None

def create_grid_pairs(universe:dict):
  minx = 0
  miny = 0
  maxx = 0
  maxy = 0
  for pair in universe:
    if minx > pair[0]:
      print(minx," is less than ", pair[0])
      minx = pair[0] 
    if miny > pair[1]:
      print(miny," is less than ", pair[1])      
      miny = pair[1]
    if maxx < pair[0]: 
      print(maxx," is less than ", pair[0])            
      maxx = pair[0]
    if maxy < pair[1]: 
      print(maxy," is less than ", pair[1])                  
      maxy = pair[1]
    rangex = abs(maxx-minx)
    rangey = abs(maxy-miny)
  print(pair,minx,miny,maxx,maxy)      
  return (range(minx-2,maxx+2),range(miny-2,maxy+2))

def print_grid(universe:dict):
  grid_pairs = create_grid_pairs(universe)
  for x in grid_pairs[0]:
    for y in grid_pairs[1]:
      pair = (x,y)
      if pair in universe:
        if universe[pair].current_state:
          sys.stdout.write('A')
        else:
          sys.stdout.write('D')
      else:
        sys.stdout.write('X')
    print()

if __name__ == '__main__':

  universe = dict()

  c = Cell(universe,0,0,True)
  universe[c.pair()] = c

  c = Cell(universe,0,1,True)
  universe[c.pair()] = c

  c = Cell(universe,0,2,True)
  universe[c.pair()] = c

  print_grid(universe)

  for pair in dict(universe):
    universe[pair].create_dead()
    
  for pair in dict(universe):
    neighbours = universe[pair].count_alive()
    print(pair,"has",neighbours,'neighbours')
    if neighbours == 0:
      del universe[pair]
    else:
      universe[pair].update_future_state(neighbours)
      universe[pair].update_current_state()













  


