class ProductOfNumbers:
    """Prefix products since the last zero, so add and getProduct are O(1)."""

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]


if __name__ == "__main__":
    ops = [
        "ProductOfNumbers",
        "add",
        "add",
        "add",
        "add",
        "add",
        "getProduct",
        "getProduct",
        "getProduct",
        "add",
        "getProduct",
    ]
    args = [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]
    expected = [None, None, None, None, None, None, 20, 40, 0, None, 32]

    obj = ProductOfNumbers()
    got = [None]
    for op, arg in zip(ops[1:], args[1:]):
        if op == "add":
            obj.add(arg[0])
            got.append(None)
        else:
            got.append(obj.getProduct(arg[0]))

    if got == expected:
        print("OK")
    else:
        print("FAIL")
        raise SystemExit(1)
