def power_15_naive(x):
    return x * x * x*x*x*x*x*x*x*x*x*x*x*x*x

def power_15_binary(x):
    x2 = x*x
    x4 = x2 * x2
    x8 = x4*x4
    x12 = x8 * x4
    x14 = x12*x2
    x15 = x14*x
    return x15

print(power_15_naive(2))
print(power_15_binary(2))