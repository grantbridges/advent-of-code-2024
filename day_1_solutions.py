from base_aoc_day_solutions import *

# https://adventofcode.com/2024/day/1

class Day1Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 1)

    def part_1(self):
        with open(self.input_file, 'r') as file:
            # track two lists for each column
            left_list = []
            right_list = []

            # for each line, store the left and right value in their
            # corresponding lists (assume separation by '   ')
            for line in file.readlines():
                vals = line.split('   ')
                left_list.append(int(vals[0]))
                right_list.append(int(vals[1]))

            # sort each list numerically
            left_list.sort()
            right_list.sort()

            distance_total = 0
            for i in range(0, len(left_list)): # assume lists are same length
                left_val = left_list[i]
                right_val = right_list[i]
                distance = abs(right_val - left_val)
                distance_total += distance

        return distance_total

    def part_2(self):
        with open(self.input_file, 'r') as file:
            left_list = []
            right_dict = dict()

            # read data in...
            for line in file.readlines():
                vals = line.split('   ')
                left_val = int(vals[0])
                right_val = int(vals[1])

                # store left_val in left_list dumbly
                left_list.append(left_val)

                # treat right_vals as a dictionary, tracking the number of times
                # each shows up
                if (right_val not in right_dict):
                    right_dict[right_val] = 0
                right_dict[right_val] += 1
            
            # Check over left list and count the number of times that
            # same number shows up in right list, then total up "similarity score"
            # as left_val * right_dict[val] (i.e. its occurrences in right list)
            total_similarity_score = 0
            for val in left_list:
                if (val in right_dict):
                    similarity_score = val * right_dict[val]
                    total_similarity_score += similarity_score

            return total_similarity_score
    
Day1Solutions().run_solutions()