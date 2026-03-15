MOD = 1_000_000_007

class Fancy:
    def __init__(self):
        # Every stored raw value represents the actual value via: actual = a * raw + b
        self.vals = []
        self.a = 1  # global multiplier
        self.b = 0  # global offset

    def append(self, val: int) -> None:
        # Reverse the current transform to get the raw value:
        # actual = a * raw + b  =>  raw = (val - b) * a^(-1)  (mod MOD)
        # a^(-1) mod p = a^(p-2) mod p  by Fermat's little theorem
        raw = (val - self.b) % MOD * pow(self.a, MOD - 2, MOD) % MOD
        self.vals.append(raw)

    def addAll(self, inc: int) -> None:
        # actual + inc = a * raw + (b + inc)
        self.b = (self.b + inc) % MOD

    def multAll(self, m: int) -> None:
        # (a * raw + b) * m = (a*m) * raw + (b*m)
        self.a = self.a * m % MOD
        self.b = self.b * m % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        return (self.a * self.vals[idx] + self.b) % MOD
