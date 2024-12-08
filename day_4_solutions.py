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

            # assuming square grid
            row_count = len(grid)
            col_count = len(grid[0])

            # keep track of occurrences in each direction, just to sanity check that all get picked up at some point
            nw = n = ne = w = e = sw = s = se = 0
            for row in range(0, row_count):
                for col in range(0, col_count):
                    if grid[row][col] == 'X':
                        # look above
                        if row >= 3:
                            # NW
                            if col >= 3:
                                if grid[row-1][col-1] == 'M' and grid[row-2][col-2] == 'A' and grid[row-3][col-3] == 'S':
                                    nw += 1
                            # N
                            if grid[row-1][col] == 'M' and grid[row-2][col] == 'A' and grid[row-3][col] == 'S':
                                n += 1
                            # NE
                            if col < col_count - 3:
                                if grid[row-1][col+1] == 'M' and grid[row-2][col+2] == 'A' and grid[row-3][col+3] == 'S':
                                    ne += 1
                        # look left
                        if col >= 3:
                            if grid[row][col-1] == 'M' and grid[row][col-2] == 'A' and grid[row][col-3] == 'S':
                                w += 1
                        # look right
                        if col < col_count - 3:
                            if grid[row][col+1] == 'M' and grid[row][col+2] == 'A' and grid[row][col+3] == 'S':
                                e += 1
                        # look below
                        if row < row_count - 3:
                            # SW
                            if col >= 3:
                                if grid[row+1][col-1] == 'M' and grid[row+2][col-2] == 'A' and grid[row+3][col-3] == 'S':
                                    sw += 1
                            # S
                            if grid[row+1][col] == 'M' and grid[row+2][col] == 'A' and grid[row+3][col] == 'S':
                                s += 1
                            # SE
                            if col < col_count - 3:
                                if grid[row+1][col+1] == 'M' and grid[row+2][col+2] == 'A' and grid[row+3][col+3] == 'S':
                                    se += 1

            total_count = nw + n + ne + w + e + sw + s + se
            log_debug(f'Totals: nw {nw} n {n} ne {ne} w {w} e {e} sw {sw} s {s} se {se}')
            log_debug(f'Grand Total: {total_count}')
            
            return total_count

    def part_2(self):
         with open(self.input_file, 'r') as f:
            grid = []
            for l in f.readlines():
                l = l.replace('\n', '')
                grid.append(l)

            # assuming square grid
            row_count = len(grid)
            col_count = len(grid[0])

            # there's only 4 configurations we have to check for
            c1 = c2 = c3 = c4 = 0

            # We're looking for "A" as our X centers, then just need to check directly 
            # around it for MAS patterns. So we can disregard the outer edge of the grid 
            # for the loop ranges.
            for row in range(1, row_count-1):
                for col in range(1, col_count-1):
                    if grid[row][col] == 'A':
                        # shorthand variables for each diagonal direction (top-left, top-right, etc)
                        tl = grid[row-1][col-1]
                        tr = grid[row-1][col+1]
                        bl = grid[row+1][col-1]
                        br = grid[row+1][col+1]

                        if tl == 'M' and tr == 'M' and bl == 'S' and br == 'S':
                            c1 += 1
                        if tl == 'M' and tr == 'S' and bl == 'M' and br == 'S':
                            c2 += 1
                        if tl == 'S' and tr == 'S' and bl == 'M' and br == 'M':
                            c3 += 1
                        if tl == 'S' and tr == 'M' and bl == 'S' and br == 'M':
                            c4 += 1

            total_count = c1 + c2 + c3 + c4
            log_debug(f'Totals: c1 {c1} c2 {c2} c3 {c3} c4 {c4}')
            log_debug(f'Grand Total: {total_count}')
            return total_count
    
Day4Solutions().run_solutions()