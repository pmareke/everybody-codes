import re


class DayOne:
    _POINTS = {
        "x": 0,
        "A": 0,
        "B": 1,
        "C": 3,
        "D": 5,
    }

    def __init__(self, filename: str) -> None:
        with open(filename) as file:
            lines = file.readlines()
            lines = list(map(lambda x: x.strip(), lines))
            self.line = lines[0]

    def part_one(self) -> int:
        return sum([self._POINTS[item] for item in self.line])

    def part_two(self) -> int:
        sum = 0
        for idx in range(0, len(self.line), 2):
            x = self.line[idx]
            y = self.line[idx + 1]
            sum += self._POINTS[x] + self._POINTS[y]
            if x != "x" and y != "x":
                sum += 2
        return sum

    def part_three(self) -> int:
        sum = 0
        for idx in range(0, len(self.line), 3):
            x = self.line[idx]
            y = self.line[idx + 1]
            z = self.line[idx + 2]
            total = self._POINTS[x] + self._POINTS[y] + self._POINTS[z]
            sum += total
            if "x" not in (x, y, z):
                sum += 6
                continue
            if "x" not in (x, y):
                sum += 2
            if "x" not in (y, z):
                sum += 2
            if "x" not in (x, z):
                sum += 2
        return sum
