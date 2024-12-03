from base_aoc_day_solutions import *
from typing import List
from enum import Enum
import copy

# https://adventofcode.com/2024/day/2

class Report:
    def __init__(self, report_number: int, levels: List[int]):
        self.report_number = report_number
        self.levels: List[int] = levels

    def is_safe(self, apply_dampener: bool):
        if Report.check_safe(self.levels):
            return True # easy
        
        if apply_dampener:
            # brute force - remove 1 entry at a time to see if ANY are safe
            for i in range(0, len(self.levels)):
                levels = copy.copy(self.levels)
                levels.pop(i)

                if Report.check_safe(levels):
                    return True # oh yay!

        # not safe :(
        return False

    @staticmethod
    def check_safe(levels):
        direction = 0 # -1 decreasing; +1 increasing
        for i in range(0, len(levels) - 1):
            # compare this one with its neighbor
            curr = levels[i]
            next = levels[i+1]

            # 1) check for equality, which is always bad
            if curr == next:
                return False

            # 2) determine direction if we haven't yet
            if direction == 0:
                direction = 1 if next > curr else -1

            # 3) ensure we're moving in the right direction
            if direction == 1 and next < curr or direction == -1 and next > curr:
                # not safe!
                return False

            # 4) ensure the difference is acceptable
            diff = abs(curr - next)
            if diff < 1 or diff > 3:
                return False
            
        # if we've made it this far, we're safe!
        return True

class Day2Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 2)

    def part_1(self):
        with open(self.input_file, 'r') as data:
            safe_reports = 0
            line_count = 0
            for line in data.readlines():
                line_count += 1
                levels = [int(x) for x in line.split()]

                report = Report(line_count, levels)
                if report.is_safe(apply_dampener=False):
                    safe_reports += 1

            return safe_reports

    def part_2(self):
        with open(self.input_file, 'r') as data:
            safe_reports = 0
            line_count = 0
            for line in data.readlines():
                line_count += 1
                levels = [int(x) for x in line.split()]

                report = Report(line_count, levels)
                if report.is_safe(apply_dampener=True):
                    safe_reports += 1

            return safe_reports
    
Day2Solutions().run_solutions()