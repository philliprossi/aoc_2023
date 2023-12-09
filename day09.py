import time
from typing import List
from dataclasses import dataclass


with open('inputs/day09.txt') as f:
    data = f.readlines()
data = [[int(d) for d in line.strip().split(" ")] for line in data]


@dataclass
class History:
    history: List[int]

    def find_next_value(self, series: List[int]) -> int:
        result = self._calculate_result(series)
        if all(r==0 for r in result):
            return series[-1]
        return series[-1] + self.find_next_value(result)

    def find_previous_value(self, series: List[int]) -> int:
        result = self._calculate_result(series)
        if all(r==0 for r in result):
            return series[0]
        return series[0] - self.find_previous_value(result)

    @staticmethod
    def _calculate_result(series: List[int]) -> List[int]:
        result = []
        for idx, val in enumerate(series):
            if idx + 1 >= len(series):
                break
            result.append(series[idx + 1] - val)
        return result


hist = [History(d) for d in data]

solution = 0
start = time.time()
for h in hist:
    solution += h.find_next_value(h.history)
end = time.time()
print(f"Solution 1: {solution}")
print(f"Solution 1 took {end-start}s")


solution = 0
start = time.time()
for h in hist:
    solution += h.find_previous_value(h.history)
end = time.time()
print(f"Solution 2: {solution}")
print(f"Solution 2 took {end-start}s")