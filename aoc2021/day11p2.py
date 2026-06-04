def adj(i, j):
    return (
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 1),
    )


lines = [
    7232374314,
8531113786,
3411787828,
5482241344,
5856827742,
7614532764,
5311321758,
1255116187,
5821277714,
2623834788
]

def p1(f):
    nums = {(i, j): int(x) for i, line in enumerate(f) for j, x in enumerate(line)}

    def dfs(p, t, visited):
        if p in visited or nums[p] + t <= 9:
            return
        visited.add(p)
        for q in adj(*p):
            if q in nums:
                nums[q] += 1
                dfs(q, t, visited)

    def process(t):
        visited = set()
        for p in nums:
            dfs(p, t + 1, visited)
        for p in visited:
            nums[p] = -t - 1
        return len(visited)

    return sum(process(t) for t in range(100))


def p2(f):
    nums = {(i, j): int(x) for i, line in enumerate(f) for j, x in enumerate(line.strip())}

    def dfs(p, t, visited):
        if p in visited or nums[p] + t <= 9:
            return
        visited.add(p)
        for q in adj(*p):
            if q in nums:
                nums[q] += 1
                dfs(q, t, visited)

    def process(t):
        visited = set()
        for p in nums:
            dfs(p, t + 1, visited)
        for p in visited:
            nums[p] = -t - 1
        return len(visited)

    return next(t + 1 for t in range(10 ** 10) if process(t) == len(nums))

p1(lines)