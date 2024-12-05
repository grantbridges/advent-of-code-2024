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
        total = 0
        with open(self.input_file, 'r') as f:
            contents = f.read()

            do_locations = [m.start() for m in re.finditer('do\(\)', contents)]
            dont_locations = [m.start() for m in re.finditer('don\'t\(\)', contents)]

            # initialize good ranges from 0 to first dont location
            good_ranges = [[0, dont_locations[0]]]

            # find all the good ranges iteratively
            last_j = 0
            for i in range(0, len(do_locations)):
                found_upper_limit = False
                for j in range(last_j, len(dont_locations)):
                    if dont_locations[j] < do_locations[i]:
                        continue
                    else:
                        # stick a new good range in here
                        good_ranges.append([do_locations[i], dont_locations[j]])
                        last_j = j
                        found_upper_limit = True
                        break

                if not found_upper_limit:
                    # if we made it here, then we went past the end of dont_locations - free add to a really big number!
                    good_ranges.append([do_locations[i], 10000000])

            log_debug('Good ranges:')
            for g in good_ranges:
                log_debug(f'{g[0]} -> {g[1]}')
            log_debug('--')

            # find all substrings with 'mul(' as our starts
            mul_starts = [m.start() for m in re.finditer('mul\([0-9]+,[0-9]+\)', contents)]

            for s in mul_starts:
                # ensure we're in a good range
                in_good_range = False
                for g in good_ranges:
                    if g[0] <= s and g[1] > s:
                        in_good_range = True
                        log_debug(f'mul() at {s} is in a good range - between {g[0]} and {g[1]}')
                        break
                    
                if not in_good_range:
                    log_debug(f'mul() at {s} is not in a good range')
                    continue

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

Day3Solutions().run_solutions()