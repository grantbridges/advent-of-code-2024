from base_aoc_day_solutions import *

import re

# https://adventofcode.com/2024/day/3

class Day3Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 3)

    def part_1(self):
        total = 0
        with open(self.input_file, 'r') as f:
            contents = f.read()
            contents = contents.replace('\r\n', '')

            # find all substrings with 'mul(' as our starts
            mul_starts = [m.start() for m in re.finditer('mul\([0-9]+,[0-9]+\)', contents)]

            for s in mul_starts:
                # reasonable substring length to split out on
                substring = contents[s:s+15]

                # first occurence of ) is our end
                end_index = substring.find(')')
                
                # this is the "mul(###,###)"
                mul_expression = contents[s:s+end_index+1]

                # trash what we don't need
                trimmed = mul_expression.replace('mul(', '').replace(')', '')
                numbers = trimmed.split(',')
                left = int(numbers[0])
                right = int(numbers[1])
                total += left * right
        
        return total

    def part_2(self):
        return 0
    
Day3Solutions().run_solutions()