from typing import Protocol


class Rater(Protocol):
    def rate(self, value: float) -> float: ...


class SmallerWebHexagon:
    def __init__(self, rater: Rater):
        self.rater = rater  # the database port needs configuring

    def rate_and_result(self, value: float) -> tuple[float, float]:
        rate = self.rater.rate(value)
        result = value * rate
        return rate, result
