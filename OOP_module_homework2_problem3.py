import math

class Duration:
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        if total_seconds < 0:
            total_seconds = 0
        self.hours = total_seconds // 3600
        remaining = total_seconds % 3600
        self.minutes = remaining // 60
        self.seconds = remaining % 60

    @property
    def total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        parts = []
        if self.hours > 0:
            parts.append(f"{self.hours}h")
        if self.minutes > 0:
            parts.append(f"{self.minutes}m")
        if self.seconds > 0:
            parts.append(f"{self.seconds}s")
        return ' '.join(parts) if parts else "0s"

    def __repr__(self):
        return f"Duration({self.hours}, {self.minutes}, {self.seconds})"

    def __add__(self, other):
        return Duration(seconds=self.total_seconds + other.total_seconds)

    def __sub__(self, other):
        diff = self.total_seconds - other.total_seconds
        return Duration(seconds=diff if diff > 0 else 0)

    def __mul__(self, multiplier):
        return Duration(seconds=self.total_seconds * multiplier)

    def __eq__(self, other):
        return self.total_seconds == other.total_seconds

    def __lt__(self, other):
        return self.total_seconds < other.total_seconds

    def __le__(self, other):
        return self.total_seconds <= other.total_seconds


if __name__ == "__main__":
    d1 = Duration(1, 30, 45)
    d2 = Duration(0, 45, 30)
    d3 = Duration(2, 15, 0)

    print("Durations:")
    print(f" d1 = {d1}")
    print(f" d2 = {d2}")
    print(f" d3 = {d3}")

    print("\nArithmetic:")
    print(f" d1 + d2 = {d1 + d2}")
    print(f" d3 - d1 = {d3 - d1}")
    print(f" d2 * 3 = {d2 * 3}")

    print("\nComparisons:")
    print(f" d1 == d2? {d1 == d2}")
    print(f" d1 < d3? {d1 < d3}")
    print(f" d2 <= d1? {d2 <= d1}")

    durations = [d3, d1, d2]
    durations.sort()

    print("\nSorted durations:")
    for d in durations:
        print(f" {d}")

    print("\nOverflow test:")
    d4 = Duration(0, 90, 90)
    print(f" Duration(0, 90, 90) = {d4}")

    print(f"\nRepr: {repr(d1)}")
