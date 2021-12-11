def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
    lcm = (a*b) // math.gcd(a, b)
    mod = 10 ** 9 + 7
    low = min(a,b)  
    high = 10 ** 14
    while low < high:
        mid = (low+high) >> 1
        ith = mid // a + mid// b - mid // lcm
        if ith < n:
            low = mid + 1 
        elif ith == n and (mid % a == 0 or mid % b == 0):
            return mid % mod
        else:
            high = mid - 1 
    return high% mod