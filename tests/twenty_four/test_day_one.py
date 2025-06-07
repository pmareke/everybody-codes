import pytest
from expects import equal, expect

from src.twenty_four.day_one import DayOne


class TestDay01:
    @pytest.mark.parametrize(
        "filename, expected",
        [
            ("inputs/2024/01_01.example", 5),
            ("inputs/2024/01_01.in", 1289),
        ],
    )
    def test_solve_part_one(self, filename: str, expected: int) -> None:
        day_one = DayOne(filename)

        result = day_one.part_one()

        expect(result).to(equal(expected))

    @pytest.mark.parametrize(
        "filename, expected",
        [
            ("inputs/2024/01_02.example", 28),
            ("inputs/2024/01_02.in", 5593),
        ],
    )
    def test_solve_part_two(self, filename: str, expected: int) -> None:
        day_one = DayOne(filename)

        result = day_one.part_two()

        expect(result).to(equal(expected))
