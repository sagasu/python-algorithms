from sympy import Add, Eq, Symbol, linsolve, solve, symbols


def solve(sections):
    w = symbols("w:14")
    z = []

    eqns = []

    for i, x in enumerate(sections):
        a, b, c = [int(x[i].split()[-1]) for i in (3, 4, 14)]
        if a == 26:
            eqns.append(Eq(z.pop(), w[i] - b))
        else:
            z.append(w[i] + c)

    return next(iter(linsolve(eqns, w[::-1])))[::-1]


def p1(f):
    sections = [x.strip().splitlines() for x in f.read().split("inp w")][1:]
    sol = solve(sections)
    subs = {}

    for var in sol:
        if not isinstance(var, Symbol):
            continue
        for val in range(9, 0, -1):
            result = [other.subs({**subs, var: val}) for other in sol]
            if all(isinstance(x, (Symbol, Add)) or 1 <= x <= 9 for x in result):
                subs[var] = val
                break

    print("".join(str(var.subs(subs)) for var in sol))


def p2(f):
    sections = [x.strip().splitlines() for x in f.read().split("inp w")][1:]
    sol = solve(sections)
    subs = {}

    for var in sol:
        if not isinstance(var, Symbol):
            continue
        for val in range(1, 10):
            result = [other.subs({**subs, var: val}) for other in sol]
            if all(isinstance(x, (Symbol, Add)) or 1 <= x <= 9 for x in result):
                subs[var] = val
                break

    print("".join(str(var.subs(subs)) for var in sol))

data = """
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 1
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -2
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 3
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x 0
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -4
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 7
mul y x
add z y"""

f = open('aoc2021/24.in', 'r')

#print(p1(f))
print(p2(f))