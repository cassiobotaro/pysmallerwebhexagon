class IncodeRater:
    def rate(self, value: float) -> float:
        if value <= 100:
            return 1.01
        return 1.5


class FileRater:
    def __init__(self, fn: str):
        self.rates = []
        with open(fn, mode="r") as f:
            for line in f:
                self.rates.append([float(value) for value in line.split()])

    def rate(self, value: float) -> float:
        if value >= self.rates[0][0] and value < self.rates[1][0]:
            rate = self.rates[0][1]
        else:
            rate = self.rates[1][1]
        return rate
