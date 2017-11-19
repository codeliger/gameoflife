import unittest, gameoflife

class CellTests(unittest.TestCase):
    def test_a_cell_has_eight_neighbours(self):
        self.assertEqual(8, len(gameoflife.Cell.NEIGHBOURHOOD))

    def test_a_new_cell_is_not_alive(self):
        cell = gameoflife.Cell()
        self.assertEqual(False,cell.is_alive)

    def test_is_alive_is_not_shared_between_cells(self):
        cell_alive = gameoflife.Cell()
        cell_alive.is_alive = True
        cell_dead = gameoflife.Cell()
        cell_dead.is_alive = False
        self.assertEqual(True,cell_alive.is_alive)
        self.assertEqual(False,cell_dead.is_alive)

    def test_still_life_block(self):
        universe = gameoflife.Universe()
        universe.click(2,2)

if __name__ == '__main__':
    unittest.main()
