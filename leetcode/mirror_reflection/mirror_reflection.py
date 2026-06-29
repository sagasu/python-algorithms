from typing import List
import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0:
            return 0
        if p == 0:
            return 2
        
        lcm = p * q // math.gcd(p,q)
        if(lcm // p) % 2 == 0:
            return 0
        if(lcm // q) % 2 == 0:
            return 2
        return 1