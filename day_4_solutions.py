from base_aoc_day_solutions import *

# https://adventofcode.com/2024/day/4

class Day4Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 4)

    def part_1(self):
        with open(self.input_file, 'r') as f:
            grid = []
            for l in f.readlines():
                l = l.replace('\n', '')
                grid.append(l)

            # assuming grid shape
            row_count = len(grid)
            col_count = len(grid[0])

            total_count = 0
            for y in range(0, row_count):
                for x in range(0, col_count):
                    if grid[x][y] == 'X':
                        # look in the directions around for 'M'
                        if y >= 3:
                            # NW
                            if x >= 3:
                                if grid[x-1][y-1] == 'M' and grid[i-2,j-2] == 'A' and grid[i-3,j-3] == 'S':
                                    total_count += 1
                            # N
                            if grid[i-1,j-1] == 'M' and grid[i-2,j-2] == 'A' and grid[i-3,j-3] == 'S':



    def part_2(self):
        return 0
    
Day4Solutions().run_solutions()