lines = ["LA-sn",
"LA-mo",
"LA-zs",
"end-RD",
"sn-mo",
"end-zs",
"vx-start",
"mh-mo",
"mh-start",
"zs-JI",
"JQ-mo",
"zs-mo",
"start-JQ",
"rk-zs",
"mh-sn",
"mh-JQ",
"RD-mo",
"zs-JQ",
"vx-sn",
"RD-sn",
"vx-mh",
"JQ-vx",
"LA-end",
"JQ-sn"]


edges = {}

for line in lines:
    a, b = line.split("-")
    edges[a] = edges.get(a, []) + [b]
    edges[b] = edges.get(b, []) + [a]

def count(node, visited = set()):
    if node == "end":
        return 1
    total = 0
    for next in edges[node]:
        if next in visited: continue
        total += count(next, visited | {node} if node == node.lower() else visited)
    return total

print(count("start"))